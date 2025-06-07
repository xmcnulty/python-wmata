from enum import Enum
from dataclasses import dataclass
from typing import Dict, List

class Weekday(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

@dataclass
class TrainTime:
    time: str
    destination_station_code: str

    @staticmethod
    def from_json(json_data) -> "TrainTime":
        return TrainTime(
            time=json_data["Time"],
            destination_station_code=json_data["DestinationStation"]
        )

@dataclass
class DailySchedule:
    opening_time: str
    first_trains: List[TrainTime]
    last_trains: List[TrainTime]

    @staticmethod
    def from_json(json_data) -> "DailySchedule":
        return DailySchedule(
            opening_time=json_data["OpeningTime"],
            first_trains=[TrainTime.from_json(t) for t in json_data["FirstTrains"]],
            last_trains=[TrainTime.from_json(t) for t in json_data["LastTrains"]]
        )

@dataclass
class StationTiming:
    station_code: str
    station_name: str
    schedule: Dict[Weekday, DailySchedule]

    @staticmethod
    def from_json(json_data) -> "StationTiming":
        return StationTiming(
            station_code=json_data["StationCode"],
            station_name=json_data["StationName"],
            schedule={
                day : DailySchedule.from_json(json_data[day.value])
                for day in Weekday
                if day.value in json_data
            }
        )