import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Block4AuditSafetyTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_audit_events_have_idempotency(self):
        data = self.load('audit_events.json')
        for event in data['events']:
            self.assertRegex(event['id'], r'^BC_AUDIT_')
            self.assertEqual(event['idempotency_key'], 'operation_id')
            self.assertIn('operation_id', event['required_fields'])
    def test_safety_gates_have_failure_policy(self):
        data = self.load('safety_gates.json')
        for gate in data['gates']:
            self.assertRegex(gate['id'], r'^BC_GATE_')
            self.assertIn(gate['on_failure'], {'reject', 'failed_requirements'})
            self.assertTrue(gate['checks'])
    def test_no_hidden_randomness_gate_exists(self):
        ids = {gate['id'] for gate in self.load('safety_gates.json')['gates']}
        self.assertIn('BC_GATE_NO_HIDDEN_RANDOMNESS', ids)
    def test_results_are_explicit(self):
        results = set(self.load('audit_events.json')['results'])
        self.assertTrue({'accepted', 'rejected', 'failed_requirements', 'duplicate'} <= results)
if __name__ == '__main__': unittest.main()
