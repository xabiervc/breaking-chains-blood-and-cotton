import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class NarrativeSteps67Tests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_runtime_bindings_reference_existing_operations_rescues_scenarios(self):
        operations = {x['id'] for x in self.load('mission_operations.json')['operations']}
        rescues = {x['id'] for x in self.load('rescue_requirements.json')['rescues']}
        scenarios = {x['id'] for x in self.load('scenarios.json')['scenarios']}
        for item in self.load('narrative_runtime_bindings.json')['bindings']:
            self.assertIn(item['operation_id'], operations)
            self.assertIn(item['rescue_id'], rescues)
            self.assertIn(item['scenario_id'], scenarios)
            self.assertRegex(item['scene_id'], r'^BC_SCENE_')
    def test_bindings_are_unique(self):
        items = self.load('narrative_runtime_bindings.json')['bindings']
        ids = [x['id'] for x in items]
        self.assertEqual(len(ids), len(set(ids)))
    def test_global_validator_remains_clean(self):
        import sys; sys.path.insert(0, str(ROOT / 'tools'))
        from validate_content import validate
        self.assertEqual(validate(ROOT), [])
if __name__ == '__main__': unittest.main()
