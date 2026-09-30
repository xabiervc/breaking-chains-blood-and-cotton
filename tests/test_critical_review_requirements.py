import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class CriticalReviewRequirementsTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_first_hour_and_duration_are_explicit(self):
        text = (ROOT / 'docs' / 'GAMEPLAY_PILLARS_AND_FIRST_HOUR.md').read_text(encoding='utf-8')
        for phrase in ('Primeros cinco minutos','Primera hora','Decisión diferencial','Duración objetivo'):
            self.assertIn(phrase, text)
    def test_campaign_and_states_are_explicit(self):
        text = (ROOT / 'docs' / 'CAMPAIGN_ARC_AND_NARRATIVE_STATES.md').read_text(encoding='utf-8')
        for phrase in ('Capítulo 1','Capítulo 4','unaware','recovered','Reglas de canon'):
            self.assertIn(phrase, text)
    def test_accessibility_acceptance_has_measurable_targets(self):
        criteria = self.load('accessibility_acceptance.json')['criteria']
        self.assertTrue(any(item['metric'] == 'normal_text_contrast_ratio' and item['target_min'] == 4.5 for item in criteria))
        self.assertTrue(any(item['metric'] == 'critical_text_scale_percent' and item['target_min'] == 200 for item in criteria))
    def test_platform_budgets_and_privacy_are_declared(self):
        self.assertTrue(self.load('platform_matrix.json')['platforms'])
        self.assertTrue(self.load('technical_budgets.json')['budgets'])
        telemetry = self.load('privacy_telemetry.json')
        self.assertTrue(telemetry['opt_in_required'])
        self.assertFalse(telemetry['personal_data_collected'])
    def test_vertical_slice_gate_is_not_only_documentary(self):
        text = (ROOT / 'docs' / 'VERTICAL_SLICE_GATES.md').read_text(encoding='utf-8')
        self.assertIn('requiere evidencia y responsable', text)
if __name__ == '__main__': unittest.main()
