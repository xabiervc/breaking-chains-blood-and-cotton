import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_content import validate


class ContentValidationTests(unittest.TestCase):
    def test_repository_content_is_valid(self):
        self.assertEqual(validate(ROOT), [])

    def test_mission_ids_are_unique(self):
        data = json.loads((ROOT / "data" / "missions.json").read_text(encoding="utf-8"))
        ids = [mission["id"] for mission in data["missions"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_evidence_ids_are_unique(self):
        data = json.loads((ROOT / "data" / "evidence.json").read_text(encoding="utf-8"))
        ids = [item["id"] for item in data["evidence"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_isaiah_chain_is_present(self):
        missions = json.loads((ROOT / "data" / "missions.json").read_text(encoding="utf-8"))["missions"]
        evidence = json.loads((ROOT / "data" / "evidence.json").read_text(encoding="utf-8"))["evidence"]
        mission_ids = {mission["id"] for mission in missions}
        evidence_ids = {item["id"] for item in evidence}
        expected_missions = {
            "BC_MISSION_LEDGER_ASHGROVE_ENTRY",
            "BC_MISSION_LEDGER_MANIFEST_FRAGMENT",
            "BC_MISSION_LEDGER_TRADER_SETTLEMENT",
            "BC_MISSION_LEDGER_VANE_ORDER",
            "BC_MISSION_LEDGER_PRIVATE_ROUTE_NOTE",
            "BC_MISSION_LEDGER_IRONWORK_SIGNAL",
        }
        expected_evidence = {
            "BC_EVIDENCE_ASHGROVE_TRANSFER_ENTRY",
            "BC_EVIDENCE_COASTWISE_MANIFEST_FRAGMENT",
            "BC_EVIDENCE_TRADER_SETTLEMENT_PAGE",
            "BC_EVIDENCE_VANE_CORRECTED_ORDER",
            "BC_EVIDENCE_PRIVATE_ROUTE_NOTE",
            "BC_EVIDENCE_IRONWORK_SIGNATURE",
        }
        self.assertTrue(expected_missions <= mission_ids)
        self.assertTrue(expected_evidence <= evidence_ids)


if __name__ == "__main__":
    unittest.main()
