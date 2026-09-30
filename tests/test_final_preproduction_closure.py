import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class FinalPreproductionClosureTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_all_a_criteria_are_defined_but_not_falsely_passed(self):
        data=self.load('level_a_completion_matrix.json')
        self.assertEqual(data['overall_definition_status'],'level_a_defined')
        self.assertEqual(data['overall_evidence_status'],'external_pending')
        self.assertEqual(len(data['criteria']),7)
        for item in data['criteria']: self.assertEqual(item['definition_status'],'defined')
    def test_governance_and_hypotheses_exist(self):
        for name in ('DESIGN_AUTHORITY.md','MUST_FIX_BEFORE_IMPLEMENTATION.md','PROTOTYPE_HYPOTHESES.md','ACCESSIBILITY_TEST_PLAN.md','CONTENT_REPRESENTATION_MATRIX.md'):
            self.assertTrue((ROOT/'docs'/name).is_file())
    def test_no_structural_blocker_claim_is_explicit(self):
        text=(ROOT/'docs'/'MUST_FIX_BEFORE_IMPLEMENTATION.md').read_text(encoding='utf-8')
        self.assertIn('no tiene bloqueos estructurales',text.lower())
        self.assertIn('producción plena',text)
if __name__ == '__main__': unittest.main()
