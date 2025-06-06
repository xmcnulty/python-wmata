from wmata_api.bus_predictions.next_busses import NextBusses
from wmata_api.core.wmata_api_module import WmataApiModule
from typing import List

from wmata_api.core.wmata_url import BusPredictionsEndpoint


class BussPredictions(WmataApiModule):

    def get_predictions(self, stop_id: int) -> NextBusses:
        params = {"StopID" : str(stop_id)}

        return self._get_and_parse_object(BusPredictionsEndpoint.BUS_PREDICTIONS.full_url(), NextBusses.from_json, params)