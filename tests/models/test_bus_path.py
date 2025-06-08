import json
import os
from unittest import TestCase

from wmata_api.models.bus_direction import BusDirection
from wmata_api.models.bus_path import BusPath


class TestShapePoint(TestCase):
    def setUp(self):
        file_path = os.path.join(os.path.dirname(__file__), "json", "test_bus_path.json")
        with open(file_path, "r") as json_file:
            self.json = json.load(json_file)

    def test_bus_path_from_sample_json(self):
        path = BusPath.from_json(self.json)

        assert isinstance(path, BusPath)
        assert path.route_name == "B30 - B30 GREENBELT-BWI (647)"
        assert path.route_id == "B30"

        assert len(path.legs) == 2
        assert path.legs[0].direction == BusDirection.NORTH
        assert path.legs[0].destination == "BWI - THURGOOD MARSHALL  AIRPORT"
        assert len(path.legs[0].shape) > 0
        assert len(path.legs[0].stops) > 0
        assert path.legs[1].direction == BusDirection.SOUTH
        assert path.legs[1].destination == "GREENBELT STATION"
        assert len(path.legs[1].shape) > 0
        assert len(path.legs[1].stops) > 0

    def test_bus_path_with_null_direction0(self):
        self.json["Direction0"] = None

        path = BusPath.from_json(self.json)

        assert len(path.legs) == 1
        assert path.legs[0].direction == BusDirection.SOUTH
        assert path.legs[0].destination == "GREENBELT STATION"

    def test_bus_path_with_null_direction1(self):
        self.json["Direction1"] = None
        path = BusPath.from_json(self.json)

        assert len(path.legs) == 1
        assert path.legs[0].direction == BusDirection.NORTH
        assert path.legs[0].destination == "BWI - THURGOOD MARSHALL  AIRPORT"

    def test_bus_path_with_both_null_directions(self):
        self.json["Direction0"] = None
        self.json["Direction1"] = None
        path = BusPath.from_json(self.json)

        assert len(path.legs) == 0