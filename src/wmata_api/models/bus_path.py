from dataclasses import dataclass
from typing import List

from wmata_api.models.bus_direction import BusDirection
from wmata_api.models.bus_stop import BusStop

@dataclass(frozen=True)
class ShapePoint:
    latitude: float
    longitude: float
    sequence_number: int

    @staticmethod
    def from_json(json) -> "ShapePoint":
        return ShapePoint(
            latitude=json["Lat"],
            longitude=json["Lon"],
            sequence_number=json["SeqNum"]
        )

@dataclass(frozen=True)
class BusPathLeg:
    direction: BusDirection
    stops: List[BusStop]
    trip_headsign: str
    shape: List[ShapePoint]

    @staticmethod
    def from_json(json) -> "BusPathLeg":
        return BusPathLeg(
            direction=BusDirection.from_string(json["DirectionText"]),
            stops=[BusStop.from_json(s) for s in json["Stops"]],
            trip_headsign=json["TripHeadsign"],
            shape=[ShapePoint.from_json(s) for s in json["Shape"]]
        )


@dataclass(frozen=True)
class BusPath:
    route_name: str
    route_id: str
    legs: List[BusPathLeg]

    @staticmethod
    def from_json(json) -> "BusPath":
        return BusPath(
            route_name=json["Name"],
            route_id=json["RouteID"],
            legs=[
                BusPathLeg.from_json(json[f"Direction{i}"])
                for i in range(2)
                if json[f"Direction{i}"] is not None
            ]
        )
