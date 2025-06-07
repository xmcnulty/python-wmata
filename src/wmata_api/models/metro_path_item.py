from dataclasses import dataclass

from src.wmata_api.models.line_code import LineCode


@dataclass(frozen=True)
class MetroPathItem:
    distance_to_previous: int
    line_code: LineCode
    sequence_number: int
    station_code: str
    station_name: str

    @staticmethod
    def from_json(json) -> 'MetroPathItem':
        return MetroPathItem(
            distance_to_previous=json['DistanceToPrev'],
            line_code=LineCode(json['LineCode']),
            sequence_number=json['SeqNum'],
            station_code=json['StationCode'],
            station_name=json['StationName']
        )