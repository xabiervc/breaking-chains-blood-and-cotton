#!/usr/bin/env python3
"""Validate all structured content and cross-catalog references."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {"mission": re.compile(r"^BC_MISSION_[A-Z0-9_]+$"), "evidence": re.compile(r"^BC_EVIDENCE_[A-Z0-9_]+$"), "character": re.compile(r"^BC_CHAR_[A-Z0-9_]+$"), "faction": re.compile(r"^BC_FACTION_[A-Z0-9_]+$"), "region": re.compile(r"^BC_REGION_[A-Z0-9_]+$"), "location": re.compile(r"^BC_LOCATION_[A-Z0-9_]+$"), "route": re.compile(r"^BC_ROUTE_[A-Z0-9_]+$"), "transport": re.compile(r"^BC_TRANSPORT_[A-Z0-9_]+$")}

def load(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)

def ids(items: list[dict[str, Any]], label: str) -> tuple[set[str], list[str]]:
    found, errors = set(), []
    for index, item in enumerate(items):
        value = item.get("id") if isinstance(item, dict) else None
        if not isinstance(value, str) or not value:
            errors.append(f"{label}[{index}] has no valid id")
        elif value in found:
            errors.append(f"duplicate {label} id: {value}")
        else:
            found.add(value)
    return found, errors

def check_ref(value: Any, kind: str, label: str, known: dict[str, set[str]], errors: list[str]) -> None:
    if not isinstance(value, str) or not PATTERNS[kind].fullmatch(value):
        errors.append(f"invalid {label}: {value}")
    elif value not in known[kind]:
        errors.append(f"unknown {label}: {value}")

def validate(root: Path = ROOT) -> list[str]:
    names = ("missions", "evidence", "regions", "locations", "characters", "factions", "routes", "transport")
    files = {name: load(root / "data" / f"{name}.json") for name in names}
    collections = {name: files[name].get(name, []) for name in names}
    errors: list[str] = []
    known: dict[str, set[str]] = {}
    for name, items in collections.items():
        kind = "transport" if name == "transport" else name.rstrip("s")
        known[kind], local = ids(items, kind)
        errors.extend(local)
    for item in collections["locations"]:
        check_ref(item.get("region_id"), "region", f"location region in {item.get('id')}", known, errors)
    for item in collections["missions"]:
        mission_id = item.get("id")
        for field, kind in (("region_id", "region"), ("location_id", "location")):
            check_ref(item.get(field), kind, f"{field} in {mission_id}", known, errors)
        for field, kind in (("characters", "character"), ("factions", "faction"), ("evidence_granted", "evidence")):
            for value in item.get(field, []):
                check_ref(value, kind, f"{field} in {mission_id}", known, errors)
        for value in item.get("prerequisites", []):
            if value.startswith("BC_MISSION_") and value not in known["mission"]:
                errors.append(f"unknown prerequisite in {mission_id}: {value}")
    for item in collections["evidence"]:
        evidence_id = item.get("id")
        check_ref(item.get("source_location"), "location", f"source location in {evidence_id}", known, errors)
        for value in item.get("required_for", []):
            check_ref(value, "mission", f"required mission in {evidence_id}", known, errors)
    for item in collections["routes"]:
        route_id = item.get("id")
        for field, kind in (("origin_region_id", "region"), ("destination_region_id", "region"), ("origin_location_id", "location"), ("destination_location_id", "location")):
            check_ref(item.get(field), kind, f"{field} in {route_id}", known, errors)
        for transport_type in item.get("transport_types", []):
            if not any(item.get("type") == transport_type for item in collections["transport"]):
                errors.append(f"unknown transport type in {route_id}: {transport_type}")
        if not item.get("deterministic_inputs"):
            errors.append(f"route has no deterministic inputs: {route_id}")
    for item in collections["transport"]:
        if not PATTERNS["transport"].fullmatch(item.get("id", "")):
            errors.append(f"invalid transport id: {item.get('id')}")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        errors = validate(args.root)
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        print(f"validation error: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("Content validation passed")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
