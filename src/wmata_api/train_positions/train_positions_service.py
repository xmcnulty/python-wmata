from typing import List
from src.wmata_api.core.wmata_api_module import WmataApiModule
from src.wmata_api.core.wmata_endpoint import TrainPositionsEndpoint
from src.wmata_api.models.standard_route import StandardRoute
from src.wmata_api.models.track_circuit import DetailedTrackCircuit
from src.wmata_api.models.train_position import TrainPosition

class TrainPositions(WmataApiModule):
    # required parameter
    _params = {"contentType": "json"}

    def get_train_positions(self) -> List[TrainPosition]:
        """
        Retrieves the current positions of all trains in the WMATA system.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=5763fb35f91823096cac1058

        Returns:
            List[TrainPosition]: A list of TrainPosition objects representing each train's current location.
        """
        return self._get_and_parse_list(TrainPositionsEndpoint.LIVE_TRAIN_POSITIONS.full_url, "TrainPositions", TrainPosition.from_json, self._params)

    def get_standard_routes(self) -> List[StandardRoute]:
        """
        Retrieves the standard train routes used in the WMATA rail system.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57641afc031f59363c586dca

        Returns:
            List[StandardRoute]: A list of StandardRoute objects defining the predefined train paths.
        """
        return self._get_and_parse_list(TrainPositionsEndpoint.STANDARD_ROUTES.full_url, "StandardRoutes", StandardRoute.from_json, self._params)

    def get_detailed_track_circuits(self) -> List[DetailedTrackCircuit]:
        """
        Returns a list of all track circuits including those on pocket tracks and crossovers.
        Each track circuit may include references to its right and left neighbors.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57644238031f59363c586dcb

        Returns:
            List[DetailedTrackCircuit]: A list of DetailedTrackCircuit objects with circuit-specific details.
        """
        return self._get_and_parse_list(TrainPositionsEndpoint.TRACK_CIRCUITS.full_url, "TrackCircuits", DetailedTrackCircuit.from_json, self._params)