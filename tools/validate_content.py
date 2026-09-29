#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {"mission": re.compile(r"^BC_MISSION_[A-Z0-9_]+$"), "evidence": re.compile(r"^BC_EVIDENCE_[A-Z0-9_]+$"), "character": re.compile(r"^BC_CHAR_[A-Z0-9_]+$"), "faction": re.compile(r"^BC_FACTION_[A-Z0-9_]+$"), "region": re.compile(r"^BC_REGION_[A-Z0-9_]+$"), "location": re.compile(r"^BC_LOCATION_[A-Z0-9_]+$"), "route": re.compile(r"^BC_ROUTE_[A-Z0-9_]+$"), "transport": re.compile(r"^BC_TRANSPORT_[A-Z0-9_]+$"), "travel_state": re.compile(r"^BC_TRAVEL_STATE_[A-Z0-9_]+$"), "resource": re.compile(r"^BC_RESOURCE_[A-Z0-9_]+$"), "operation": re.compile(r"^BC_OPERATION_[A-Z0-9_]+$"), "rescue": re.compile(r"^BC_RESCUE_[A-Z0-9_]+$"), "person": re.compile(r"^BC_PERSON_[A-Z0-9_]+$"), "audit": re.compile(r"^BC_AUDIT_[A-Z0-9_]+$"), "gate": re.compile(r"^BC_GATE_[A-Z0-9_]+$")}
def load(path: Path) -> Any:
    with path.open(encoding='utf-8') as handle: return json.load(handle)
def validate(root: Path = ROOT) -> list[str]:
    errors=[]
    required=('missions','evidence','regions','locations','characters','factions','routes','transport','travel_states','resources','rescue_requirements','reputation_factions','persons','mission_operations','rescue_transitions','audit_events','safety_gates')
    for name in required:
        path=root/'data'/f'{name}.json'
        if not path.is_file(): errors.append(f'missing catalog: {name}')
        else:
            try: load(path)
            except (OSError,json.JSONDecodeError) as exc: errors.append(f'invalid catalog {name}: {exc}')
    if errors: return errors
    data={name:load(root/'data'/f'{name}.json') for name in required}
    ids={}
    for name, payload in data.items():
        key={'rescue_requirements':'rescues','reputation_factions':'factions','mission_operations':'operations','rescue_transitions':'transitions','audit_events':'events','safety_gates':'gates'}.get(name,name)
        items=payload.get(key,[])
        for item in items:
            value=item.get('id') or item.get('faction_id')
            if value in ids: errors.append(f'duplicate id: {value}')
            ids[value]=name
    resource_ids={x['id'] for x in data['resources']['resources']}; mission_ids={x['id'] for x in data['missions']['missions']}; rescue_ids={x['id'] for x in data['rescue_requirements']['rescues']}; state_ids={x['id'] for x in data['travel_states']['travel_states']}; person_ids={x['id'] for x in data['persons']['persons']}; location_ids={x['id'] for x in data['locations']['locations']}
    for operation in data['mission_operations']['operations']:
        for field, known in (('mission_id',mission_ids),('rescue_id',rescue_ids),('required_travel_state',state_ids),('next_travel_state',state_ids)):
            if operation.get(field) not in known: errors.append(f'unknown {field}: {operation.get(field)}')
        for item in operation.get('resource_inputs',[]):
            if item.get('resource_id') not in resource_ids: errors.append(f'unknown operation resource: {item.get("resource_id")}')
    for rescue in data['rescue_requirements']['rescues']:
        if rescue.get('person_id') not in person_ids: errors.append(f'unknown rescue person: {rescue.get("person_id")}')
        if rescue.get('destination_location_id') not in location_ids: errors.append(f'unknown rescue destination: {rescue.get("destination_location_id")}')
    event_ids={x['id'] for x in data['audit_events']['events']}; gate_ids={x['id'] for x in data['safety_gates']['gates']}
    if not event_ids or not gate_ids: errors.append('audit and safety catalogs must not be empty')
    return errors
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--root',type=Path,default=ROOT); args=parser.parse_args(); errors=validate(args.root)
    if errors: print('\n'.join(f'ERROR: {x}' for x in errors),file=sys.stderr); return 1
    print('Content validation passed'); return 0
if __name__=='__main__': raise SystemExit(main())
