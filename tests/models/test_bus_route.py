from unittest import TestCase

from wmata_api.models.bus_route import BusRoute


class TestBusRoute(TestCase):

    def setUp(self):
        self.json = {
        "RouteID": "10A",
        "Name": "10A - HUNTING POINT -PENTAGON",
        "LineDescription": "Hunting Point-Pentagon Line"
    }

    def test_parse_proper_json(self):
        route = BusRoute.from_json(self.json)

        assert route.id == "10A"
        assert route.name == "10A - HUNTING POINT -PENTAGON"
        assert route.line_description == "Hunting Point-Pentagon Line"
