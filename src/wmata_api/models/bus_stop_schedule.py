from dataclasses import dataclass
from datetime import datetime
from typing import List

from wmata_api.core.utils import parse_wmata_timestamp
from wmata_api.models.bus_direction import BusDirection
from wmata_api.models.bus_stop import BusStop

@dataclass(frozen=True)
class BusStationArrival:
    start_time: datetime
    end_time: datetime
    schedule_time: datetime
    route_id: str
    direction: BusDirection
    destination: str
    trip_id: str

    @staticmethod
    def from_json(json) -> 'BusStationArrival':
        return BusStationArrival(
            start_time=parse_wmata_timestamp(json['StartTime']),
            end_time=parse_wmata_timestamp(json['EndTime']),
            schedule_time=parse_wmata_timestamp(json['ScheduleTime']),
            route_id=json['RouteID'],
            direction=BusDirection.from_string(json['TripDirectionText']),
            destination=json['TripHeadsign'],
            trip_id=json['TripID']
        )

@dataclass(frozen=True)
class BusStopSchedule:
    stop: BusStop
    scheduled_arrivals: List[BusStationArrival]

    @staticmethod
    def from_json(json) -> 'BusStopSchedule':
        arrivals_data = json.get('ScheduleArrivals') or []

        scheduled_arrivals = [BusStationArrival.from_json(sa) for sa in arrivals_data]

        return BusStopSchedule(
            stop=BusStop.from_json(json['Stop']),
            scheduled_arrivals=scheduled_arrivals
        )