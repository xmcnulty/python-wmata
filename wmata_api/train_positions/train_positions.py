from typing import List
from wmata_api.core.wmata_api_module import WmataApiModule
from wmata_api.core.wmata_url import TrainPositionsEndpoint
from wmata_api.train_positions.standard_route import StandardRoute
from wmata_api.train_positions.track_circuit import DetailedTrackCircuit
from wmata_api.train_positions.train_position import TrainPosition

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
        return self._get_and_parse(TrainPositionsEndpoint.LIVE_TRAIN_POSITIONS, "TrainPositions", TrainPosition.from_json)

    def get_standard_routes(self) -> List[StandardRoute]:
        """
        Retrieves the standard train routes used in the WMATA rail system.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57641afc031f59363c586dca

        Returns:
            List[StandardRoute]: A list of StandardRoute objects defining the predefined train paths.
        """
        return self._get_and_parse(TrainPositionsEndpoint.STANDARD_ROUTES, "StandardRoutes", StandardRoute.from_json)

    def get_detailed_track_circuits(self) -> List[DetailedTrackCircuit]:
        """
        Returns a list of all track circuits including those on pocket tracks and crossovers.
        Each track circuit may include references to its right and left neighbors.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57644238031f59363c586dcb

        Returns:
            List[DetailedTrackCircuit]: A list of DetailedTrackCircuit objects with circuit-specific details.
        """
        return self._get_and_parse(TrainPositionsEndpoint.TRACK_CIRCUITS, "TrackCircuits", DetailedTrackCircuit.from_json)