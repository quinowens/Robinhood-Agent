import copy
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import strategy_research_lab as lab

AT = '2026-10-05T19:59:00Z'
NOW = datetime.fromisoformat(AT.replace('Z', '+00:00'))


def fixture():
    base = dict(underlying='XYZ', option_type='call', strike=100, bid=9.9, ask=10.1,
                expiration='2026-11-20', delta=.5, quote_at=AT, open_interest=500,
                theta=-.1, implied_volatility=.4, realized_volatility_20d=.3, event_compatible=True)
    contracts = [dict(base, option_id='a'), dict(base, option_id='b', delta=.7),
                 dict(base, option_id='c', expiration='2027-01-08', delta=.55)]
    return dict(captured_at=AT, underlying_price=100, underlying_quote_at=AT,
                setup=dict(strategy_version='2.0.2', option_setup_id='setup1', signal_group_id='signal1',
                           option_id='a', underlying='XYZ', directional_thesis='bullish',
                           setup_quality_status='QUALIFIED', options_setup_score=82,
                           is_canonical=True, underlying_eligibility='eligible', timestamp=AT), contracts=contracts)


def observation(frozen, n, bid=11, thesis=True):
    day = lab.expected_sessions(frozen)[n-1]
    at = day + 'T20:01:00Z'
    return dict(lab_id=frozen['lab_id'], session=day, captured_at=at, source='test_fixture',
                underlying_price=101, underlying_quote_at=at, thesis_valid=thesis, thesis_evidence='fixture condition',
                quotes={i: dict(bid=bid, ask=bid+.2, quote_at=at, implied_volatility=.35)
                        for i in ('a', 'b', 'c')})


class ResearchLabTests(unittest.TestCase):
    def test_expiration_and_zero_bid(self):
        p = fixture()
        for c in p['contracts']:
            c['expiration'] = '2026-11-06'
        f = lab.freeze(p, NOW)
        observations = [observation(f, i, 10) for i in range(1, 31)]
        result = lab.evaluate(f, observations, observations[-1]['session'])['A']
        self.assertEqual(result['horizons']['30']['valuation'], 'EXPIRATION_INTRINSIC')
        self.assertAlmostEqual(result['horizons']['30']['return'], -.9)
        o = observation(f, 1, 0)
        lab.validate_observation(f, o, lab.timestamp(o['captured_at']))

    def test_bearish_missing_evidence_and_missing_components(self):
        p = {'captured_at': AT, 'features': {k: {'score': 3, 'evidence': 'dated source'} for k in
             ('failed_breakout', 'relative_weakness', 'trend_deterioration', 'negative_catalyst_confirmation', 'weak_sector_regime_alignment')}}
        self.assertEqual(lab.score_bearish(p, NOW)['bearish_research_score'], 75)
        p['features']['failed_breakout']['score'] = None
        self.assertIsNone(lab.score_bearish(p, NOW)['bearish_research_score'])

    def test_missing_iv_disables_proxy_and_duplicates_fail(self):
        p = fixture()
        for c in p['contracts']:
            c['realized_volatility_20d'] = None
        self.assertEqual(lab.freeze(p, NOW)['variants']['D']['status'], 'UNAVAILABLE')
        p['contracts'].append(p['contracts'][0])
        with self.assertRaises(ValueError):
            lab.freeze(p, NOW)

    def test_partial_capture_rejected(self):
        f = lab.freeze(fixture(), NOW)
        o = observation(f, 1)
        del o['quotes']['b']
        with self.assertRaises(ValueError):
            lab.validate_observation(f, o, lab.timestamp(o['captured_at']))

    def test_selection_and_baseline(self):
        p = fixture()
        p['contracts'][0]['delta'] = .64
        f = lab.freeze(p, NOW)
        self.assertEqual([f['variants'][a]['contract']['option_id'] for a in 'ABC'], ['a', 'b', 'c'])
        self.assertFalse(f['a_target_band_match'])
        self.assertEqual(f['variants']['D']['contract']['option_id'], 'b')
        self.assertEqual(f['input'], p)

    def test_missing_arm_and_rejected_quote(self):
        p = fixture()
        p['contracts'][1]['quote_at'] = '2026-10-05T18:00:00Z'
        f = lab.freeze(p, NOW)
        self.assertEqual(f['variants']['B']['status'], 'UNAVAILABLE')
        self.assertEqual(len(f['rejected_contracts']), 1)

    def test_reject_watch_low_score_retroactive(self):
        for key, value in [('setup_quality_status', 'WATCH'), ('options_setup_score', 74), ('is_canonical', False)]:
            p = fixture()
            p['setup'][key] = value
            with self.assertRaises(ValueError):
                lab.freeze(p, NOW)
        with self.assertRaises(ValueError):
            lab.freeze(fixture(), datetime(2026, 10, 6, tzinfo=timezone.utc))

    def test_puts_signed_delta(self):
        p = fixture()
        p['setup']['directional_thesis'] = 'bearish'
        for c in p['contracts']:
            c['option_type'] = 'put'
            c['delta'] *= -1
        f = lab.freeze(p, NOW)
        self.assertEqual(f['variants']['B']['contract']['option_id'], 'b')

    def test_freeze_immutable_and_idempotent(self):
        f = lab.freeze(fixture(), NOW)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'lab.json'
            lab.save_once(path, f)
            lab.save_once(path, f)
            changed = copy.deepcopy(f)
            changed['variants']['A']['contract']['bid'] = 1
            with self.assertRaises(ValueError):
                lab.save_once(path, changed)
            self.assertEqual(json.loads(path.read_text()), f)

    def test_capture_validation(self):
        f = lab.freeze(fixture(), NOW)
        o = observation(f, 1)
        at = lab.timestamp(o['captured_at'])
        lab.validate_observation(f, o, at)
        o['session'] = '2026-10-07'
        with self.assertRaises(ValueError):
            lab.validate_observation(f, o, at)

    def test_exit_realized_bid_and_missing_path(self):
        f = lab.freeze(fixture(), NOW)
        o = observation(f, 1, 14)
        r = lab.evaluate(f, [o], o['session'])['A']
        policy = r['exit_policies']['tp25_sl20_time5']
        self.assertEqual(policy['reason'], 'TP')
        self.assertAlmostEqual(policy['return'], 14/10.1-1)
        late = observation(f, 5, 14)
        r = lab.evaluate(f, [late], late['session'])['A']
        self.assertEqual(r['exit_policies']['tp25_sl20_time5']['status'], 'INDETERMINATE_MISSING_PATH')
        self.assertFalse(r['excursions_complete'])

    def test_technical_exit_and_time_stop(self):
        f = lab.freeze(fixture(), NOW)
        observations = [observation(f, i, 10, i != 3) for i in range(1, 6)]
        r = lab.evaluate(f, observations, observations[-1]['session'])['A']
        self.assertEqual(r['exit_policies']['technical_exit']['session'], observations[2]['session'])
        self.assertEqual(r['exit_policies']['tp60_sl40_time5']['reason'], 'TIME')

    def test_daily_due_includes_non_horizon_and_pairing(self):
        f = lab.freeze(fixture(), NOW)
        o = observation(f, 2)
        self.assertEqual(lab.due([f], {}, o['session'])['option_ids'], ['a', 'b', 'c'])
        o = observation(f, 1)
        report = lab.report([f], {f['lab_id']: [o]}, o['session'])
        self.assertEqual(report['signals'], 1)
        self.assertEqual(report['paired_return_differences']['bullish_B-A_1d']['n'], 1)
        self.assertEqual(report['paired_return_differences']['bearish_B-A_1d']['n'], 0)
        self.assertEqual(report['score_buckets']['bullish_80-84_A_1d']['n'], 1)


if __name__ == '__main__':
    unittest.main()
