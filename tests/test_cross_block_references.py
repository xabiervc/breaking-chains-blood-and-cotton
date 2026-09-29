import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class CrossBlockReferenceTests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_rescue_people_exist(self):
        people = {x['id'] for x in self.load('persons.json')['persons']}
        for rescue in self.load('rescue_requirements.json')['rescues']: self.assertIn(rescue['person_id'], people)
    def test_rescue_destinations_exist(self):
        locations = {x['id'] for x in self.load('locations.json')['locations']}
        for rescue in self.load('rescue_requirements.json')['rescues']: self.assertIn(rescue['destination_location_id'], locations)
    def test_global_validator_passes(self):
        import sys; sys.path.insert(0, str(ROOT / 'tools'))
        from validate_content import validate
        self.assertEqual(validate(ROOT), [])
if __name__ == '__main__': unittest.main()
