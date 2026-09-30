import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class LevelAReadinessTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_only_definition_is_marked_defined(self):
        gates = self.load('level_a_gates.json')['gates']
        definition = next(item for item in gates if item['id'] == 'BC_LEVEL_A_DEFINITION')
        self.assertEqual(definition['status'], 'defined')
        self.assertTrue(all(item['status'] == 'external_pending' for item in gates if item['id'] != definition['id']))
    def test_every_gate_requires_evidence(self):
        for gate in self.load('level_a_gates.json')['gates']:
            self.assertTrue(gate['required'])
            self.assertTrue(gate['evidence'])
    def test_canonical_register_is_explicit(self):
        text = (ROOT / 'docs' / 'DOCUMENT_STATUS_REGISTER.md').read_text(encoding='utf-8')
        self.assertIn('Authoritative', text)
        self.assertIn('Subordinate', text)
        self.assertIn('Archived or historical', text)
    def test_no_false_production_claim(self):
        text = (ROOT / 'docs' / 'LEVEL_A_PREPRODUCTION_STANDARD.md').read_text(encoding='utf-8')
        self.assertIn('No significa que exista un juego terminado', text)
        self.assertIn('Evidencia obligatoria antes de producción plena', text)
if __name__ == '__main__': unittest.main()
