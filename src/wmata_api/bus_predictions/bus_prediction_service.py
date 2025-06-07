from src.wmata_api.models.next_busses import NextBusses
from src.wmata_api.core.wmata_api_module import WmataApiModule

from src.wmata_api.core.wmata_endpoint import BusPredictionsEndpoint


class BusPredictions(WmataApiModule):

    def get_predictions(self, stop_id: int) -> NextBusses:
        params = {"StopID" : str(stop_id)}

        return self._get_and_parse_object(BusPredictionsEndpoint.BUS_PREDICTIONS.full_url, NextBusses.from_json, params)