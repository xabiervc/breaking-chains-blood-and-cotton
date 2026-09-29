import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class AuditFixTests(unittest.TestCase):
    def test_environment_file_exists(self):
        self.assertTrue((ROOT / 'environment.yml').is_file())
    def test_global_validator_covers_new_catalogs(self):
        text = (ROOT / 'tools' / 'validate_content.py').read_text(encoding='utf-8')
        for name in ('mission_operations','rescue_transitions','audit_events','safety_gates','scenarios'):
            self.assertIn(name, text)
    def test_schema_validator_uses_conformance_validation(self):
        text = (ROOT / 'schemas' / 'validate_schemas.py').read_text(encoding='utf-8')
        self.assertIn('Draft202012Validator', text)
if __name__ == '__main__': unittest.main()
