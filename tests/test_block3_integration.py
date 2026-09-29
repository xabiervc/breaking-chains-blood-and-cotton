import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Block3IntegrationTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_mission_operations_are_deterministic(self):
        data = self.load('mission_operations.json')
        for operation in data['operations']:
            self.assertTrue(operation['deterministic'])
            self.assertRegex(operation['mission_id'], r'^BC_MISSION_')
            self.assertRegex(operation['rescue_id'], r'^BC_RESCUE_')
    def test_transition_statuses_are_declared(self):
        data = self.load('rescue_transitions.json')
        for transition in data['transitions']:
            self.assertIn(transition['from_status'], data['statuses'])
            self.assertIn(transition['to_status'], data['statuses'])
    def test_block3_references_exist(self):
        missions = {x['id'] for x in self.load('missions.json')['missions']}
        rescues = {x['id'] for x in self.load('rescue_requirements.json')['rescues']}
        states = {x['id'] for x in self.load('travel_states.json')['travel_states']}
        for operation in self.load('mission_operations.json')['operations']:
            self.assertIn(operation['mission_id'], missions)
            self.assertIn(operation['rescue_id'], rescues)
            self.assertIn(operation['required_travel_state'], states)
            self.assertIn(operation['next_travel_state'], states)
    def test_global_validator_is_importable(self):
        import sys
        sys.path.insert(0, str(ROOT / 'tools'))
        from validate_content import validate
        self.assertIsInstance(validate(ROOT), list)
if __name__ == '__main__': unittest.main()
