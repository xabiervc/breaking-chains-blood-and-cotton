import json
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Block7InvariantTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_catalog_ids_are_unique(self):
        catalogs = {'missions.json':'missions','evidence.json':'evidence','regions.json':'regions','locations.json':'locations','characters.json':'characters','factions.json':'factions','routes.json':'routes','transport.json':'transport','travel_states.json':'travel_states','persons.json':'persons','resources.json':'resources','rescue_requirements.json':'rescues','mission_operations.json':'operations','rescue_transitions.json':'transitions','audit_events.json':'events','safety_gates.json':'gates'}
        for filename, key in catalogs.items():
            items = self.load(filename)[key]
            ids = [item.get('id') or item.get('faction_id') for item in items]
            self.assertEqual(len(ids), len(set(ids)), filename)
    def test_resource_amounts_are_positive(self):
        data = self.load('resources.json')
        for operation in data['operations']:
            for entry in operation['inputs'] + operation['outputs']:
                self.assertGreater(entry['amount'], 0)
    def test_reputation_bounds_are_valid(self):
        for faction in self.load('reputation_factions.json')['factions']:
            self.assertLessEqual(faction['minimum'], faction['maximum'])
            self.assertGreaterEqual(faction['starting_reputation'], faction['minimum'])
            self.assertLessEqual(faction['starting_reputation'], faction['maximum'])
    def test_travel_state_transitions_are_declared(self):
        states = {item['id']: item for item in self.load('travel_states.json')['travel_states']}
        for state in states.values():
            for target in state.get('allowed_next', []): self.assertIn(target, states)
    def test_sensitive_operations_are_auditable(self):
        events = self.load('audit_events.json')['events']
        for event in events:
            self.assertIn('operation_id', event['required_fields'])
            self.assertEqual(event['idempotency_key'], 'operation_id')
    def test_no_random_fields_in_deterministic_catalogs(self):
        for filename, key in (('travel_states.json','travel_states'),('mission_operations.json','operations'),('rescue_transitions.json','transitions')):
            for item in self.load(filename)[key]: self.assertNotIn('random', item)
    def test_global_validator_remains_clean(self):
        import sys
        sys.path.insert(0, str(ROOT / 'tools'))
        from validate_content import validate
        self.assertEqual(validate(ROOT), [])
if __name__ == '__main__': unittest.main()
