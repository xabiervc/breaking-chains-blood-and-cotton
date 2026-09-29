import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_content import validate
class RouteDataTests(unittest.TestCase):
    def test_routes_and_transport_are_valid_json(self):
        routes = json.loads((ROOT / "data" / "routes.json").read_text(encoding="utf-8"))
        transport = json.loads((ROOT / "data" / "transport.json").read_text(encoding="utf-8"))
        self.assertEqual(len(routes["routes"]), 5)
        self.assertEqual(len(transport["transport"]), 5)
    def test_routes_have_deterministic_inputs(self):
        routes = json.loads((ROOT / "data" / "routes.json").read_text(encoding="utf-8"))["routes"]
        for route in routes:
            self.assertTrue(route["deterministic_inputs"])
            self.assertEqual(set(route["alert_modifiers"]), {"LOW", "MEDIUM", "HIGH"})
    def test_route_transport_types_are_defined(self):
        routes = json.loads((ROOT / "data" / "routes.json").read_text(encoding="utf-8"))["routes"]
        transport = json.loads((ROOT / "data" / "transport.json").read_text(encoding="utf-8"))["transport"]
        defined = {item["type"] for item in transport}
        for route in routes:
            self.assertTrue(set(route["transport_types"]) <= defined)
    def test_route_regions_match_endpoint_locations(self):
        data = {name: json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))[name] for name in ("routes", "locations")}
        locations = {item["id"]: item["region_id"] for item in data["locations"]}
        for route in data["routes"]:
            self.assertEqual(locations[route["origin_location_id"]], route["origin_region_id"])
            self.assertEqual(locations[route["destination_location_id"]], route["destination_region_id"])
    def test_content_validator_still_passes(self):
        self.assertEqual(validate(ROOT), [])
if __name__ == "__main__":
    unittest.main()
