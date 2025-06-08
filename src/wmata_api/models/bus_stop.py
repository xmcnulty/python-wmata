from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class BusStop:
    latitude: float
    longitude: float
    name: str
    routes: List[str]
    stop_id: Optional[str]

    @staticmethod
    def from_json(json) -> "BusStop":
        return BusStop(
            latitude=json["Lat"],
            longitude=json["Lon"],
            name=json["Name"],
            routes=json["Routes"],
            stop_id=json["StopID"]
        )