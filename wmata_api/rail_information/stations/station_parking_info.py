from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ParkingSummary:
    total_count: int

@dataclass(frozen=True)
class DailyParkingSummary(ParkingSummary):
    rider_cost: float
    rider_cost: Optional[float]
    non_rider_cost: Optional[float]
    saturday_rider_cost: Optional[int]
    saturday_non_rider_cost: Optional[int]

    @staticmethod
    def from_json(json: dict) -> "DailyParkingSummary":
        return DailyParkingSummary(
            total_count=json['TotalCount'],
            rider_cost=json['RiderCost'],
            non_rider_cost=json['NonRiderCost'],
            saturday_rider_cost=json['SaturdayRiderCost'],
            saturday_non_rider_cost=json['SaturdayNonRiderCost']
        )

@dataclass(frozen=True)
class ShortTermParkingSummary(ParkingSummary):
    notes: Optional[str]

    @staticmethod
    def from_json(json: dict) -> "ShortTermParkingSummary":
        return ShortTermParkingSummary(
            total_count=json['TotalCount'],
            notes=json['Notes']
        )

@dataclass(frozen=True)
class StationParkingInformation:
    code: str
    daily_parking_summary: DailyParkingSummary
    short_term_summary: ShortTermParkingSummary
    notes: Optional[str]

    @staticmethod
    def from_json(json: dict) -> 'StationParkingInformation':
        return StationParkingInformation(
            code=json['Code'],
            daily_parking_summary=DailyParkingSummary.from_json(json['AllDayParking']),
            short_term_summary=ShortTermParkingSummary.from_json(json['ShortTermParking']),
            notes=json['Notes']
        )

