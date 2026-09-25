import copy
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from historical_resolver import get_historical_option_close, is_trading_day, signal_trading_date, trading_day
from update_option_outcomes import due_option_checkpoints, merge_snapshots, update_row


def bar(day, close, high=None, low=None):
    return {"date": day, "close": close, "high": high if high is not None else close, "low": low if low is not None else close}


class HistoricalOutcomeTests(unittest.TestCase):
    def snapshot(self):
        return {"as_of":"2026-07-10T21:00:00Z","source":"fixture","option_id_lookup":{"setup":"opt"},"equity_bars":{"ABC":[bar("2026-07-02",100),bar("2026-07-06",102),bar("2026-07-07",104),bar("2026-07-08",103),bar("2026-07-09",105),bar("2026-07-10",106)],"SPY":[bar("2026-07-02",200),bar("2026-07-06",202),bar("2026-07-07",204),bar("2026-07-08",203),bar("2026-07-09",205),bar("2026-07-10",206)],"QQQ":[bar("2026-07-02",300),bar("2026-07-06",303),bar("2026-07-07",306),bar("2026-07-08",304),bar("2026-07-09",307),bar("2026-07-10",309)]},"option_bars":{"opt":[bar("2026-07-02",2),bar("2026-07-06",2.5),bar("2026-07-07",3),bar("2026-07-08",2.8),bar("2026-07-09",3.2),bar("2026-07-10",3.5)]}}

    def row(self):
        return {"outcome_record_id":"out","option_setup_id":"setup","underlying":"ABC","signal_date":"2026-07-02","expiration":"2026-08-21","strike":105,"option_type":"call","entry_option_mid":2,"entry_contract_premium_dollars":200,"underlying_price_at_entry":100,"is_canonical":True}

    def test_weekend_and_holiday_crossing(self):
        self.assertFalse(is_trading_day(date(2026,7,3)))
        self.assertEqual(trading_day(date(2026,7,2),1),date(2026,7,6))
        self.assertEqual(trading_day(date(2026,7,2),5),date(2026,7,10))

    def test_normal_partial_and_units(self):
        row=self.row(); changed,issues=update_row(row,self.snapshot(),[])
        self.assertTrue(changed); self.assertEqual(row["forward_1d_status"],"OBSERVED")
        self.assertEqual(row["option_forward_1d_return"],0.25)  # 2.50 / 2.00, never / $200
        self.assertEqual(row["underlying_forward_1d_return"],0.02)
        self.assertFalse(any(i["horizon"]=="1D" for i in issues))

    def test_missing_option_does_not_block_equity(self):
        snapshot=self.snapshot(); snapshot["option_bars"]={}; snapshot["capabilities"]={"option_historical":False}
        row=self.row(); update_row(row,snapshot,[])
        self.assertEqual(row["underlying_forward_1d_return"],0.02)
        self.assertIsNone(row.get("option_forward_1d_return"))
        self.assertEqual(row["forward_1d_underlying_status"],"OBSERVED")
        self.assertEqual(row["forward_1d_option_status"],"OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE")
        self.assertEqual(row["forward_1d_status"],"PERMANENTLY_UNAVAILABLE")

    def test_temporary_history_failure_and_benchmark_failure(self):
        snapshot=self.snapshot(); snapshot["option_bars"]["opt"]=[]; snapshot["equity_bars"]["SPY"]=[]
        row=self.row(); update_row(row,snapshot,[])
        self.assertEqual(row["forward_1d_spy_status"],"NO_ROWS_RETURNED")
        self.assertEqual(row["underlying_forward_1d_return"],0.02)

    def test_expiration_terminal_intrinsic_value(self):
        snapshot=self.snapshot(); snapshot["as_of"]="2026-07-10"; row=self.row(); row["expiration"]="2026-07-06"; row["strike"]=100
        result=get_historical_option_close(snapshot,row,date(2026,7,10),as_of=date(2026,7,10))
        self.assertEqual(result["status"],"FOUND"); self.assertEqual(result["terminal_state"],"EXPIRED_ITM")
        self.assertEqual(result["terminal_value"],2)

    def test_midpoint_fallback(self):
        snapshot=self.snapshot(); snapshot["option_bars"]["opt"]=[{"date":"2026-07-06","bid":2,"ask":3}]
        result=get_historical_option_close(snapshot,self.row(),date(2026,7,6),as_of=date(2026,7,10))
        self.assertEqual(result["price"],2.5); self.assertTrue(result["fallback_used"])

    def test_finalized_and_idempotent(self):
        row=self.row(); snapshot=self.snapshot(); update_row(row,snapshot,[]); frozen=copy.deepcopy(row)
        changed,_=update_row(row,snapshot,[])
        self.assertFalse(changed); self.assertEqual(row,frozen)

    def test_non_trading_signal_uses_next_session(self):
        self.assertEqual(trading_day(date(2026,7,4),1),date(2026,7,6))

    def test_pre_close_signal_uses_same_session(self):
        self.assertEqual(signal_trading_date(date(2026,9,1),"2026-09-01T19:59:59Z"),date(2026,9,1))
        row=self.row(); row["signal_date"]="2026-07-02"; row["entry_snapshot_at"]="2026-07-02T19:59:00Z"
        update_row(row,self.snapshot(),[])
        self.assertEqual(row["forward_1d_observation"]["signal_trading_session"],"2026-07-02")
        self.assertEqual(row["forward_1d_observation"]["target_observation_date"],"2026-07-06")

    def test_after_close_signal_rolls_to_next_session(self):
        self.assertEqual(signal_trading_date(date(2026,9,1),"2026-09-01T20:01:00Z"),date(2026,9,2))
        row=self.row(); row["entry_snapshot_at"]="2026-07-02T20:01:00Z"
        update_row(row,self.snapshot(),[])
        self.assertEqual(row["forward_1d_observation"]["signal_trading_session"],"2026-07-06")
        self.assertEqual(row["forward_1d_observation"]["target_observation_date"],"2026-07-07")

    def test_holiday_signal_rolls_to_next_session(self):
        self.assertEqual(signal_trading_date(date(2026,7,3),"2026-07-03T15:00:00Z"),date(2026,7,6))

    def test_option_history_unsupported_by_source(self):
        snapshot=self.snapshot(); snapshot["capabilities"]={"option_historical":False}
        result=get_historical_option_close(snapshot,self.row(),date(2026,7,6),as_of=date(2026,7,10))
        self.assertEqual(result["status"],"OPTION_HISTORY_NOT_SUPPORTED_BY_SOURCE")
        self.assertFalse(result["retryable"])

    def test_prospective_option_checkpoint_records_return(self):
        snapshot=self.snapshot()
        snapshot["capabilities"]={"option_historical":False}
        snapshot["checkpoint_date"]="2026-07-06"
        snapshot["source"]="robinhood_option_quote_checkpoint"
        snapshot["option_quotes"]={"opt":{"mark_price":"2.75","updated_at":"2026-07-06T19:59:59Z"}}
        row=self.row(); update_row(row,snapshot,[])
        self.assertEqual(row["forward_1d_status"],"OBSERVED")
        self.assertEqual(row["forward_1d_option_status"],"OBSERVED")
        self.assertEqual(row["option_forward_1d_return"],0.375)
        self.assertEqual(row["forward_1d_observation"]["component_resolutions"]["option"]["valuation_method"],"prospective_option_checkpoint_mark_price")

    def test_raw_robinhood_quote_snapshot_is_merged_as_checkpoint(self):
        merged=merge_snapshots([self.snapshot(),{"as_of":"2026-07-06T20:00:00Z","checkpoint_date":"2026-07-06","source":"robinhood_option_quote_checkpoint","capabilities":{"option_historical":False},"data":{"results":[{"quote":{"instrument_id":"opt","adjusted_mark_price":"2.8","updated_at":"2026-07-06T19:59:59Z"},"close":{"price":"2.7"}}]}}])
        row=self.row(); update_row(row,merged,[])
        self.assertEqual(row["forward_1d_option_status"],"OBSERVED")
        self.assertEqual(row["option_forward_1d_return"],0.4)

    def test_due_option_checkpoint_export(self):
        row=self.row()
        due=due_option_checkpoints([],date(2026,7,6))
        self.assertEqual(due,[])
        import tempfile, json
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"outcomes.jsonl"
            path.write_text(json.dumps(row)+"\n",encoding="utf-8")
            due=due_option_checkpoints([path],date(2026,7,6))
        self.assertEqual(due[0]["option_id"],"contract:ABC:2026-08-21:105:call")
        self.assertEqual(due[0]["horizon"],"1D")

    def test_expiration_before_horizon_uses_terminal_intrinsic(self):
        snapshot=self.snapshot(); row=self.row(); row["expiration"]="2026-07-06"; row["strike"]=110
        result=get_historical_option_close(snapshot,row,date(2026,7,10),as_of=date(2026,7,10))
        self.assertEqual(result["status"],"FOUND")
        self.assertEqual(result["terminal_state"],"EXPIRED_OTM")
        self.assertEqual(result["terminal_value"],0)


if __name__ == "__main__": unittest.main()
