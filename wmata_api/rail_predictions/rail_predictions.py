from typing import List

from wmata_api.core.wmata_api_module import WmataApiModule
from wmata_api.core.wmata_url import RailPredictionsEndpoint
from wmata_api.rail_predictions.rail_prediction_info import RailPredictionInfo


class RailPredictions(WmataApiModule):
    @staticmethod
    def _build_url(station_codes: List[str]) -> str:
        url_base = RailPredictionsEndpoint.RAIL_PREDICTIONS.full_url()
        return f"{url_base}/{','.join(station_codes)}"

    def _get(self, stations: List[str]) -> List[RailPredictionInfo]:
        url = self._build_url(stations)

        return self._get_and_parse_list(url, "Trains", RailPredictionInfo.from_json)

    def get_all_predictions(self) -> List[RailPredictionInfo]:
        return self._get(['All'])

    def get_predictions(self, stations: List[str]) -> List[RailPredictionInfo]:
        return self._get(stations)