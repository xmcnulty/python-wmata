from datetime import datetime, timezone
from unittest import TestCase

from wmata_api.models.bus_direction import BusDirection
from wmata_api.models.bus_position import BusPosition

class TestBusPosition(TestCase):
    def setUp(self):
        self.sample_json = {
        "DateTime": "2014-10-27T01:23:40Z",
        "Deviation": 7,
        "DirectionNum": "10",
        "DirectionText": "NORTH",
        "Lat": 39.191525,
        "Lon": -76.672821,
        "RouteID": "B30",
        "TripEndTime": "2014-10-27T01:17:00Z",
        "TripHeadsign": "BWI LT RAIL STA",
        "TripID": "6794838",
        "TripStartTime": "2014-10-27T12:40:00Z",
        "VehicleID": "6217"
    }

    def test_bus_position_from_json_parses_all_fields_correctly(self):
        position = BusPosition.from_json(self.sample_json)

        assert isinstance(position, BusPosition)
        assert position.date_time == datetime(2014, 10, 27, 1, 23, 40, tzinfo=timezone.utc)
        assert position.deviation == 7
        assert position.direction == BusDirection.NORTH
        assert position.latitude == 39.191525
        assert position.longitude == -76.672821
        assert position.route_id == "B30"
        assert position.trip_id == "6794838"
        assert position.trip_end_time == datetime(2014, 10, 27, 1, 17, 0, tzinfo=timezone.utc)
        assert position.destination == "BWI LT RAIL STA"
        assert position.trip_id == "6794838"
        assert position.vehicle_id == "6217"
        assert position.trip_start_time == datetime(2014, 10, 27, 12, 40, 00, tzinfo=timezone.utc)

    def test_bus_position_with_invalid_direction_defaults_to_unknown(self):
        self.sample_json["DirectionText"] = "Invalid Direction"

        position = BusPosition.from_json(self.sample_json)

        assert position.direction == BusDirection.UNKNOWN

    def test_bus_position_missing_field_raises_key_error(self):
        del self.sample_json["VehicleID"]

        with self.assertRaises(KeyError):
            BusPosition.from_json(self.sample_json)

    def test_bus_position_with_invalid_datetime_raises_value_error(self):
        self.sample_json["DateTime"] = "invalid-datetime"

        with self.assertRaises(ValueError):
            BusPosition.from_json(self.sample_json)