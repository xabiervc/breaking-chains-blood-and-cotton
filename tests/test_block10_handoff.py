import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Block10HandoffTests(unittest.TestCase):
    def test_traceability_matrix_exists(self):
        self.assertTrue((ROOT / 'docs' / 'TRACEABILITY_MATRIX.md').is_file())
    def test_handoff_preserves_ci_gate(self):
        text = (ROOT / 'docs' / 'IMPLEMENTATION_HANDOFF.md').read_text(encoding='utf-8')
        self.assertIn('workflow', text)
        self.assertIn('`success`', text)
    def test_final_status_is_honest(self):
        text = (ROOT / 'docs' / 'PREIMPLEMENTATION_FINAL_STATUS.md').read_text(encoding='utf-8')
        self.assertIn('Pendiente de verificación externa', text)
        self.assertIn('0.1.0-preimplementation', text)
if __name__ == '__main__': unittest.main()
