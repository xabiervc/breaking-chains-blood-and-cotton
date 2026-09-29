import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Block6GovernanceTests(unittest.TestCase):
    def test_version_is_preimplementation(self):
        self.assertEqual((ROOT / 'VERSION').read_text(encoding='utf-8').strip(), '0.1.0-preimplementation')
    def test_required_governance_documents_exist(self):
        for name in ('OPERATIONS_RUNBOOK.md','DATA_CONTRACTS.md','RELEASE_GATES.md'):
            self.assertTrue((ROOT / 'docs' / name).is_file())
    def test_release_gates_require_ci_success(self):
        text = (ROOT / 'docs' / 'RELEASE_GATES.md').read_text(encoding='utf-8')
        self.assertIn('GitHub Actions informa `success`', text)
        self.assertIn('No hay referencias huérfanas', text)
if __name__ == '__main__': unittest.main()
