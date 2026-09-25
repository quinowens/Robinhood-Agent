import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from migrate_option_outcome_component_schema import (
    LEGACY_COMPONENT_SCHEMA_VERSION,
    has_complete_component_schema,
    migrate_row,
)


class OptionOutcomeComponentMigrationTests(unittest.TestCase):
    def test_marks_legacy_row_idempotently(self):
        row = {"strategy_version": "2.0.2", "forward_1d_status": "OBSERVED"}
        self.assertTrue(migrate_row(row))
        self.assertTrue(row["legacy_component_schema"])
        self.assertEqual(row["component_schema_version"], LEGACY_COMPONENT_SCHEMA_VERSION)
        self.assertFalse(migrate_row(row))

    def test_current_component_schema_is_not_marked_legacy(self):
        row = {}
        for horizon in (1, 5, 10, 20, 30):
            row[f"forward_{horizon}d_observation"] = {
                "target_observation_date": None,
                "component_resolutions": {},
            }
            for component in ("underlying", "option", "spy", "qqq"):
                row[f"forward_{horizon}d_{component}_status"] = "PENDING"
        self.assertTrue(has_complete_component_schema(row))
        self.assertTrue(migrate_row(row))
        self.assertNotIn("legacy_component_schema", row)
        self.assertIsNone(row["terminal_state"])
        self.assertIsNone(row["terminal_value"])
        self.assertIsNone(row["valuation_method"])
        self.assertFalse(migrate_row(row))


if __name__ == "__main__":
    unittest.main()
