import logging

from src.wmata_api.bus_predictions.bus_prediction_service import BusPredictions
from src.wmata_api.core.rest_adapter import RestAdapter
from src.wmata_api.incidents.incidents import Incidents
from src.wmata_api.rail_information.rail_information_service import RailInformation
from src.wmata_api.rail_predictions.rail_prediction_service import RailPredictions
from src.wmata_api.train_positions.train_positions_service import TrainPositions
from wmata_api.bus_info.bus_info_service import BusInformationService


class WmataApiClient:
    def __init__(
            self,
            api_key: str,
            ssl_verify: bool = True,
            logger: logging.Logger = None
    ):
        self._logger = logger or logging.getLogger(__name__)
        self._rest_adapter = RestAdapter(
            api_key=api_key,
            ssl_verify=ssl_verify,
            logger=self._logger
        )

        self.train_positions = TrainPositions(self._rest_adapter, self._logger)
        self.rail_predictions = RailPredictions(self._rest_adapter, self._logger)
        self.bus_predictions = BusPredictions(self._rest_adapter, self._logger)
        self.rail_info = RailInformation(self._rest_adapter, self._logger)
        self.incidents = Incidents(self._rest_adapter, self._logger)
        self.bus_info = BusInformationService(self._rest_adapter, self._logger)

__all__ = ["WmataApiClient"]