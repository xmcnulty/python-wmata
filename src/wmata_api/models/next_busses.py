from dataclasses import dataclass
from typing import List, Dict

@dataclass(frozen=True)
class Prediction:
    direction_num: str
    direction_text: str
    minutes: int
    route_id: str
    trip_id: str
    vehicle_id: str

    @staticmethod
    def from_json(json: Dict) -> 'Prediction':
        return Prediction(
            direction_num=json['DirectionNum'],
            direction_text=json['DirectionText'],
            minutes=json['Minutes'],
            route_id=json['RouteID'],
            trip_id=json['TripID'],
            vehicle_id=json['VehicleID']
        )


@dataclass(frozen=True)
class NextBusses:
    predictions: List[Prediction]
    stop_name: str

    @staticmethod
    def from_json(json: Dict) -> 'NextBusses':
        return NextBusses(
            stop_name=json['StopName'],
            predictions=[Prediction.from_json(p) for p in json.get("Predictions", [])]
        )