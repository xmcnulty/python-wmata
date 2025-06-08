from enum import Enum

class EndpointMixin:
    _BASE_URL = "https://api.wmata.com"

    @property
    def full_url(self) -> str:
        return f"{self._BASE_URL}/{self.value}" # type: ignore[attr-defined]

class TrainPositionsEndpoint(EndpointMixin, Enum):
    LIVE_TRAIN_POSITIONS = "TrainPositions/TrainPositions"
    STANDARD_ROUTES = "TrainPositions/StandardRoutes"
    TRACK_CIRCUITS = "TrainPositions/TrackCircuits"

class RailPredictionsEndpoint(EndpointMixin, Enum):
    RAIL_PREDICTIONS = "StationPrediction.svc/json/GetPrediction"

class BusPredictionsEndpoint(EndpointMixin, Enum):
    BUS_PREDICTIONS = "NextBusService.svc/json/jPredictions"

class RailInfoEndpoint(EndpointMixin, Enum):
    RAIL_LINES = "Rail.svc/json/jLines"
    STATION_LIST = "Rail.svc/json/jStations"
    PARKING_INFORMATION = "Rail.svc/json/jStationParking"
    PATH_BETWEEN_STATIONS = "Rail.svc/json/jPath"
    STATION_ENTRANCES = "Rail.svc/json/jStationEntrances"
    STATION_INFORMATION = "Rail.svc/json/jStationInfo"
    STATION_TIMING = "Rail.svc/json/jStationTimes"
    STATION_TO_STATION = "Rail.svc/json/jSrcStationToDstStationInfo"

class IncidentsEndpoint(EndpointMixin, Enum):
    BUS_INCIDENTS = "Incidents.svc/json/BusIncidents"
    RAIL_INCIDENTS = "Incidents.svc/json/Incidents"
    ELEVATOR_ESCALATOR_INCIDENTS = "Incidents.svc/json/ElevatorIncidents"

class BusInformation(EndpointMixin, Enum):
    STOP_SEARCH = "Bus.svc/json/jStops"
    BUS_ROUTES = "Bus.svc/json/jRoutes"
    BUS_POSITIONS = "Bus.svc/json/jBusPositions"
    BUS_PATH = "Bus.svc/json/jRouteDetails"
    ROUTE_SCHEDULE = "Bus.svc/json/jRouteSchedule"
    STOP_SCHEDULE = "Bus.svc/json/jStopSchedule"