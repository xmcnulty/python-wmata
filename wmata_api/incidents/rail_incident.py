from dataclasses import dataclass
from datetime import datetime
from typing import List

from wmata_api.rail_information.lines.line_code import LineCode


@dataclass(frozen=True)
class RailIncident:
    date_updated: datetime
    description: str
    incident_id: str
    incident_type: str
    lines_affected: List[LineCode]

    @staticmethod
    def from_json(json: dict) -> "RailIncident":
        # parse ; separated line codes
        lines = json["LinesAffected"]
        split_lines = [l.strip() for l in lines.split(';') if l.strip()]
        line_codes = [LineCode(lc) for lc in split_lines]

        return RailIncident(
            date_updated=datetime.fromisoformat(json["DateUpdated"]),
            description=json["Description"],
            incident_id=json["IncidentID"],
            incident_type=json["IncidentType"],
            lines_affected=line_codes
        )