from dataclasses import dataclass
from typing import Dict, List

from wmata_api.rail_info.line_code import LineCode


@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    zipcode: str

    @staticmethod
    def from_json(json: Dict) -> 'Address':
        return Address(
            street=json['Street'],
            city=json['City'],
            state=json['State'],
            zipcode=json['Zip']
        )

@dataclass
class Station:
    address: Address
    code: str
    latitude: float
    lines: List[LineCode]
    longitude: float
    name: str
    station_together: str

    @staticmethod
    def from_json(json: Dict) -> 'Station':
        return Station(
            address=Address.from_json(json['Address']),
            code=json['Code'],
            latitude=json['Lat'],
            lines = [
                LineCode(json[f"LineCode{i}"])
                for i in range(1, 5)
                if json.get(f"LineCode{i}") is not None
            ],
            longitude=json['Lon'],
            name=json['Name'],
            station_together=json['StationTogether1']
        )