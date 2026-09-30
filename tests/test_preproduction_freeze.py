import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class PreproductionFreezeTests(unittest.TestCase):
    def load(self): return json.loads((ROOT / 'data' / 'preproduction_freeze.json').read_text(encoding='utf-8'))
    def test_baseline_is_frozen_for_prototype(self):
        data=self.load()
        self.assertEqual(data['baseline_status'],'frozen_for_prototype')
        self.assertEqual(data['definition_level'],'A')
        self.assertEqual(data['production_status'],'blocked_pending_external_evidence')
    def test_structural_change_requires_formal_decision(self):
        self.assertEqual(self.load()['change_control'],'formal_decision_required')
    def test_external_validations_are_not_falsely_passed(self):
        self.assertGreaterEqual(len(self.load()['open_validations']),8)
        self.assertNotIn('passed', self.load()['open_validations'])
if __name__ == '__main__': unittest.main()
