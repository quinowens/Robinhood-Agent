#!/usr/bin/env python3
"""Prospective, isolated contract experiments. No broker or order-writing code."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import date, datetime, timezone, timedelta
from pathlib import Path
from statistics import mean, median

from historical_resolver import US_EASTERN, is_trading_day, trading_day

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "research-lab-1"
HORIZONS = (1, 5, 10, 20, 30)
POLICIES = ([{"name": f"tp{tp}_sl{sl}_time{days}", "tp": tp / 100,
              "sl": -sl / 100, "days": days, "thesis": False}
             for tp in (25, 40, 60) for sl in (20, 30, 40) for days in (5, 10)]
            + [{"name": "technical_exit", "tp": None, "sl": None, "days": 30, "thesis": True}])


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("Timestamps must include timezone")
    return result


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, allow_nan=False).encode()).hexdigest()


def save_once(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if path.exists():
        if json.loads(path.read_text()) != value:
            raise ValueError(f"Immutable artifact conflict: {path}")
        return
    with path.open("x") as handle:
        handle.write(serialized)


def quote(q, at, entry=False):
    bid, ask = q.get("bid"), q.get("ask")
    if not all(number(x) for x in (bid, ask)) or bid < 0 or ask < bid or (entry and bid == 0):
        raise ValueError("Missing, crossed, zero, or non-finite bid/ask")
    qt = timestamp(q["quote_at"])
    if qt > at or (at - qt).total_seconds() > (300 if entry else 1800):
        raise ValueError("Quote is future-dated or stale")
    return (bid + ask) / 2


def diagnostics(c, underlying):
    mid = (c["bid"] + c["ask"]) / 2
    iv, rv = c.get("implied_volatility"), c.get("realized_volatility_20d")
    be = c["strike"] + mid if c["option_type"] == "call" else c["strike"] - mid
    return {"spread_fraction_mid": (c["ask"] - c["bid"]) / mid,
            "premium_fraction_underlying": mid / underlying,
            "breakeven_distance_fraction": (be - underlying) / underlying,
            "iv_to_realized_volatility": iv / rv if number(iv) and number(rv) and rv > 0 else None,
            **{key: c.get(key) for key in ("implied_volatility", "iv_rank", "iv_percentile",
                "realized_volatility_20d", "theta", "vega", "delta")}}


def freeze(payload, now=None):
    """Capture all four arms once, including unavailable arms and the candidate set."""
    now = now or datetime.now(timezone.utc)
    at = timestamp(payload["captured_at"])
    if abs((now - at).total_seconds()) > 300:
        raise ValueError("Freeze must occur prospectively within five minutes of capture")
    local = at.astimezone(US_EASTERN)
    if not is_trading_day(local.date()) or not ("09:30" <= local.strftime("%H:%M") < "16:00"):
        raise ValueError("Freeze requires a regular-session entry snapshot")
    s = payload["setup"]
    if (s.get("setup_quality_status") != "QUALIFIED" or
        not number(s.get("options_setup_score")) or s["options_setup_score"] < 75 or
        s.get("is_canonical") is not True or s.get("superseded_by_record_id") or
        s.get("underlying_eligibility") != "eligible" or
        s.get("directional_thesis") not in ("bullish", "bearish")):
        raise ValueError("Only canonical, eligible, qualified directional setups scoring >=75 enter the lab")
    if abs((at - timestamp(s["timestamp"])).total_seconds()) > 300:
        raise ValueError("Setup and lab must share the signal timestamp")
    if not s.get("signal_group_id") or not s.get("option_setup_id"):
        raise ValueError("Stable setup and signal-group IDs are required")
    spot = payload["underlying_price"]
    if not number(spot) or spot <= 0:
        raise ValueError("Positive underlying price required")
    if abs((at - timestamp(payload["underlying_quote_at"])).total_seconds()) > 300:
        raise ValueError("Underlying quote must be contemporaneous")
    side = "call" if s["directional_thesis"] == "bullish" else "put"
    raw_ids = [c.get("option_id") for c in payload["contracts"]]
    if len(set(raw_ids)) != len(raw_ids):
        raise ValueError("Duplicate candidate IDs would make selection ambiguous")
    candidates, rejected, ids = [], [], set()
    for raw in payload["contracts"]:
        c = dict(raw)
        try:
            cid = c["option_id"]
            if not isinstance(cid, str) or not cid:
                raise ValueError("Empty contract ID")
            if cid in ids:
                raise ValueError("Duplicate contract ID")
            ids.add(cid)
            if c["underlying"] != s["underlying"] or c["option_type"] != side:
                raise ValueError("Wrong underlying or direction")
            c["midpoint"] = quote(c, at, entry=True)
            c["dte"] = (date.fromisoformat(c["expiration"]) - local.date()).days
            if c["dte"] < 30 or not number(c.get("strike")) or c["strike"] <= 0:
                raise ValueError("Invalid strike or expiration")
            if not number(c.get("delta")) or not 0 < abs(c["delta"]) <= 1 or (c["delta"] > 0) != (side == "call"):
                raise ValueError("Missing/invalid signed delta")
            c["diagnostics"] = diagnostics(c, spot)
            candidates.append(c)
        except (ValueError, KeyError, TypeError) as exc:
            rejected.append({"option_id": c.get("option_id"), "reason": str(exc)})
    canonical_id = s.get("option_id") or s.get("instrument_id")
    canonical = next((c for c in candidates if c["option_id"] == canonical_id), None)
    # These are experiment eligibility filters, never production selection rules.
    pool = [c for c in candidates if c["diagnostics"]["spread_fraction_mid"] <= .05
            and number(c.get("open_interest")) and c["open_interest"] >= 100
            and c.get("event_compatible") is True]
    def choose(items, target):
        return min(items, key=lambda c: (abs(abs(c["delta"]) - target),
                   c["diagnostics"]["spread_fraction_mid"], c["option_id"]), default=None)
    b = choose([c for c in pool if canonical and c["expiration"] == canonical["expiration"]
                and .65 <= abs(c["delta"]) <= .75], .70)
    c = choose([c for c in pool if 75 <= c["dte"] <= 100 and .50 <= abs(c["delta"]) <= .60], .55)
    # Transparent exposure-cost proxy; not an estimated return or Sharpe ratio.
    def cost(c):
        theta = c.get("theta")
        iv_ratio = c["diagnostics"]["iv_to_realized_volatility"]
        if not number(theta) or not number(iv_ratio):
            return None
        return (((c["ask"] - c["bid"]) + 10 * max(0, -theta)) / (abs(c["delta"]) * spot)) * max(1, iv_ratio)
    ranked = [c for c in pool if 35 <= c["dte"] <= 100 and .45 <= abs(c["delta"]) <= .75 and cost(c) is not None]
    d = min(ranked, key=lambda c: (cost(c), c["option_id"]), default=None)
    variants = {}
    for label, contract in zip("ABCD", (canonical, b, c, d)):
        variants[label] = {"status": "FROZEN" if contract else "UNAVAILABLE",
                           "reason": None if contract else "NO_ELIGIBLE_CONTEMPORANEOUS_CONTRACT",
                           "contract": contract}
    return {"protocol": PROTOCOL, "lab_id": digest(s["signal_group_id"])[:24],
            "production_strategy_version": s.get("strategy_version"),
            "captured_at": payload["captured_at"], "entry_session": local.date().isoformat(),
            "setup": s, "underlying_price": spot, "variants": variants,
            "exit_policies": POLICIES, "input": payload, "rejected_contracts": rejected,
            "d_proxy": "(spread + 10 * max(0, -theta)) / (abs(delta) * underlying) * max(1, IV/RV20)",
            "a_target_band_match": bool(canonical and .45 <= abs(canonical["delta"]) <= .55 and 35 <= canonical["dte"] <= 65)}


def expected_sessions(lab):
    start = date.fromisoformat(lab["entry_session"])
    return [trading_day(start, i).isoformat() for i in range(1, 31)]


def validate_observation(lab, obs, now=None):
    now = now or datetime.now(timezone.utc)
    at = timestamp(obs["captured_at"])
    local = at.astimezone(US_EASTERN)
    if abs((now - at).total_seconds()) > 1800:
        raise ValueError("Observation must be persisted prospectively within 30 minutes")
    if obs["session"] != local.date().isoformat() or obs["session"] not in expected_sessions(lab):
        raise ValueError("Observation date must match the captured trading session")
    if not "16:00" <= local.strftime("%H:%M") <= "16:30":
        raise ValueError("Capture closing observations between 16:00 and 16:30 Eastern")
    if obs["lab_id"] != lab["lab_id"] or not obs.get("source"):
        raise ValueError("Lab ID and source required")
    if not number(obs.get("underlying_price")) or obs["underlying_price"] <= 0:
        raise ValueError("Positive underlying close required")
    underlying_at = timestamp(obs["underlying_quote_at"]).astimezone(US_EASTERN)
    if underlying_at.date() != local.date() or underlying_at.strftime("%H:%M") < "16:00" or underlying_at > local:
        raise ValueError("Underlying must be the same-session closing observation")
    if obs.get("thesis_valid") is not None and not isinstance(obs["thesis_valid"], bool):
        raise ValueError("Thesis validity must be true, false, or null")
    if obs.get("thesis_valid") is not None and not obs.get("thesis_evidence"):
        raise ValueError("Technical assessment requires evidence against frozen entry thesis")
    required = {v["contract"]["option_id"] for v in lab["variants"].values()
                if v["contract"] and v["contract"]["expiration"] >= obs["session"]}
    if not required.issubset(obs["quotes"]):
        raise ValueError("Capture all active variant quotes together; retain failed raw capture separately")
    for cid, q in obs["quotes"].items():
        quote(q, at)
        if timestamp(q["quote_at"]).astimezone(US_EASTERN).strftime("%H:%M") < "15:55":
            raise ValueError("Expected a closing quote")
    return obs


def due(labs, observations, as_of):
    requests = []
    for lab in labs:
        existing = {o["session"] for o in observations.get(lab["lab_id"], [])}
        sessions = expected_sessions(lab)
        missing = [s for s in sessions if s <= as_of and s not in existing]
        ids = sorted({v["contract"]["option_id"] for v in lab["variants"].values()
                      if v["contract"] and v["contract"]["expiration"] >= as_of})
        if as_of in sessions:
            # Partial captures remain due, but their original snapshot cannot be overwritten.
            today = next((o for o in observations.get(lab["lab_id"], []) if o["session"] == as_of), None)
            requests.append({"lab_id": lab["lab_id"], "option_ids": [i for i in ids if not today or i not in today["quotes"]],
                             "missing_prior_sessions": [s for s in missing if s < as_of]})
        elif missing:
            requests.append({"lab_id": lab["lab_id"], "option_ids": [], "missing_prior_sessions": missing})
    return {"as_of": as_of, "requests": requests,
            "option_ids": sorted({i for r in requests for i in r["option_ids"]})}


def summarize(values):
    return {"n": len(values), "mean_return": mean(values) if values else None,
            "median_return": median(values) if values else None,
            "win_rate": mean(v > 0 for v in values) if values else None}


def evaluate(lab, observations, as_of):
    sessions = expected_sessions(lab)
    obs = {o["session"]: o for o in observations if o["session"] <= as_of}
    result = {}
    for label, arm in lab["variants"].items():
        c = arm["contract"]
        if not c:
            result[label] = {"status": "UNAVAILABLE"}
            continue
        path = {}
        for n, day in enumerate(sessions, 1):
            o = obs.get(day)
            q = o.get("quotes", {}).get(c["option_id"]) if o else None
            expiry = date.fromisoformat(c["expiration"])
            while not is_trading_day(expiry):
                expiry -= timedelta(days=1)
            settlement = obs.get(expiry.isoformat())
            if day >= expiry.isoformat() and not settlement:
                q = None
            if day >= expiry.isoformat() and settlement:
                spot = settlement["underlying_price"]
                payoff = max(0, spot - c["strike"]) if c["option_type"] == "call" else max(0, c["strike"] - spot)
                q = {"bid": payoff, "ask": payoff}
            if q and o:
                mid = (q["bid"] + q["ask"]) / 2
                iv0, iv1 = c.get("implied_volatility"), q.get("implied_volatility")
                path[n] = {"session": day, "return": mid / c["midpoint"] - 1,
                           "executable_return": q["bid"] / c["ask"] - 1,
                           "underlying_return": o["underlying_price"] / lab["underlying_price"] - 1,
                           "iv_change": iv1 - iv0 if number(iv0) and number(iv1) else None,
                           "theta": q.get("theta"), "vega": q.get("vega"),
                           "thesis_valid": o.get("thesis_valid"),
                           "valuation": "EXPIRATION_INTRINSIC" if day >= expiry.isoformat() and settlement else "QUOTE"}
        for point in path.values():
            directional = point["underlying_return"] * (1 if c["option_type"] == "call" else -1)
            point["direction_option_diagnostic"] = (
                "DIRECTION_RIGHT_OPTION_LOSS_IV_CONTRACTION" if directional > 0 and point["return"] < 0 and point["iv_change"] is not None and point["iv_change"] < 0 else
                "DIRECTION_RIGHT_OPTION_LOSS" if directional > 0 and point["return"] < 0 else
                "DIRECTION_RIGHT_OPTION_GAIN" if directional > 0 and point["return"] > 0 else
                "DIRECTION_WRONG_OR_FLAT")
        matured = [i for i, day in enumerate(sessions, 1) if day <= as_of]
        policies = {}
        for policy in lab["exit_policies"]:
            outcome = {"status": "PENDING", "return": None}
            for n in matured:
                p = path.get(n)
                if not p or (policy["thesis"] and p["thesis_valid"] is None):
                    outcome = {"status": "INDETERMINATE_MISSING_PATH", "return": None}
                    break
                r = p["executable_return"]
                reason = ("THESIS" if policy["thesis"] and p["thesis_valid"] is False else
                          "TP" if policy["tp"] is not None and r >= policy["tp"] else
                          "SL" if policy["sl"] is not None and r <= policy["sl"] else
                          "EXPIRATION" if p["valuation"] == "EXPIRATION_INTRINSIC" else
                          "TIME" if n >= policy["days"] else None)
                if reason:
                    outcome = {"status": "EXITED", "return": r, "reason": reason, "session": p["session"]}
                    break
            policies[policy["name"]] = outcome
        for h in HORIZONS:
            if h in path:
                prefix = [p for n, p in path.items() if n <= h]
                for asset in ("option", "underlying"):
                    key = "return" if asset == "option" else "underlying_return"
                    values = [p[key] for p in prefix]
                    path[h][f"sampled_{asset}_mae"] = min([0] + values)
                    path[h][f"sampled_{asset}_mfe"] = max([0] + values)
                path[h]["path_complete"] = len(prefix) == h
        rets = [p["return"] for p in path.values()]
        underlying = [p["underlying_return"] for p in path.values()]
        result[label] = {"status": "TRACKING", "option_id": c["option_id"],
            "horizons": {str(h): path.get(h, {"status": "MISSING" if sessions[h-1] <= as_of else "PENDING"}) for h in HORIZONS},
            "observed_sessions": len(path), "expected_sessions": len(matured),
            "sampled_option_mae": min([0] + rets), "sampled_option_mfe": max([0] + rets),
            "sampled_underlying_mae": min([0] + underlying), "sampled_underlying_mfe": max([0] + underlying),
            "excursions_complete": len(path) == len(matured), "exit_policies": policies}
    return result


def report(labs, observations, as_of):
    rows = [{"lab_id": l["lab_id"], "score": l["setup"]["options_setup_score"],
             "direction": l["setup"]["directional_thesis"],
             "variants": evaluate(l, observations.get(l["lab_id"], []), as_of)} for l in labs]
    comparisons, buckets = {}, {}
    for direction in ("bullish", "bearish"):
        subset = [r for r in rows if r["direction"] == direction]
        for h in HORIZONS:
            def ret(r, arm):
                return r["variants"][arm].get("horizons", {}).get(str(h), {}).get("return")
            for arm in "BCD":
                paired = [ret(r, arm) - ret(r, "A") for r in subset if ret(r, arm) is not None and ret(r, "A") is not None]
                comparisons[f"{direction}_{arm}-A_{h}d"] = summarize(paired)
            for low in range(75, 100, 5):
                group = [r for r in subset if low <= r["score"] <= (100 if low == 95 else low + 4)]
                for arm in "ABCD":
                    values = [ret(r, arm) for r in group if ret(r, arm) is not None]
                    stats = summarize(values)
                    points = [r["variants"][arm].get("horizons", {}).get(str(h), {}) for r in group]
                    complete = [p for p in points if p.get("path_complete")]
                    stats["complete_path_n"] = len(complete)
                    for metric in ("sampled_option_mae", "sampled_option_mfe", "sampled_underlying_mae", "sampled_underlying_mfe"):
                        stats[metric + "_mean"] = mean(p[metric] for p in complete) if complete else None
                    buckets[f"{direction}_{low}-{100 if low == 95 else low+4}_{arm}_{h}d"] = stats
    exits = {}
    for direction in ("bullish", "bearish"):
        for arm in "ABCD":
            for policy in POLICIES:
                results = [r["variants"][arm].get("exit_policies", {}).get(policy["name"], {})
                           for r in rows if r["direction"] == direction]
                exits[f"{direction}_{arm}_{policy['name']}"] = {
                    **summarize([p["return"] for p in results if p.get("status") == "EXITED"]),
                    "indeterminate_n": sum(p.get("status") == "INDETERMINATE_MISSING_PATH" for p in results)}
    return {"protocol": PROTOCOL, "as_of": as_of, "signals": len(rows), "exit_policy_summary": exits, "experiments": rows,
            "paired_return_differences": comparisons, "score_buckets": buckets,
            "limitations": ["Daily sampled excursions, not intraday extremes", "Exits evaluated at observed bid, entry at ask; no threshold-price fills",
                "Missing path prevents reliable exit simulation", "D is a frozen cost proxy, not demonstrated risk-adjusted alpha",
                "Correlated variants are not independent signals; no strategy changes from small samples"]}


def score_bearish(payload, now=None):
    now = now or datetime.now(timezone.utc)
    if abs((now - timestamp(payload["captured_at"])).total_seconds()) > 300:
        raise ValueError("Bearish evidence must be scored prospectively")
    features = ("failed_breakout", "relative_weakness", "trend_deterioration",
                "negative_catalyst_confirmation", "weak_sector_regime_alignment")
    values = []
    for feature in features:
        item = payload["features"][feature]
        score = item.get("score")
        if score is not None:
            if not isinstance(score, int) or isinstance(score, bool) or not 0 <= score <= 4 or not item.get("evidence"):
                raise ValueError("Bearish components require integer 0–4 and cited evidence, or null")
            values.append(score)
    return {"protocol": PROTOCOL, "input": payload, "observed_components": len(values),
            "bearish_research_score": sum(values) * 5 if len(values) == 5 else None,
            "permission": "RESEARCH_ONLY_NOT_A_QUALIFICATION_GATE"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("freeze", "observe", "due", "report", "bearish"))
    parser.add_argument("--input", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT / "data/strategy_research_lab")
    parser.add_argument("--as-of", default=date.today().isoformat())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command in ("freeze", "observe", "bearish") and args.input is None:
        parser.error("--input is required for freeze, observe, and bearish")
    if args.command == "bearish":
        output = score_bearish(json.loads(args.input.read_text()))
        save_once(args.root / "bearish_candidates" / (digest(output["input"]) + ".json"), output)
    elif args.command == "freeze":
        lab = freeze(json.loads(args.input.read_text()))
        save_once(args.root / "experiments" / (lab["lab_id"] + ".json"), lab)
        output = {"lab_id": lab["lab_id"], "variants": {k: v["status"] for k, v in lab["variants"].items()}}
    else:
        labs = [json.loads(p.read_text()) for p in sorted((args.root / "experiments").glob("*.json"))]
        observations = {l["lab_id"]: [json.loads(p.read_text()) for p in sorted((args.root / "observations" / l["lab_id"]).glob("*.json"))] for l in labs}
        if args.command == "observe":
            obs = json.loads(args.input.read_text())
            lab = next(l for l in labs if l["lab_id"] == obs["lab_id"])
            validate_observation(lab, obs)
            save_once(args.root / "observations" / lab["lab_id"] / (obs["session"] + ".json"), obs)
            output = {"saved": True}
        else:
            date.fromisoformat(args.as_of)
            output = (due if args.command == "due" else report)(labs, observations, args.as_of)
    content = json.dumps(output, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
