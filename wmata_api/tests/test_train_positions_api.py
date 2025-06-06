import unittest
from unittest.mock import MagicMock, patch
from wmata_api.core.exceptions import WmataApiException
from wmata_api.train_positions.train_position import TrainPosition
from wmata_api.train_positions.standard_route import StandardRoute
from wmata_api.train_positions.track_circuit import DetailedTrackCircuit
from wmata_api.core.rest_adapter import Result
from wmata_api.train_positions.train_positions import TrainPositions


class TestTrainsPositionsApi(unittest.TestCase):
    def setUp(self):
        self.api_key = "fake-key"
        self.mock_logger = MagicMock()
        self.api = TrainPositions(api_key=self.api_key, logger=self.mock_logger)
        self.api._rest_adapter = MagicMock()

    def mock_result(self, key: str, items: list):
        return Result(status_code=200, message="OK", data={key: items})

    def test_get_train_positions_success(self):
        data = [{"TrainId": "1", "TrainNumber": "123", "CarCount": 6, "DirectionNum": 1,
                 "CircuitId": 101, "SecondsAtLocation": 45, "ServiceType": "Normal",
                 "DestinationStationCode": "A01", "LineCode": "RD"}]
        self.api._rest_adapter.get.return_value = self.mock_result("TrainPositions", data)

        with patch("wmata_api.train_positions.train_position.TrainPosition.from_json") as mock_parser:
            mock_parser.return_value = MagicMock(spec=TrainPosition)
            result = self.api.get_train_positions()

        self.assertEqual(len(result), 1)
        mock_parser.assert_called_once_with(data[0])

    def test_get_standard_routes_success(self):
        data = [{"RouteID": "R1", "TrackCircuits": []}]
        self.api._rest_adapter.get.return_value = self.mock_result("StandardRoutes", data)

        with patch("wmata_api.train_positions.standard_route.StandardRoute.from_json") as mock_parser:
            mock_parser.return_value = MagicMock(spec=StandardRoute)
            result = self.api.get_standard_routes()

        self.assertEqual(len(result), 1)
        mock_parser.assert_called_once_with(data[0])

    def test_get_detailed_track_circuits_success(self):
        data = [{"CircuitId": 1, "Track": 2, "Neighbors": []}]
        self.api._rest_adapter.get.return_value = self.mock_result("TrackCircuits", data)

        with patch("wmata_api.train_positions.track_circuit.DetailedTrackCircuit.from_json") as mock_parser:
            mock_parser.return_value = MagicMock(spec=DetailedTrackCircuit)
            result = self.api.get_detailed_track_circuits()

        self.assertEqual(len(result), 1)
        mock_parser.assert_called_once_with(data[0])

    def test_parser_error_with_safe_mode_on(self):
        data = [{"bad": "json"}]
        api = TrainPositions(api_key=self.api_key, logger=self.mock_logger, safe_mode=True)
        api._rest_adapter = MagicMock()
        api._rest_adapter.get.return_value = self.mock_result("TrainPositions", data)

        with patch("wmata_api.train_positions.train_position.TrainPosition.from_json", side_effect=ValueError("oops")):
            result = api.get_train_positions()

        self.assertEqual(result, [])
        self.mock_logger.warning.assert_called_once()
        self.mock_logger.error.assert_not_called()

    def test_parser_error_with_safe_mode_off(self):
        data = [{"bad": "json"}]
        self.api._rest_adapter.get.return_value = self.mock_result("TrainPositions", data)

        with patch("wmata_api.train_positions.train_position.TrainPosition.from_json", side_effect=ValueError("fail")):
            with self.assertRaises(WmataApiException):
                self.api.get_train_positions()
        self.mock_logger.error.assert_called_once()
        self.mock_logger.warning.assert_not_called()

    def test_empty_data_list_returns_empty(self):
        self.api._rest_adapter.get.return_value = self.mock_result("TrainPositions", [])
        with patch("wmata_api.train_positions.train_position.TrainPosition.from_json") as mock_parser:
            result = self.api.get_train_positions()
        self.assertEqual(result, [])
        mock_parser.assert_not_called()


if __name__ == "__main__":
    unittest.main()
