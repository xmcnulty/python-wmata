import logging
from typing import List, TypeVar, Callable

from wmata_api.core.exceptions import WmataApiException
from wmata_api.core.rest_adapter import RestAdapter
from wmata_api.train_positions.standard_route import StandardRoute
from wmata_api.train_positions.track_circuit import DetailedTrackCircuit
from wmata_api.train_positions.train_position import TrainPosition

T = TypeVar('T')

class TrainsPositionsApi:
    _hostname = "api.wmata.com/TrainPositions"

    # required parameter
    _params = {"contentType": "json"}

    def __init__(
            self,
            api_key: str,
            ssl_verify: bool = True,
            logger: logging.Logger = None,
            safe_mode: bool = False
    ) -> None:
        """
                Initializes the TrainsPositionsApi client.

                Args:
                    api_key (str): WMATA API key. (required)
                    ssl_verify (bool): Whether to verify SSL certificates. Default is True.
                    logger (logging.Logger, optional): Optional logger instance for debugging/logging.
                    safe_mode (bool): If True, skips over malformed entries instead of raising an exception.
                """
        self.safe_mode = safe_mode

        self._logger = logger or logging.getLogger(__name__)

        self._rest_adapter = RestAdapter(
            hostname=self._hostname,
            api_key=api_key,
            ssl_verify=ssl_verify,
            logger=self._logger
        )

    def _get_and_parse( self, endpoint: str, key: str, parser: Callable[[dict], T]) -> List[T]:
        """
        Fetches data from the given WMATA endpoint, extracts a list from the specified key,
        and parses each item using the provided parser function.

        Args:
            endpoint (str): API endpoint, e.g., "TrainPositions"
            key (str): Key in the JSON response that holds a list of items
            parser (Callable[[dict], T]): Function to parse each item

        Returns:
            List[T]: List of successfully parsed objects

        Raises:
            WmataApiException: If parsing fails and safe_mode is False
        """

        result = self._rest_adapter.get(endpoint=endpoint, params=self._params)
        items = result.data.get(key, [])

        parsed = []

        for i, item in enumerate(items):
            try:
                parsed.append(parser(item))
            except Exception as e:
                msg = f"Failed to parse item from {endpoint} at index {i}: {e}"
                if self.safe_mode:
                    self._logger.warning(f"Skipping malformed item: {msg}")
                else:
                    self._logger.error(msg)
                    raise WmataApiException(f"Failed to pars JSON from {endpoint}") from e

        return parsed

    def get_train_positions(self) -> List[TrainPosition]:
        """
        Retrieves the current positions of all trains in the WMATA system.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=5763fb35f91823096cac1058

        Returns:
            List[TrainPosition]: A list of TrainPosition objects representing each train's current location.
        """
        return self._get_and_parse("TrainPositions", "TrainPositions", TrainPosition.from_json)

    def get_standard_routes(self) -> List[StandardRoute]:
        """
        Retrieves the standard train routes used in the WMATA rail system.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57641afc031f59363c586dca

        Returns:
            List[StandardRoute]: A list of StandardRoute objects defining the predefined train paths.
        """
        return self._get_and_parse("StandardRoutes", "StandardRoutes", StandardRoute.from_json)

    def get_detailed_track_circuits(self) -> List[DetailedTrackCircuit]:
        """
        Returns a list of all track circuits including those on pocket tracks and crossovers.
        Each track circuit may include references to its right and left neighbors.
        https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57644238031f59363c586dcb

        Returns:
            List[DetailedTrackCircuit]: A list of DetailedTrackCircuit objects with circuit-specific details.
        """
        return self._get_and_parse("TrackCircuits", "TrackCircuits", DetailedTrackCircuit.from_json)