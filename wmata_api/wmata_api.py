import logging

from wmata_api.bus_predictions.bus_predictions import BussPredictions
from wmata_api.core.rest_adapter import RestAdapter
from wmata_api.incidents.incidents import Incidents
from wmata_api.rail_information.rail_information import RailInformation
from wmata_api.rail_predictions.rail_predictions import RailPredictions
from wmata_api.train_positions.train_positions import TrainPositions


class WmataApi:
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
        self.bus_predictions = BussPredictions(self._rest_adapter, self._logger)
        self.rail_info = RailInformation(self._rest_adapter, self._logger)
        self.incidents = Incidents(self._rest_adapter, self._logger)