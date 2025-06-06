from dataclasses import dataclass
from typing import Dict

from wmata_api.rail_information.lines.line_code import LineCode


@dataclass(frozen=True)
class RailLine:
    display_name: str
    end_station_code: str
    internal_destination_1: str
    internal_destination_2: str
    line_code: LineCode
    start_station_code: str

    @staticmethod
    def from_json(json: Dict) -> "RailLine":
        return RailLine(
            display_name=json["DisplayName"],
            end_station_code=json["EndStationCode"],
            internal_destination_1=json["InternalDestination1"],
            internal_destination_2=json["InternalDestination2"],
            line_code=LineCode[json["LineCode"]],
            start_station_code=json["StartStationCode"]
        )