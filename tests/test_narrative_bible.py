import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class NarrativeBibleTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_isaiah_is_canonical_protagonist(self):
        item = self.load('narrative_characters.json')['characters'][0]
        self.assertEqual(item['id'], 'BC_NARRATIVE_CHAR_ISAIAH_BELL')
        self.assertEqual(item['role'], 'protagonist')
    def test_timeline_is_strictly_ordered(self):
        events = self.load('narrative_timeline.json')['events']
        sequences = [item['sequence'] for item in events]
        self.assertEqual(sequences, sorted(set(sequences)))
    def test_timeline_references_known_story_ids(self):
        known = set()
        for name, key in (('missions.json','missions'),('evidence.json','evidence'),('persons.json','persons')):
            known |= {item['id'] for item in self.load(name)[key]}
        for event in self.load('narrative_timeline.json')['events']:
            for field in ('requires','reveals','unlocks'):
                for value in event.get(field, []):
                    self.assertIn(value, known)
    def test_relationships_have_valid_factions(self):
        factions = {item['id'] for item in self.load('factions.json')['factions']}
        for relationship in self.load('narrative_relationships.json')['relationships']:
            for field in ('to_faction_id','from_faction_id'):
                if field in relationship: self.assertIn(relationship[field], factions)
if __name__ == '__main__': unittest.main()
