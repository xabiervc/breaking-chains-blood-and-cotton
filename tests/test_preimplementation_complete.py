import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class PreimplementationCompleteTests(unittest.TestCase):
    def load(self, path): return json.loads((ROOT / path).read_text(encoding='utf-8'))
    def test_all_required_catalogs_exist(self):
        for path in ('data/missions.json','data/evidence.json','data/regions.json','data/locations.json','data/characters.json','data/factions.json','data/routes.json','data/transport.json','data/travel_states.json','data/persons.json','data/resources.json','data/rescue_requirements.json','data/reputation_factions.json','data/mission_operations.json','data/rescue_transitions.json','data/audit_events.json','data/safety_gates.json'):
            self.assertTrue((ROOT / path).is_file(), path)
    def test_block3_operations_use_block4_audit_contract(self):
        audit = self.load('data/audit_events.json')
        event_types = {event['event_type'] for event in audit['events']}
        self.assertIn('mission_operation', event_types)
        self.assertIn('rescue_transition', event_types)
        operations = self.load('data/mission_operations.json')['operations']
        self.assertTrue(all(item['deterministic'] is True for item in operations))
    def test_safety_gate_contract_is_complete(self):
        gates = self.load('data/safety_gates.json')['gates']
        gate_ids = {gate['id'] for gate in gates}
        self.assertTrue({'BC_GATE_VALIDATE_REFERENCES','BC_GATE_CHECK_RESOURCES','BC_GATE_CHECK_REPUTATION','BC_GATE_CHECK_RESCUE','BC_GATE_NO_HIDDEN_RANDOMNESS'} <= gate_ids)
    def test_people_remain_separate_from_resources(self):
        people = {item['id'] for item in self.load('data/persons.json')['persons']}
        resources = {item['id'] for item in self.load('data/resources.json')['resources']}
        self.assertTrue(people.isdisjoint(resources))
    def test_global_validator_is_clean(self):
        import sys
        sys.path.insert(0, str(ROOT / 'tools'))
        from validate_content import validate
        self.assertEqual(validate(ROOT), [])
if __name__ == '__main__': unittest.main()
