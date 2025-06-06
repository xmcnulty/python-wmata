from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class StationEntrance:
    description: str
    latitude: float
    longitude: float
    name: str
    station_codes: List[str]

    @staticmethod
    def from_json(json: dict) -> 'StationEntrance':
        return StationEntrance(
            description=json['Description'],
            latitude=json['Lat'],
            longitude=json['Lon'],
            name=json['Name'],
            station_codes=[
                json[f"StationCode{i}"]
                for i in range(1, 3)
                if json[f"StationCode{i}"] is not None
            ]
        )