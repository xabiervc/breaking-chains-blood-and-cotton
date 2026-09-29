import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class Block8CIHardeningTests(unittest.TestCase):
    def test_schema_validator_exists(self):
        self.assertTrue((ROOT / 'schemas' / 'validate_schemas.py').is_file())
    def test_all_schema_pairs_are_declared(self):
        content = (ROOT / 'schemas' / 'validate_schemas.py').read_text(encoding='utf-8')
        for name in ('resource.schema.json','rescue_requirement.schema.json','reputation.schema.json','mission_operation.schema.json','rescue_transition.schema.json','audit_event.schema.json','safety_gate.schema.json'):
            self.assertIn(name, content)
    def test_workflow_runs_global_and_schema_validation(self):
        content = (ROOT / '.github' / 'workflows' / 'python-package-conda.yml').read_text(encoding='utf-8')
        self.assertIn('python tools/validate_content.py', content)
        self.assertIn('python schemas/validate_schemas.py', content)
        self.assertIn('python -m unittest discover -s tests -v', content)
    def test_release_gate_mentions_schema_validation(self):
        content = (ROOT / 'docs' / 'RELEASE_GATES.md').read_text(encoding='utf-8')
        self.assertIn('esquemas', content.lower())
if __name__ == '__main__': unittest.main()
