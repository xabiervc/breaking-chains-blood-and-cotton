#!/usr/bin/env python3
"""Validate structured mission and evidence content."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MISSION_ID = re.compile(r"^BC_MISSION_[A-Z0-9_]+$")
EVIDENCE_ID = re.compile(r"^BC_EVIDENCE_[A-Z0-9_]+$")
CHARACTER_ID = re.compile(r"^BC_CHAR_[A-Z0-9_]+$")
FACTION_ID = re.compile(r"^BC_FACTION_[A-Z0-9_]+$")
REGION_ID = re.compile(r"^BC_REGION_[A-Z0-9_]+$")
LOCATION_ID = re.compile(r"^BC_LOCATION_[A-Z0-9_]+$")


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def unique_ids(items: list[dict[str, Any]], key: str, label: str) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(items):
        value = item.get(key)
        if not isinstance(value, str) or not value:
            errors.append(f"{label}[{index}] has no valid {key}")
        elif value in seen:
            errors.append(f"duplicate {label} id: {value}")
        else:
            seen.add(value)
    return errors


def check_pattern(value: str, pattern: re.Pattern[str], label: str, errors: list[str]) -> None:
    if not pattern.fullmatch(value):
        errors.append(f"invalid {label}: {value}")


def validate_missions(data: dict[str, Any], evidence_ids: set[str]) -> list[str]:
    errors: list[str] = []
    missions = data.get("missions")
    if not isinstance(missions, list):
        return ["missions.json must contain a missions array"]
    errors.extend(unique_ids(missions, "id", "mission"))
    mission_ids = {item.get("id") for item in missions if isinstance(item, dict)}
    required = {"id", "act", "classification", "region_id", "location_id", "prerequisites", "objectives", "evidence_granted", "failure_states", "success_state", "characters", "factions", "resources", "rewards", "reputation_effects", "deterministic_inputs", "tags"}
    for mission in missions:
        if not isinstance(mission, dict):
            errors.append("mission entries must be objects")
            continue
        missing = required - mission.keys()
        errors.extend(f"{mission.get('id', '<unknown>')} missing field: {field}" for field in sorted(missing))
        mission_id = mission.get("id")
        if isinstance(mission_id, str):
            check_pattern(mission_id, MISSION_ID, "mission id", errors)
        for prerequisite in mission.get("prerequisites", []):
            if isinstance(prerequisite, str) and prerequisite.startswith("BC_MISSION_") and prerequisite not in mission_ids:
                errors.append(f"{mission_id} references unknown mission prerequisite: {prerequisite}")
        for evidence_id in mission.get("evidence_granted", []):
            if evidence_id not in evidence_ids:
                errors.append(f"{mission_id} references unknown evidence: {evidence_id}")
        for character_id in mission.get("characters", []):
            if isinstance(character_id, str):
                check_pattern(character_id, CHARACTER_ID, "character id", errors)
        for faction_id in mission.get("factions", []):
            if isinstance(faction_id, str):
                check_pattern(faction_id, FACTION_ID, "faction id", errors)
        if isinstance(mission.get("region_id"), str):
            check_pattern(mission["region_id"], REGION_ID, "region id", errors)
        if isinstance(mission.get("location_id"), str):
            check_pattern(mission["location_id"], LOCATION_ID, "location id", errors)
    return errors


def validate_evidence(data: dict[str, Any], mission_ids: set[str]) -> list[str]:
    errors: list[str] = []
    evidence = data.get("evidence")
    if not isinstance(evidence, list):
        return ["evidence.json must contain an evidence array"]
    errors.extend(unique_ids(evidence, "id", "evidence"))
    for item in evidence:
        if not isinstance(item, dict):
            errors.append("evidence entries must be objects")
            continue
        evidence_id = item.get("id")
        if isinstance(evidence_id, str):
            check_pattern(evidence_id, EVIDENCE_ID, "evidence id", errors)
        if isinstance(item.get("source_location"), str):
            check_pattern(item["source_location"], LOCATION_ID, "evidence source location", errors)
        for mission_id in item.get("required_for", []):
            if mission_id not in mission_ids:
                errors.append(f"{evidence_id} references unknown mission: {mission_id}")
    return errors


def validate_cross_references(missions: list[dict[str, Any]], evidence: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    defined_evidence = {item.get("id") for item in evidence}
    defined_missions = {item.get("id") for item in missions}
    for mission in missions:
        for evidence_id in mission.get("evidence_granted", []):
            if evidence_id not in defined_evidence:
                errors.append(f"granted evidence is not defined: {evidence_id}")
    for item in evidence:
        for mission_id in item.get("required_for", []):
            if mission_id not in defined_missions:
                errors.append(f"required mission is not defined: {mission_id}")
    return errors


def validate(root: Path = ROOT) -> list[str]:
    missions_data = load_json(root / "data" / "missions.json")
    evidence_data = load_json(root / "data" / "evidence.json")
    missions = missions_data.get("missions", [])
    evidence = evidence_data.get("evidence", [])
    evidence_ids = {item.get("id") for item in evidence if isinstance(item, dict)}
    mission_ids = {item.get("id") for item in missions if isinstance(item, dict)}
    errors = validate_missions(missions_data, evidence_ids)
    errors.extend(validate_evidence(evidence_data, mission_ids))
    errors.extend(validate_cross_references(missions, evidence))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        errors = validate(args.root)
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        print(f"validation error: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Content validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
