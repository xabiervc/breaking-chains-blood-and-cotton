import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class QualityBarTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_accessibility_options_are_required_and_unique(self):
        options = self.load('accessibility_options.json')['options']
        ids = [item['id'] for item in options]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(item['required'] is True for item in options))
    def test_quality_bar_names_all_dimensions(self):
        text = (ROOT / 'docs' / 'QUALITY_BAR.md').read_text(encoding='utf-8').lower()
        for term in ('diseño','jugabilidad','narrativa','accesibilidad','calidad técnica'):
            self.assertIn(term, text)
    def test_design_pillars_protect_agency(self):
        text = (ROOT / 'docs' / 'DESIGN_PILLARS.md').read_text(encoding='utf-8')
        self.assertIn('La agencia sobrevive al fracaso', text)
        self.assertIn('Las personas no son recursos', text)
if __name__ == '__main__': unittest.main()
