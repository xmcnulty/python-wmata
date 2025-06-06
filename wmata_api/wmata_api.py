import logging

from wmata_api.core.rest_adapter import RestAdapter
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
            logger=logger
        )

        self.train_positions = TrainPositions(self._rest_adapter, self._logger)