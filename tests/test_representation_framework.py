import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class RepresentationFrameworkTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_primary_perspective_is_coral(self):
        primary = [x for x in self.load('perspective_framework.json')['perspectives'] if x['primary']]
        self.assertEqual(len(primary), 1)
        self.assertEqual(primary[0]['id'], 'BC_PERSPECTIVE_CORAL_COMMUNITY')
        self.assertTrue(primary[0]['external_savior_prohibited'])
    def test_cotton_has_four_systemic_layers(self):
        layers = {x['layer'] for x in self.load('cotton_economy.json')['systems']}
        self.assertEqual(layers, {'production','trade','debt','logistics'})
        self.assertTrue(all(x['not_a_repetitive_minigame'] for x in self.load('cotton_economy.json')['systems']))
    def test_agency_is_community_facing(self):
        data = self.load('community_agency.json')
        self.assertTrue(data['external_savior_prohibited'])
        self.assertGreaterEqual(len(data['dimensions']), 4)
    def test_warnings_prohibit_spectacle(self):
        text = (ROOT / 'docs' / 'CONTENT_WARNINGS_AND_GUARDRAILS.md').read_text(encoding='utf-8')
        self.assertIn('No usar violencia sexual como mecánica', text)
        self.assertIn('No hacer del sufrimiento un coleccionable', text)
if __name__ == '__main__': unittest.main()
