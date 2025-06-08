import json
import os
from unittest import TestCase
from datetime import datetime, timezone

from wmata_api.models.bus_direction import BusDirection
from wmata_api.models.bus_stop_schedule import BusStopSchedule


class TestBusStopSchedule(TestCase):
    def setUp(self):
        file_path = os.path.join(os.path.dirname(__file__), "json", "test_bus_stop_schedule.json")
        print(file_path)
        with open(file_path, "r") as json_file:
            self.json = json.load(json_file)

    def test_from_json_sample(self):
        schedule = BusStopSchedule.from_json(self.json)

        assert isinstance(schedule, BusStopSchedule)

        assert len(schedule.scheduled_arrivals) > 0
        assert schedule.stop.stop_id == "3002578"

        first_arrival = schedule.scheduled_arrivals[0]

        assert first_arrival.direction == BusDirection.SOUTH
        assert first_arrival.trip_id == "6788790"
        assert first_arrival.start_time == datetime(2014, 10, 27, 4, 46, 0, tzinfo=timezone.utc)
        assert first_arrival.end_time == datetime(2014, 10, 27, 5, 37, 0, tzinfo=timezone.utc)
        assert first_arrival.schedule_time == datetime(2014, 10, 27, 5, 35, 12, tzinfo=timezone.utc)

    def test_from_json_empty_schedule_arrivals(self):
        self.json["ScheduleArrivals"] = []

        schedule = BusStopSchedule.from_json(self.json)

        assert isinstance(schedule, BusStopSchedule)

        assert len(schedule.scheduled_arrivals) == 0
        assert schedule.stop.stop_id == "3002578"

    def test_from_json_null_schedule_departures(self):
        self.json["ScheduleArrivals"] = None
        schedule = BusStopSchedule.from_json(self.json)

        assert isinstance(schedule, BusStopSchedule)

        assert len(schedule.scheduled_arrivals) == 0
        assert schedule.stop.stop_id == "3002578"