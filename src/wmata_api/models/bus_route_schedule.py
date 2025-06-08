from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

from wmata_api.core.utils import parse_wmata_timestamp
from wmata_api.models.bus_direction import BusDirection


@dataclass(frozen=True)
class StopTime:
    stop_id: int
    stop_name: str
    stop_sequence: int
    time: datetime

    @staticmethod
    def from_json(json: Dict) -> 'StopTime':
        return StopTime(
            stop_id=json['StopID'],
            stop_name=json['StopName'],
            stop_sequence=json['StopSeq'],
            time=datetime.fromisoformat(json['Time'])
        )

@dataclass(frozen=True)
class Trip:
    start_time: datetime
    end_time: datetime
    route_id: str
    direction: BusDirection
    destination: str
    trip_id: str
    stop_times: List[StopTime]

    @staticmethod
    def from_json(json: Dict) -> 'Trip':
        return Trip(
            start_time=parse_wmata_timestamp(json['StartTime']),
            end_time=parse_wmata_timestamp(json['EndTime']),
            route_id=json['RouteID'],
            direction=BusDirection.from_string(json['TripDirectionText']),
            destination=json['TripHeadsign'],
            trip_id=json['TripID'],
            stop_times=[StopTime.from_json(st) for st in json['StopTimes']]
        )

@dataclass(frozen=True)
class BusRouteSchedule:
    name: str
    directional_trips: List[List[Trip]]

    @staticmethod
    def from_json(json: Dict) -> 'BusRouteSchedule':
        directional_trips = []

        # build list of trips for each direction
        i = 0
        while f"Direction{i}" in json:
            if json[f"Direction{i}"] is not None:
                trips = [Trip.from_json(t) for t in json[f"Direction{i}"]]
                directional_trips.append(trips)
            i += 1

        return BusRouteSchedule(
            name=json['Name'],
            directional_trips=directional_trips
        )