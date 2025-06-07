from enum import Enum

class WmataUrl:
    _BASE_URL = "https://api.wmata.com"

    def full_url(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

class TrainPositionsEndpoint(WmataUrl, Enum):
    LIVE_TRAIN_POSITIONS = "TrainPositions/TrainPositions"
    STANDARD_ROUTES = "TrainPositions/StandardRoutes"
    TRACK_CIRCUITS = "TrainPositions/TrackCircuits"

    def full_url(self) -> str:
        return f"{self._BASE_URL}/{self.value}"


class RailPredictionsEndpoint(WmataUrl, Enum):
    RAIL_PREDICTIONS = "StationPrediction.svc/json/GetPrediction"

    def full_url(self) -> str:
        return f"{self._BASE_URL}/{self.value}"

class BusPredictionsEndpoint(WmataUrl, Enum):
    BUS_PREDICTIONS = "NextBusService.svc/json/jPredictions"

    def full_url(self) -> str:
        return f"{self._BASE_URL}/{self.value}"

class RailInfoEndpoint(WmataUrl, Enum):
    RAIL_LINES = "Rail.svc/json/jLines"
    STATION_LIST = "Rail.svc/json/jStations"
    PARKING_INFORMATION = "Rail.svc/json/jStationParking"
    PATH_BETWEEN_STATIONS = "Rail.svc/json/jPath"
    STATION_ENTRANCES = "Rail.svc/json/jStationEntrances"
    STATION_INFORMATION = "Rail.svc/json/jStationInfo"
    STATION_TIMING = "Rail.svc/json/jStationTimes"
    STATION_TO_STATION = "Rail.svc/json/jSrcStationToDstStationInfo"

    def full_url(self) -> str:
        return f"{self._BASE_URL}/{self.value}"

class IncidentsEndpoint(WmataUrl, Enum):
    BUS_INCIDENTS = "Incidents.svc/json/BusIncidents"
    RAIL_INCIDENTS = "Incidents.svc/json/Incidents"
    ELEVATOR_ESCALATOR_INCIDENTS = "Incidents.svc/json/ElevatorIncidents"

    def full_url(self) -> str:
        return f"{self._BASE_URL}/{self.value}"