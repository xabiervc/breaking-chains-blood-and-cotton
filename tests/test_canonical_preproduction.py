import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class CanonicalPreproductionTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_canonical_source_exists(self):
        text=(ROOT/'docs'/'CANONICAL_PREPRODUCTION_SPEC.md').read_text(encoding='utf-8')
        self.assertIn('fuente única de verdad', text)
    def test_scope_matrix_has_operational_targets(self):
        text=(ROOT/'docs'/'CONTENT_SCOPE_MATRIX.md').read_text(encoding='utf-8')
        for phrase in ('Escenas jugables','Localizaciones','Diálogos','Estados narrativos','Ramas principales'):
            self.assertIn(phrase,text)
    def test_decisions_have_variable_scene_and_result(self):
        text=(ROOT/'docs'/'DECISION_TRACEABILITY_MATRIX.md').read_text(encoding='utf-8')
        for phrase in ('Variable','Escena','Resultado inmediato','Consecuencia persistente'):
            self.assertIn(phrase,text)
    def test_status_separates_external_evidence(self):
        statuses={item['id']:item['items'] for item in self.load('preproduction_status.json')['statuses']}
        self.assertIn('ci_success',statuses['BC_STATUS_EXTERNAL_PENDING'])
        self.assertIn('full_production_before_external_review',statuses['BC_STATUS_BLOCKED'])
if __name__ == '__main__': unittest.main()
