import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class TravelStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data" / "travel_states.json").read_text(encoding="utf-8"))
        cls.states = {item["id"]: item for item in cls.data["travel_states"]}
    def test_expected_states_exist(self):
        expected = {"BC_TRAVEL_STATE_AVAILABLE", "BC_TRAVEL_STATE_IN_TRANSIT", "BC_TRAVEL_STATE_DELAYED", "BC_TRAVEL_STATE_ARRIVED", "BC_TRAVEL_STATE_BLOCKED", "BC_TRAVEL_STATE_FAILED_REQUIREMENTS"}
        self.assertTrue(expected <= self.states.keys())
    def test_transitions_reference_existing_states(self):
        for state in self.states.values():
            for target in state["allowed_next"]:
                self.assertIn(target, self.states)
    def test_arrived_is_terminal(self):
        self.assertTrue(self.states["BC_TRAVEL_STATE_ARRIVED"]["terminal"])
    def test_no_random_resolution_field(self):
        for state in self.states.values():
            self.assertNotIn("random", state)
    def test_global_validator_includes_travel_states(self):
        import sys
        sys.path.insert(0, str(ROOT / "tools"))
        from validate_content import validate
        self.assertEqual(validate(ROOT), [])
if __name__ == "__main__":
    unittest.main()
