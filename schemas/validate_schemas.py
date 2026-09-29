#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT = Path(__file__).resolve().parents[1]
PAIRS = {
    'resource.schema.json': 'data/resources.json',
    'rescue_requirement.schema.json': 'data/rescue_requirements.json',
    'reputation.schema.json': 'data/reputation_factions.json',
    'mission_operation.schema.json': 'data/mission_operations.json',
    'rescue_transition.schema.json': 'data/rescue_transitions.json',
    'audit_event.schema.json': 'data/audit_events.json',
    'safety_gate.schema.json': 'data/safety_gates.json',
    'scenario.schema.json': 'data/scenarios.json',
}
def main():
    errors=[]
    for schema_name, data_name in PAIRS.items():
        schema_path=ROOT/'schemas'/schema_name; data_path=ROOT/data_name
        if not schema_path.is_file(): errors.append(f'missing schema: {schema_name}'); continue
        if not data_path.is_file(): errors.append(f'missing data: {data_name}'); continue
        try:
            schema=json.loads(schema_path.read_text(encoding='utf-8'))
            data=json.loads(data_path.read_text(encoding='utf-8'))
            for error in Draft202012Validator(schema).iter_errors(data):
                errors.append(f'{schema_name}: {error.json_path}: {error.message}')
        except (OSError,json.JSONDecodeError,TypeError) as exc: errors.append(f'invalid JSON/schema: {schema_name}/{data_name}: {exc}')
    if errors:
        sys.stderr.write('\n'.join(f'ERROR: {item}' for item in errors)+'\n'); return 1
    print('Schema conformance validation passed'); return 0
if __name__ == '__main__': raise SystemExit(main())
