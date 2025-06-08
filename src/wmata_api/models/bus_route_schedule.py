from dataclasses import dataclass
from datetime import datetime
from typing import List

from wmata_api.models.bus_direction import BusDirection


@dataclass(frozen=True)
class StopTime:
    stop_id: int
    stop_name: str
    stop_sequence: int
    time: datetime

    @staticmethod
    def from_json(json) -> 'StopTime':
        return StopTime(
            stop_id=json['StopID'],
            stop_name=json['StopName'],
            stop_sequence=json['StopSequence'],
            time=datetime.fromisoformat(json['Time'])
        )

@dataclass(frozen=True)
class BusRouteLeg:
    start_time: datetime
    end_time: datetime
    route_id: str
    direction: BusDirection
    trip_headsign: str
    trip_id: str
    stop_times: List[StopTime]

    @staticmethod
    def from_json(json) -> 'BusRouteLeg':
        return BusRouteLeg(
            start_time=datetime.fromisoformat(json['StartTime']),
            end_time=datetime.fromisoformat(json['EndTime']),
            route_id=json['RouteID'],
            direction=BusDirection.from_string(json['TripDirectionText']),
            trip_headsign=json['TripHeadsign'],
            trip_id=json['TripID'],
            stop_times=[StopTime.from_json(st) for st in json['StopTimes']]
        )

@dataclass(frozen=True)
class BusRouteSchedule:
    name: str
    legs: List[BusRouteLeg]

    @staticmethod
    def from_json(json) -> 'BusRouteSchedule':
        return BusRouteSchedule(
            name=json['Name'],
            legs=[
                BusRouteLeg.from_json(json[f"Direction{i}"])
                for i in range(2)
                if json[f"Direction{i}"] is not None
            ]
        )