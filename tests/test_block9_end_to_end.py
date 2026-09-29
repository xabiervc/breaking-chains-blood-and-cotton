import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Block9EndToEndTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_scenarios_reference_real_operations_and_rescues(self):
        operations = {x['id']: x for x in self.load('mission_operations.json')['operations']}
        rescues = {x['id']: x for x in self.load('rescue_requirements.json')['rescues']}
        for scenario in self.load('scenarios.json')['scenarios']:
            self.assertIn(scenario['operation_id'], operations)
            self.assertIn(scenario['rescue_id'], rescues)
            self.assertEqual(operations[scenario['operation_id']]['rescue_id'], scenario['rescue_id'])
            self.assertTrue(scenario['deterministic'])
    def test_success_scenario_ends_delivered(self):
        scenarios = self.load('scenarios.json')['scenarios']
        item = next(x for x in scenarios if x['result'] == 'accepted')
        self.assertEqual(item['to_status'], 'delivered')
        self.assertIn('BC_TRAVEL_STATE_ARRIVED', item['travel_states'])
    def test_failure_scenario_does_not_deliver(self):
        scenarios = self.load('scenarios.json')['scenarios']
        item = next(x for x in scenarios if x['result'] == 'failed_requirements')
        self.assertEqual(item['to_status'], 'failed_requirements')
        self.assertNotEqual(item['to_status'], 'delivered')
    def test_global_validator_remains_clean(self):
        import sys
        sys.path.insert(0, str(ROOT / 'tools'))
        from validate_content import validate
        self.assertEqual(validate(ROOT), [])
if __name__ == '__main__': unittest.main()
