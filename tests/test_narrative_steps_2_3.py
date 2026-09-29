import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class NarrativeSteps23Tests(unittest.TestCase):
    def load(self, name): return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))
    def test_mission_sequence_is_strict(self):
        missions = self.load('narrative_mission_sequence.json')['missions']
        self.assertEqual([x['sequence'] for x in missions], sorted({x['sequence'] for x in missions}))
        self.assertEqual(missions[0]['unlocks'], ['BC_MISSION_LEDGER_IRONWORK_SIGNAL'])
    def test_evidence_chain_is_continuous(self):
        chain = self.load('narrative_evidence_chain.json')['chain']
        self.assertEqual(chain[0]['next_evidence_id'], chain[1]['evidence_id'])
        self.assertIsNone(chain[-1]['next_evidence_id'])
    def test_missions_and_evidence_are_canonical(self):
        missions = {x['id'] for x in self.load('missions.json')['missions']}
        evidence = {x['id'] for x in self.load('evidence.json')['evidence']}
        for item in self.load('narrative_mission_sequence.json')['missions']:
            self.assertIn(item['mission_id'], missions)
            for value in item['reveals']: self.assertIn(value, evidence)
        for item in self.load('narrative_evidence_chain.json')['chain']: self.assertIn(item['evidence_id'], evidence)
    def test_consequences_have_explicit_triggers(self):
        for item in self.load('narrative_consequences.json')['consequences']:
            self.assertTrue(item['trigger'])
            self.assertIn('effects', item)
    def test_faction_stakes_reference_existing_factions(self):
        factions = {x['id'] for x in self.load('factions.json')['factions']}
        for item in self.load('narrative_faction_stakes.json')['stakes']: self.assertIn(item['faction_id'], factions)
    def test_global_validator_remains_clean(self):
        import sys; sys.path.insert(0, str(ROOT / 'tools'))
        from validate_content import validate
        self.assertEqual(validate(ROOT), [])
if __name__ == '__main__': unittest.main()
