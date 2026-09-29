import json
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class EconomyAndRescueTests(unittest.TestCase):
    def load(self, name):
        return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_resources_are_non_negative_and_unique(self):
        data = self.load('resources.json')['resources']
        ids = [item['id'] for item in data]
        self.assertEqual(len(ids), len(set(ids)))
        for item in data:
            self.assertRegex(item['id'], r'^BC_RESOURCE_[A-Z0-9_]+$')
            self.assertGreaterEqual(item['minimum'], 0)
    def test_operations_have_declared_resource_inputs(self):
        data = self.load('resources.json')
        resources = {item['id'] for item in data['resources']}
        for operation in data['operations']:
            self.assertRegex(operation['id'], r'^BC_OPERATION_[A-Z0-9_]+$')
            for entry in operation['inputs'] + operation['outputs']:
                self.assertIn(entry['resource_id'], resources)
                self.assertGreater(entry['amount'], 0)
    def test_rescue_requirements_are_explicit(self):
        data = self.load('rescue_requirements.json')
        locations = {item['id'] for item in self.load('locations.json')['locations']}
        for rescue in data['rescues']:
            self.assertRegex(rescue['id'], r'^BC_RESCUE_[A-Z0-9_]+$')
            self.assertIn(rescue['status'], data['statuses'])
            self.assertIn(rescue['destination_location_id'], locations)
            self.assertGreater(rescue['required_capacity'], 0)
    def test_reputation_deltas_are_bounded(self):
        data = self.load('reputation_factions.json')
        factions = {item['faction_id'] for item in data['factions']}
        for faction in data['factions']:
            self.assertGreaterEqual(faction['starting_reputation'], faction['minimum'])
            self.assertLessEqual(faction['starting_reputation'], faction['maximum'])
        for delta in data['deltas']:
            self.assertIn(delta['faction_id'], factions)
            self.assertNotEqual(delta['delta'], 0)
    def test_people_are_not_inventory_items(self):
        resources = self.load('resources.json')['resources']
        self.assertFalse(any('PERSON' in item['id'] for item in resources))
if __name__ == '__main__':
    unittest.main()
