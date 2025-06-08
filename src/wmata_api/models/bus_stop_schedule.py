from dataclasses import dataclass
from datetime import datetime
from typing import List

from wmata_api.models.bus_direction import BusDirection
from wmata_api.models.bus_stop import BusStop

@dataclass(frozen=True)
class BusStationArrival:
    start_time: datetime
    end_time: datetime
    schedule_time: datetime
    route_id: str
    direction: BusDirection
    trip_headsign: str
    trip_id: str

    @staticmethod
    def from_json(json) -> 'BusStationArrival':
        return BusStationArrival(
            start_time=datetime.fromisoformat(json['StartTime']),
            end_time=datetime.fromisoformat(json['EndTime']),
            schedule_time=datetime.fromisoformat(json['ScheduleTime']),
            route_id=json['RouteID'],
            direction=BusDirection.from_string(json['TripDirectionText']),
            trip_headsign=json['TripHeadsign'],
            trip_id=json['TripId']
        )

@dataclass(frozen=True)
class BusStopSchedule:
    stop: BusStop
    scheduled_arrivals: List[BusStationArrival]

    @staticmethod
    def from_json(json) -> 'BusStopSchedule':
        return BusStopSchedule(
            stop=BusStop.from_json(json['Stop']),
            scheduled_arrivals=[BusStationArrival.from_json(sa) for sa in json['ScheduleArrivals']]
        )