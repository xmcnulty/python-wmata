from dataclasses import dataclass
from datetime import datetime

from wmata_api.models.bus_direction import BusDirection


@dataclass(frozen=True)
class BusPosition:
    date_time: datetime
    deviation: int
    direction: BusDirection
    latitude: float
    longitude: float
    route_id: str
    trip_start_time: datetime
    trip_end_time: datetime
    trip_id: str
    vehicle_id: str

    @staticmethod
    def from_json(json) -> "BusPosition":
        return BusPosition(
            date_time = datetime.fromisoformat(json["DateTime"]),
            deviation = int(json["Deviation"]),
            direction = BusDirection.from_string(json["DirectionText"]),
            latitude = float(json["Lat"]),
            longitude = float(json["Lon"]),
            route_id = json["RouteID"],
            trip_start_time = datetime.fromisoformat(json["TripStartTime"]),
            trip_end_time = datetime.fromisoformat(json["TripEndTime"]),
            trip_id = json["TripID"],
            vehicle_id = json["VehicleID"]
        )
