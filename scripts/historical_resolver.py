#!/usr/bin/env python3
"""Structured historical price resolution for outcome tracking.

Resolvers never use current quotes and never choose a nearby session. The only
option fallback is same-session bid/ask midpoint. Post-expiration valuation uses
intrinsic value on the expiration session, consistent with long-option payoff.
"""
from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone
from typing import Any
from zoneinfo import ZoneInfo

RESOLUTION_STATUSES = {
    "FOUND",
    "NOT_YET_MATURE",
    "NO_TRADING_DAY",
    "INSTRUMENT_NOT_FOUND",
    "INVALID_INSTRUMENT_ID",
    "NO_ROWS_RETURNED",
    "TARGET_DATE_NOT_IN_RESPONSE",
    "OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE",
    "SOURCE_CAPABILITY_UNSUPPORTED",
    "CHECKPOINT_NOT_FOR_TARGET_DATE",
    "PARSE_ERROR",
    "HISTORY_UNAVAILABLE",
    "SOURCE_ERROR",
    "INVALID_RECORD",
}
NON_RETRYABLE_STATUSES = {
    "NO_TRADING_DAY",
    "INSTRUMENT_NOT_FOUND",
    "INVALID_INSTRUMENT_ID",
    "OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE",
    "SOURCE_CAPABILITY_UNSUPPORTED",
    "CHECKPOINT_NOT_FOR_TARGET_DATE",
    "INVALID_RECORD",
}
US_EASTERN = ZoneInfo("America/New_York")
MARKET_CLOSE = time(16, 0)


def parse_date(value: Any) -> date | None:
    try: return date.fromisoformat(str(value)[:10]) if value else None
    except ValueError: return None


def easter(year: int) -> date:
    a=year%19; b=year//100; c=year%100; d=b//4; e=b%4; f=(b+8)//25; g=(b-f+1)//3
    h=(19*a+b-d-g+15)%30; i=c//4; k=c%4; l=(32+2*e+2*i-h-k)%7; m=(a+11*h+22*l)//451
    return date(year,(h+l-7*m+114)//31,((h+l-7*m+114)%31)+1)


def observed(day: date) -> date:
    if day.weekday()==5: return day-timedelta(days=1)
    if day.weekday()==6: return day+timedelta(days=1)
    return day


def nth_weekday(year: int, month: int, weekday: int, n: int) -> date:
    day=date(year,month,1)
    return day+timedelta(days=(weekday-day.weekday())%7+7*(n-1))


def last_weekday(year: int, month: int, weekday: int) -> date:
    day=date(year+int(month==12),(month%12)+1,1)-timedelta(days=1)
    return day-timedelta(days=(day.weekday()-weekday)%7)


def market_holidays(year: int) -> set[date]:
    holidays={observed(date(year,1,1)),nth_weekday(year,1,0,3),nth_weekday(year,2,0,3),easter(year)-timedelta(days=2),last_weekday(year,5,0),observed(date(year,6,19)),observed(date(year,7,4)),nth_weekday(year,9,0,1),nth_weekday(year,11,3,4),observed(date(year,12,25))}
    holidays.add(observed(date(year+1,1,1)))
    return holidays


def is_trading_day(day: date) -> bool:
    return day.weekday()<5 and day not in market_holidays(day.year) and day not in market_holidays(day.year-1)


def trading_day(signal_day: date, horizon: int) -> date:
    current=signal_day; found=0
    while found<horizon:
        current+=timedelta(days=1)
        if is_trading_day(current): found+=1
    return current


def next_trading_session(day: date) -> date:
    current = day
    while not is_trading_day(current):
        current += timedelta(days=1)
    return current


def signal_trading_date(signal_day: date, entry_snapshot_at: Any = None) -> date:
    """Return the trading session that owns the signal.

    Signals stamped after the regular close are evaluated from the next session.
    This keeps after-close research from claiming a close it could not have used.
    """
    session = next_trading_session(signal_day)
    if not entry_snapshot_at:
        return session
    try:
        timestamp = datetime.fromisoformat(str(entry_snapshot_at).replace("Z", "+00:00"))
    except ValueError:
        return session
    if timestamp.tzinfo is None:
        timestamp = timestamp.replace(tzinfo=timezone.utc)
    eastern = timestamp.astimezone(US_EASTERN)
    if eastern.time() >= MARKET_CLOSE:
        return trading_day(eastern.date(), 1)
    return next_trading_session(eastern.date())


def expiration_session(expiration: date) -> date:
    while not is_trading_day(expiration): expiration-=timedelta(days=1)
    return expiration


def _result(status: str, requested: date | None, source: str, **extra: Any) -> dict[str, Any]:
    retryable = extra.pop("retryable", status not in NON_RETRYABLE_STATUSES and status not in {"FOUND", "NOT_YET_MATURE"})
    return {"status":status,"requested_date":requested.isoformat() if requested else None,"resolved_trading_date":extra.pop("resolved_trading_date",None),"price":extra.pop("price",None),"source":source,"instrument_id":extra.pop("instrument_id",None),"retrieved_at":extra.pop("retrieved_at",datetime.now(timezone.utc).isoformat()),"fallback_used":extra.pop("fallback_used",False),"retryable":retryable,**extra}


def source_capabilities(snapshot: dict[str, Any]) -> dict[str, bool]:
    explicit = snapshot.get("capabilities") or {}
    source = str(snapshot.get("source") or snapshot.get("source_id") or "").lower()
    option_bars_present = bool(snapshot.get("option_bars"))
    default_option_history = option_bars_present and "live_equity_history" not in source
    return {
        "equity_historical": bool(explicit.get("equity_historical", True)),
        "benchmark_historical": bool(explicit.get("benchmark_historical", explicit.get("equity_historical", True))),
        "option_historical": bool(explicit.get("option_historical", default_option_history)),
        "option_current_quotes": bool(explicit.get("option_current_quotes", False)),
    }


def _bars(snapshot: dict[str, Any], asset: str, instrument: str) -> dict[str, dict[str, Any]]:
    group=snapshot.get(asset,{})
    return {str(bar.get("date"))[:10]:bar for bar in group.get(instrument,[]) if bar.get("date")}


def _checkpoint_quotes(snapshot: dict[str, Any], option_id: str, target: date) -> dict[str, Any] | None:
    target_text = target.isoformat()
    checkpoints = snapshot.get("option_quote_checkpoints") or {}
    if isinstance(checkpoints, dict):
        dated = checkpoints.get(target_text) or {}
        if option_id in dated:
            return dated[option_id]
    checkpoint_date = str(snapshot.get("checkpoint_date") or snapshot.get("quote_date") or snapshot.get("as_of") or "")[:10]
    if checkpoint_date != target_text:
        return None
    quotes = snapshot.get("option_quotes") or {}
    if isinstance(quotes, dict) and option_id in quotes:
        return quotes[option_id]
    results = ((snapshot.get("data") or {}).get("results") or snapshot.get("results") or [])
    for item in results:
        quote = item.get("quote") if isinstance(item, dict) else None
        if quote and str(quote.get("instrument_id")) == option_id:
            return {"quote": quote, "close": item.get("close")}
    return None


def _quote_price(quote_record: dict[str, Any]) -> tuple[float | None, str | None]:
    quote = quote_record.get("quote") if isinstance(quote_record.get("quote"), dict) else quote_record
    for key in ("adjusted_mark_price", "mark_price", "mark", "midpoint", "price"):
        try:
            value = quote.get(key)
            if value not in (None, ""):
                return float(value), key
        except (TypeError, ValueError, AttributeError):
            return None, key
    try:
        bid = float(quote.get("bid_price", quote.get("bid")))
        ask = float(quote.get("ask_price", quote.get("ask")))
        if bid > 0 and ask > 0:
            return round((bid + ask) / 2, 6), "bid_ask_midpoint"
    except (TypeError, ValueError, AttributeError):
        pass
    return None, None


def get_historical_underlying_close(snapshot: dict[str, Any], symbol: str, target: date, *, as_of: date) -> dict[str, Any]:
    source=str(snapshot.get("source") or "historical_bar_snapshot")
    if not symbol or not target: return _result("INVALID_RECORD",target,source,error="missing symbol or target")
    if not source_capabilities(snapshot)["equity_historical"]: return _result("SOURCE_CAPABILITY_UNSUPPORTED",target,source,instrument_id=symbol,component="underlying",root_cause="equity_historical_disabled")
    if target>as_of: return _result("NOT_YET_MATURE",target,source)
    if not is_trading_day(target): return _result("NO_TRADING_DAY",target,source)
    bars=_bars(snapshot,"equity_bars",symbol)
    if not bars: return _result("NO_ROWS_RETURNED",target,source,instrument_id=symbol,component="underlying",root_cause="no_rows_for_symbol")
    bar=bars.get(target.isoformat())
    if not bar: return _result("TARGET_DATE_NOT_IN_RESPONSE",target,source,instrument_id=symbol,component="underlying",root_cause="target_session_absent")
    try:
        price = float(bar["close"])
    except (TypeError, ValueError, KeyError):
        return _result("PARSE_ERROR",target,source,instrument_id=symbol,component="underlying",root_cause="missing_or_invalid_close")
    return _result("FOUND",target,source,resolved_trading_date=target.isoformat(),price=price,instrument_id=symbol,retrieved_at=str(snapshot.get("as_of")),valuation_method="official_close",retryable=False)


def get_historical_benchmark_close(snapshot: dict[str, Any], symbol: str, target: date, *, as_of: date) -> dict[str, Any]:
    if not source_capabilities(snapshot)["benchmark_historical"]:
        source=str(snapshot.get("source") or "historical_bar_snapshot")
        return _result("SOURCE_CAPABILITY_UNSUPPORTED",target,source,instrument_id=symbol,component="benchmark",root_cause="benchmark_historical_disabled")
    return get_historical_underlying_close(snapshot,symbol,target,as_of=as_of)


def resolve_option_id(snapshot: dict[str, Any], row: dict[str, Any]) -> str | None:
    direct=row.get("option_id") or row.get("instrument_id")
    if direct: return str(direct)
    mapped=snapshot.get("option_id_lookup",{}).get(str(row.get("option_setup_id")))
    if mapped: return str(mapped)
    expiration=str(row.get("expiration") or "")[:10]; strike=row.get("strike"); right=str(row.get("option_type") or "").lower()
    for instrument_id, meta in snapshot.get("option_contracts",{}).items():
        if str(meta.get("underlying") or "").upper()==str(row.get("underlying") or "").upper() and str(meta.get("expiration") or "")[:10]==expiration and str(meta.get("option_type") or meta.get("right") or "").lower()==right:
            try:
                if abs(float(meta.get("strike"))-float(strike))<0.0001: return str(instrument_id)
            except (TypeError,ValueError): pass
    if row.get("underlying") and expiration and strike is not None and right in {"call","put"}:
        return f"contract:{str(row['underlying']).upper()}:{expiration}:{float(strike):g}:{right}"
    return None


def get_historical_option_close(snapshot: dict[str, Any], row: dict[str, Any], target: date, *, as_of: date) -> dict[str, Any]:
    source=str(snapshot.get("source") or "historical_bar_snapshot"); option_id=resolve_option_id(snapshot,row)
    if target>as_of: return _result("NOT_YET_MATURE",target,source,instrument_id=option_id)
    if not option_id: return _result("INVALID_INSTRUMENT_ID",target,source,contract=str(row.get("contract") or ""))
    checkpoint = _checkpoint_quotes(snapshot, option_id, target)
    if checkpoint:
        price, method = _quote_price(checkpoint)
        if price is None:
            return _result("PARSE_ERROR",target,source,instrument_id=option_id,component="option",root_cause="checkpoint_quote_missing_mark")
        quote = checkpoint.get("quote") if isinstance(checkpoint.get("quote"), dict) else checkpoint
        return _result("FOUND",target,source,resolved_trading_date=target.isoformat(),price=price,instrument_id=option_id,retrieved_at=str(quote.get("updated_at") or snapshot.get("as_of")),valuation_method=f"prospective_option_checkpoint_{method}",fallback_used=method == "bid_ask_midpoint",retryable=False,checkpoint=True)
    if not source_capabilities(snapshot)["option_historical"]:
        return _result("OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE",target,source,instrument_id=option_id,component="option",root_cause="no_historical_option_bars_endpoint")
    expiration=parse_date(row.get("expiration")); terminal=expiration_session(expiration) if expiration else None
    lookup_day=terminal if terminal and target>terminal else target
    bars=_bars(snapshot,"option_bars",option_id); bar=bars.get(lookup_day.isoformat()) if bars else None
    if terminal and target>terminal:
        equity=get_historical_underlying_close(snapshot,str(row.get("underlying") or ""),terminal,as_of=as_of)
        if equity["status"]=="FOUND":
            strike=float(row["strike"]); spot=float(equity["price"]); put=str(row.get("option_type") or "").lower()=="put"
            value=max(strike-spot,0) if put else max(spot-strike,0); state="EXPIRED_OTM" if value==0 else "EXPIRED_ITM"
            return _result("FOUND",target,source,resolved_trading_date=terminal.isoformat(),price=round(value,6),instrument_id=option_id,retrieved_at=str(snapshot.get("as_of")),fallback_used=True,terminal_state=state,terminal_value=round(value,6),valuation_method="intrinsic_value",retryable=False)
    if bar and bar.get("close") is not None:
        return _result("FOUND",target,source,resolved_trading_date=lookup_day.isoformat(),price=float(bar["close"]),instrument_id=option_id,retrieved_at=str(snapshot.get("as_of")),valuation_method="historical_close",terminal_state=None,retryable=False)
    if bar and bar.get("bid") is not None and bar.get("ask") is not None:
        price=round((float(bar["bid"])+float(bar["ask"]))/2,6)
        return _result("FOUND",target,source,resolved_trading_date=lookup_day.isoformat(),price=price,instrument_id=option_id,retrieved_at=str(snapshot.get("as_of")),fallback_used=True,valuation_method="historical_midpoint",retryable=False)
    return _result("NO_ROWS_RETURNED" if not bars else "TARGET_DATE_NOT_IN_RESPONSE",target,source,instrument_id=option_id,component="option",root_cause="no_option_bar_for_target")
