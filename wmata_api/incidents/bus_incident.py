from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class BusIncident:
    date_updated: datetime
    description: str
    incident_id: str
    incident_type: str
    routes_affected: List[str]

    @staticmethod
    def from_json(json) -> "BusIncident":
        return BusIncident(
            date_updated=datetime.fromisoformat(json["DateUpdated"]),
            description=json["Description"],
            incident_id=json["IncidentID"],
            incident_type=json["IncidentType"],
            routes_affected=json["RoutesAffected"]
        )