import json
import os
from datetime import datetime, timezone
from unittest import TestCase

from wmata_api.models.bus_direction import BusDirection
from wmata_api.models.bus_route_schedule import BusRouteSchedule


class TestBusRouteSchedule(TestCase):

    def setUp(self):
        file_path = os.path.join(os.path.dirname(__file__), "json", "test_bus_route_schedule.json")
        with open(file_path, "r") as json_file:
            self.json = json.load(json_file)

    def test_bus_route_schedule_from_sample_json(self):
        rs = BusRouteSchedule.from_json(self.json)

        assert isinstance(rs, BusRouteSchedule)
        assert len(rs.directional_trips) == 2
        assert rs.name == "B30 - B30 GREENBELT-BWI (647)"

        # check direction0
        assert rs.directional_trips[0][0].direction == BusDirection.NORTH
        assert rs.directional_trips[0][0].start_time == datetime(2014, 10, 27, 6, 10, 0, tzinfo=timezone.utc)
        assert rs.directional_trips[0][0].end_time == datetime(2014, 10, 27, 6, 45, 0, tzinfo=timezone.utc)
        assert len(rs.directional_trips[0][0].stop_times) > 0
        assert rs.directional_trips[0][0].stop_times[0].time == datetime(2014, 10, 27, 6, 10, 0, tzinfo=timezone.utc)

        #check direction1
        assert rs.directional_trips[1][0].direction == BusDirection.SOUTH
        assert rs.directional_trips[1][0].start_time == datetime(2014, 10, 27, 6, 54, 0, tzinfo=timezone.utc)
        assert rs.directional_trips[1][0].end_time == datetime(2014, 10, 27, 7, 32, 0, tzinfo=timezone.utc)
        assert len(rs.directional_trips[1][0].stop_times) > 0
        assert rs.directional_trips[1][0].stop_times[0].time == datetime(2014, 10, 27, 6, 54, 0, tzinfo=timezone.utc)

    def test_bus_route_schedule_null_direction1(self):
        self.json["Direction1"] = None
        rs = BusRouteSchedule.from_json(self.json)

        assert isinstance(rs, BusRouteSchedule)
        assert len(rs.directional_trips) == 1