import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class NarrativeSceneTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_scene_choices_and_consequences_are_linked(self):
        scenes = {item['id']: item for item in self.load('narrative_scenes.json')['scenes']}
        choices = self.load('narrative_choices.json')['choices']
        for choice in choices:
            self.assertIn(choice['scene_id'], scenes)
            self.assertIn(choice['id'], scenes[choice['scene_id']]['choice_ids'])
            self.assertTrue(choice['deterministic'])
    def test_scenes_have_existing_missions_and_locations(self):
        missions = {item['id'] for item in self.load('missions.json')['missions']}
        locations = {item['id'] for item in self.load('locations.json')['locations']}
        for scene in self.load('narrative_scenes.json')['scenes']:
            self.assertIn(scene['mission_id'], missions)
            self.assertIn(scene['location_id'], locations)
    def test_scene_sequences_are_ordered(self):
        sequences = [item['sequence'] for item in self.load('narrative_scenes.json')['scenes']]
        self.assertEqual(sequences, sorted(sequences))
if __name__ == '__main__': unittest.main()
