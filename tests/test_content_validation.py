import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_content import validate
class ContentValidationTests(unittest.TestCase):
    def test_all_catalogs_and_references_are_valid(self):
        self.assertEqual(validate(ROOT), [])
    def test_world_catalog_counts(self):
        expected = {"regions": 5, "locations": 6, "characters": 8, "factions": 8}
        for name, count in expected.items():
            data = json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))
            self.assertEqual(len(data[name]), count)
    def test_isaiah_chain_is_present(self):
        missions = json.loads((ROOT / "data" / "missions.json").read_text(encoding="utf-8"))["missions"]
        evidence = json.loads((ROOT / "data" / "evidence.json").read_text(encoding="utf-8"))["evidence"]
        mission_ids = {item["id"] for item in missions}
        evidence_ids = {item["id"] for item in evidence}
        self.assertTrue({"BC_MISSION_LEDGER_ASHGROVE_ENTRY", "BC_MISSION_LEDGER_IRONWORK_SIGNAL"} <= mission_ids)
        self.assertTrue({"BC_EVIDENCE_ASHGROVE_TRANSFER_ENTRY", "BC_EVIDENCE_IRONWORK_SIGNATURE"} <= evidence_ids)
if __name__ == "__main__":
    unittest.main()
