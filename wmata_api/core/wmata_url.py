from enum import Enum

class WmataUrl:
    _BASE_URL = "https://api.wmata.com"

    def full_url(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

class TrainPositionsEndpoint(WmataUrl, Enum):
    LIVE_TRAIN_POSITIONS = "TrainPositions"
    STANDARD_ROUTES = "StandardRoutes"
    TRACK_CIRCUITS = "TrackCircuits"

    def full_url(self) -> str:
        return f"{self._BASE_URL}/TrainPositions/{self.value}"


class RailPredictionsEndpoint(WmataUrl, Enum):
    RAIL_PREDICTIONS = "StationPrediction.svc/json/GetPrediction"

    def full_url(self) -> str:
        return f"{self._BASE_URL}/{self.value}"

class BusPredictionsEndpoint(WmataUrl, Enum):
    BUS_PREDICTIONS = "NextBusService.svc/json/jPredictions"

    def full_url(self) -> str:
        return f"{self._BASE_URL}/{self.value}"