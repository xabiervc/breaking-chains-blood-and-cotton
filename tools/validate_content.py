#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {"mission": re.compile(r"^BC_MISSION_[A-Z0-9_]+$"), "evidence": re.compile(r"^BC_EVIDENCE_[A-Z0-9_]+$"), "character": re.compile(r"^BC_CHAR_[A-Z0-9_]+$"), "faction": re.compile(r"^BC_FACTION_[A-Z0-9_]+$"), "region": re.compile(r"^BC_REGION_[A-Z0-9_]+$"), "location": re.compile(r"^BC_LOCATION_[A-Z0-9_]+$"), "route": re.compile(r"^BC_ROUTE_[A-Z0-9_]+$"), "transport": re.compile(r"^BC_TRANSPORT_[A-Z0-9_]+$"), "travel_state": re.compile(r"^BC_TRAVEL_STATE_[A-Z0-9_]+$"), "resource": re.compile(r"^BC_RESOURCE_[A-Z0-9_]+$"), "operation": re.compile(r"^BC_OPERATION_[A-Z0-9_]+$"), "rescue": re.compile(r"^BC_RESCUE_[A-Z0-9_]+$"), "person": re.compile(r"^BC_PERSON_[A-Z0-9_]+$"), "reputation": re.compile(r"^BC_REPUTATION_[A-Z0-9_]+$")}

def load(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)

def collect(items: list[dict[str, Any]], key: str, label: str, errors: list[str]) -> set[str]:
    values = set()
    for index, item in enumerate(items):
        value = item.get(key) if isinstance(item, dict) else None
        if not isinstance(value, str) or not value:
            errors.append(f"{label}[{index}] has no valid {key}")
        elif value in values:
            errors.append(f"duplicate {label} id: {value}")
        else:
            values.add(value)
    return values

def ref(value: Any, kind: str, label: str, known: dict[str, set[str]], errors: list[str]) -> None:
    if not isinstance(value, str) or not PATTERNS[kind].fullmatch(value): errors.append(f"invalid {label}: {value}")
    elif value not in known[kind]: errors.append(f"unknown {label}: {value}")

def validate(root: Path = ROOT) -> list[str]:
    names = ("missions","evidence","regions","locations","characters","factions","routes","transport","travel_states","resources","rescue_requirements","reputation_factions","persons")
    files = {name: load(root / "data" / f"{name}.json") for name in names}
    key_for = {"rescue_requirements":"rescues","reputation_factions":"factions","travel_states":"travel_states"}
    collections = {name: files[name].get(key_for.get(name, name), []) for name in names}
    errors: list[str] = []
    kind_for = {"transport":"transport","travel_states":"travel_state","resources":"resource","rescue_requirements":"rescue","reputation_factions":"faction","persons":"person"}
    known = {kind_for.get(name, name.rstrip("s")): collect(items, "id" if name != "reputation_factions" else "faction_id", kind_for.get(name, name.rstrip("s")), errors) for name, items in collections.items()}
    for item in collections["locations"]: ref(item.get("region_id"), "region", f"location region in {item.get('id')}", known, errors)
    for item in collections["missions"]:
        for field, kind in (("region_id","region"),("location_id","location")): ref(item.get(field), kind, f"{field} in {item.get('id')}", known, errors)
        for field, kind in (("characters","character"),("factions","faction"),("evidence_granted","evidence")):
            for value in item.get(field, []): ref(value, kind, f"{field} in {item.get('id')}", known, errors)
    for item in collections["evidence"]:
        ref(item.get("source_location"), "location", f"source location in {item.get('id')}", known, errors)
        for value in item.get("required_for", []): ref(value, "mission", f"required mission in {item.get('id')}", known, errors)
    for item in collections["routes"]:
        for field, kind in (("origin_region_id","region"),("destination_region_id","region"),("origin_location_id","location"),("destination_location_id","location")): ref(item.get(field), kind, f"{field} in {item.get('id')}", known, errors)
        if not item.get("deterministic_inputs"): errors.append(f"route has no deterministic inputs: {item.get('id')}")
        defined_types = {x.get("type") for x in collections["transport"]}
        for value in item.get("transport_types", []):
            if value not in defined_types: errors.append(f"unknown transport type in {item.get('id')}: {value}")
    for item in collections["travel_states"]:
        if "random" in item: errors.append(f"travel state contains forbidden random field: {item.get('id')}")
        for value in item.get("allowed_next", []): ref(value, "travel_state", f"travel transition from {item.get('id')}", known, errors)
    resource_ids = known["resource"]
    operation_ids = set()
    for operation in files["resources"].get("operations", []):
        if not PATTERNS["operation"].fullmatch(operation.get("id", "")): errors.append(f"invalid operation id: {operation.get('id')}")
        operation_ids.add(operation.get("id"))
        for entry in operation.get("inputs", []) + operation.get("outputs", []):
            ref(entry.get("resource_id"), "resource", f"resource in operation {operation.get('id')}", known, errors)
            if not isinstance(entry.get("amount"), int) or entry.get("amount") <= 0: errors.append(f"invalid amount in operation {operation.get('id')}")
    for item in collections["rescue_requirements"]:
        ref(item.get("person_id"), "person", f"person in rescue {item.get('id')}", known, errors)
        ref(item.get("destination_location_id"), "location", f"destination in rescue {item.get('id')}", known, errors)
        faction = item.get("minimum_reputation", {}).get("faction_id")
        ref(faction, "faction", f"reputation faction in rescue {item.get('id')}", known, errors)
        for entry in item.get("required_resources", []): ref(entry.get("resource_id"), "resource", f"required resource in rescue {item.get('id')}", known, errors)
    for item in files["reputation_factions"].get("deltas", []):
        ref(item.get("faction_id"), "faction", f"reputation delta faction in {item.get('id')}", known, errors)
        if item.get("operation_id") not in operation_ids: errors.append(f"unknown reputation operation: {item.get('operation_id')}")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--root", type=Path, default=ROOT); args = parser.parse_args(); errors = validate(args.root)
    if errors: print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr); return 1
    print("Content validation passed"); return 0
if __name__ == "__main__": raise SystemExit(main())
