from unittest import TestCase

from wmata_api.models.bus_stop import BusStop


class TestBusStop(TestCase):


    def setUp(self):
        self.json = {
        "Lat": 38.878356,
        "Lon": -76.990378,
        "Name": "K ST + POTOMAC AVE",
        "Routes": ["V7", "V7c", "V7cv1", "V7v1", "V7v2", "V8", "V9"],
        "StopID": "1000533"
    }

    def test_from_json_sample(self):
        stop = BusStop.from_json(self.json)

        assert isinstance(stop, BusStop)
        assert isinstance(stop.latitude, float)
        assert isinstance(stop.longitude, float)

        assert stop.stop_id == "1000533"

    def test_from_json_null_stop_id(self):
        # noinspection PyTypeChecker
        self.json["StopID"] = None

        stop = BusStop.from_json(self.json)

        assert isinstance(stop, BusStop)
        assert stop.stop_id is None

    def test_from_json_stop_id_0(self):
        self.json["StopID"] = "0"

        stop = BusStop.from_json(self.json)
        assert isinstance(stop, BusStop)
        assert stop.stop_id == "0"

