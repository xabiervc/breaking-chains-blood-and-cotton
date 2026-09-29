#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {"mission": re.compile(r"^BC_MISSION_[A-Z0-9_]+$"), "evidence": re.compile(r"^BC_EVIDENCE_[A-Z0-9_]+$"), "character": re.compile(r"^BC_CHAR_[A-Z0-9_]+$"), "faction": re.compile(r"^BC_FACTION_[A-Z0-9_]+$"), "region": re.compile(r"^BC_REGION_[A-Z0-9_]+$"), "location": re.compile(r"^BC_LOCATION_[A-Z0-9_]+$"), "route": re.compile(r"^BC_ROUTE_[A-Z0-9_]+$"), "transport": re.compile(r"^BC_TRANSPORT_[A-Z0-9_]+$"), "travel_state": re.compile(r"^BC_TRAVEL_STATE_[A-Z0-9_]+$"), "resource": re.compile(r"^BC_RESOURCE_[A-Z0-9_]+$"), "operation": re.compile(r"^BC_OPERATION_[A-Z0-9_]+$"), "rescue": re.compile(r"^BC_RESCUE_[A-Z0-9_]+$"), "person": re.compile(r"^BC_PERSON_[A-Z0-9_]+$"), "audit": re.compile(r"^BC_AUDIT_[A-Z0-9_]+$"), "gate": re.compile(r"^BC_GATE_[A-Z0-9_]+$"), "scenario": re.compile(r"^BC_SCENARIO_[A-Z0-9_]+$")}
def load(path: Path) -> Any:
    with path.open(encoding='utf-8') as handle: return json.load(handle)
def validate(root: Path = ROOT) -> list[str]:
    errors=[]
    required=('missions','evidence','regions','locations','characters','factions','routes','transport','travel_states','resources','rescue_requirements','reputation_factions','persons','mission_operations','rescue_transitions','audit_events','safety_gates','scenarios')
    data={}
    for name in required:
        path=root/'data'/f'{name}.json'
        if not path.is_file(): errors.append(f'missing catalog: {name}'); continue
        try: data[name]=load(path)
        except (OSError,json.JSONDecodeError) as exc: errors.append(f'invalid catalog {name}: {exc}')
    if errors: return errors
    key={'rescue_requirements':'rescues','reputation_factions':'factions','mission_operations':'operations','rescue_transitions':'transitions','audit_events':'events','safety_gates':'gates' }
    ids={}
    for name,payload in data.items():
        items=payload.get(key.get(name,name),[])
        for item in items:
            value=item.get('id') or item.get('faction_id')
            if not isinstance(value,str): errors.append(f'missing id in {name}')
            elif value in ids: errors.append(f'duplicate id: {value}')
            else: ids[value]=name
    def values(name, field=None):
        return {item.get(field or 'id') for item in data[name][key.get(name,name)]}
    known={name:values(name) for name in data}
    for operation in data['mission_operations']['operations']:
        for field, catalog in (('mission_id','missions'),('rescue_id','rescue_requirements'),('required_travel_state','travel_states'),('next_travel_state','travel_states')):
            if operation.get(field) not in known[catalog]: errors.append(f'unknown {field}: {operation.get(field)}')
        if operation.get('deterministic') is not True: errors.append(f'non-deterministic mission operation: {operation.get("id")}')
        for item in operation.get('resource_inputs',[]):
            if item.get('resource_id') not in known['resources']: errors.append(f'unknown operation resource: {item.get("resource_id")}')
    for rescue in data['rescue_requirements']['rescues']:
        if rescue.get('person_id') not in known['persons']: errors.append(f'unknown rescue person: {rescue.get("person_id")}')
        if rescue.get('destination_location_id') not in known['locations']: errors.append(f'unknown rescue destination: {rescue.get("destination_location_id")}')
        faction=rescue.get('minimum_reputation',{}).get('faction_id')
        if faction not in known['factions']: errors.append(f'unknown rescue faction: {faction}')
        for item in rescue.get('required_resources',[]):
            if item.get('resource_id') not in known['resources']: errors.append(f'unknown rescue resource: {item.get("resource_id")}')
    transition_statuses=set(data['rescue_transitions']['statuses'])
    for transition in data['rescue_transitions']['transitions']:
        if transition.get('from_status') not in transition_statuses or transition.get('to_status') not in transition_statuses: errors.append(f'unknown rescue transition status: {transition.get("id")}')
        if transition.get('required_state') not in known['travel_states']: errors.append(f'unknown transition state: {transition.get("required_state")}')
    operation_ids={item['id'] for item in data['resources']['operations']}
    for delta in data['reputation_factions']['deltas']:
        if delta.get('faction_id') not in known['factions']: errors.append(f'unknown reputation faction: {delta.get("faction_id")}')
        if delta.get('operation_id') not in operation_ids: errors.append(f'unknown reputation operation: {delta.get("operation_id")}')
    event_types={item.get('event_type') for item in data['audit_events']['events']}
    for scenario in data['scenarios']['scenarios']:
        if scenario.get('operation_id') not in {item['id'] for item in data['mission_operations']['operations']}: errors.append(f'unknown scenario operation: {scenario.get("operation_id")}')
        if scenario.get('rescue_id') not in known['rescue_requirements']: errors.append(f'unknown scenario rescue: {scenario.get("rescue_id")}')
        if scenario.get('result') not in data['scenarios']['results']: errors.append(f'unknown scenario result: {scenario.get("result")}')
        if scenario.get('deterministic') is not True: errors.append(f'non-deterministic scenario: {scenario.get("id")}')
    if not event_types: errors.append('audit events must not be empty')
    return errors
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--root',type=Path,default=ROOT); args=parser.parse_args(); errors=validate(args.root)
    if errors: print('\n'.join(f'ERROR: {x}' for x in errors),file=sys.stderr); return 1
    print('Content validation passed'); return 0
if __name__=='__main__': raise SystemExit(main())
