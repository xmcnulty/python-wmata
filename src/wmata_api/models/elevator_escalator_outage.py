from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict


class UnitType(Enum):
    ELEVATOR = "ELEVATOR"
    ESCALATOR = "ESCALATOR"

@dataclass(frozen=True)
class ElevatorEscalatorOutage:
    date_out_of_service: datetime
    date_updated: datetime
    estimated_return_to_service: datetime
    location_description: str
    station_code: str
    station_name: str
    symptom_description: str
    unit_name: str
    unit_type: UnitType

    @staticmethod
    def from_json(json: Dict) -> "ElevatorEscalatorOutage":
        return ElevatorEscalatorOutage(
            date_out_of_service=datetime.fromisoformat(json["DateOutOfServ"]),
            date_updated=datetime.fromisoformat(json["DateUpdated"]),
            estimated_return_to_service=datetime.fromisoformat(json["EstimatedReturnToService"]),
            location_description=json["LocationDescription"],
            station_code=json["StationCode"],
            station_name=json["StationName"],
            symptom_description=json["SymptomDescription"],
            unit_name=json["UnitName"],
            unit_type=UnitType(json["UnitType"])
        )
