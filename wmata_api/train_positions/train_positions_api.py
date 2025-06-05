import logging
from typing import List

from wmata_api.core.rest_adapter import RestAdapter
from wmata_api.train_positions.standard_route import StandardRoute
from wmata_api.train_positions.track_circuit import DetailedTrackCircuit
from wmata_api.train_positions.train_position import TrainPosition


class TrainsPositionsApi:
    _hostname = "api.wmata.com/TrainPositions"

    # required parameter
    _params = {"contentType": "json"}

    def __init__(self, api_key: str, ssl_verify: bool = True, logger: logging.Logger = None) -> None:
        """
                Initializes the TrainsPositionsApi client.

                Args:
                    api_key (str): WMATA API key. (required)
                    ssl_verify (bool): Whether to verify SSL certificates. Default is True.
                    logger (logging.Logger, optional): Optional logger instance for debugging/logging.
                """
        self._rest_adapter = RestAdapter(
            hostname=self._hostname,
            api_key=api_key,
            ssl_verify=ssl_verify,
            logger=logger
        )

    def get_train_positions(self) -> List[TrainPosition]:
        """
        Retrieves the current positions of all trains in the WMATA system.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=5763fb35f91823096cac1058

        Returns:
            List[TrainPosition]: A list of TrainPosition objects representing each train's current location.
        """
        result = self._rest_adapter.get(endpoint="TrainPositions", params=self._params)

        positions_data = result.data.get("TrainPositions", [])

        return [TrainPosition.from_json(p) for p in positions_data]

    def get_standard_routes(self) -> List[StandardRoute]:
        """
        Retrieves the standard train routes used in the WMATA rail system.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57641afc031f59363c586dca

        Returns:
            List[StandardRoute]: A list of StandardRoute objects defining the predefined train paths.
        """
        result = self._rest_adapter.get(endpoint="StandardRoutes", params=self._params)

        standard_routes_data = result.data.get("StandardRoutes", [])

        return [StandardRoute.from_json(r) for r in standard_routes_data]

    def get_detailed_track_circuits(self) -> List[DetailedTrackCircuit]:
        """
        Returns a list of all track circuits including those on pocket tracks and crossovers.
        Each track circuit may include references to its right and left neighbors.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57644238031f59363c586dcb

        Returns:
            List[DetailedTrackCircuit]: A list of DetailedTrackCircuit objects with circuit-specific details.
        """
        result = self._rest_adapter.get(endpoint="TrackCircuits", params=self._params)

        circuits_data = result.data.get("TrackCircuits", [])

        return [DetailedTrackCircuit.from_json(c) for c in circuits_data]