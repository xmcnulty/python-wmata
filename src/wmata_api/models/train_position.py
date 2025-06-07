from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional

class ServiceType(Enum):
    """
    Enumeration of possible WMATA train service types.
    https://developer.wmata.com/api-details#SeviceType

    Attributes:
        NO_PASSENGERS: Non-revenue train with no passengers.
        NORMAL: Normal revenue service train.
        SPECIAL: Special revenue service train with an unspecified line and destination.
        More prevalent during scheduled track work.
        UNKNOWN: Service type is unknown or could not be determined.
    """
    NO_PASSENGERS = "NoPassengers"
    NORMAL = "Normal"
    SPECIAL = "Special"
    UNKNOWN = "Unknown"


@dataclass(frozen=True)
class TrainPosition:
    """
    Represents train position information provided by the WMATA API.
    https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=5763fb35f91823096cac1058

    Attributes:
        train_id (str): Uniquely identifiable internal train identifier.
        train_number (str): Non-unique train identifier, often used by WMATA's Rail Scheduling and Operations Teams, as well as over open radio communication.
        car_count (int): Number of cars in the train. 0 when no data available.
        direction_num (int): The direction of movement regardless of which track the train is on. Valid values are 1 or 2. Generally speaking, trains with direction 1 are northbound/eastbound, while trains with direction 2 are southbound/westbound.
        circuit_id (int): Track circuit identifier where the train is currently located.
        seconds_at_location (int): Number of seconds the train has been at its current location.
        service_type (ServiceType): Type of service the train is providing (e.g., Normal, Special).
        destination_station_code (Optional[str]): Station code of the train’s final destination. Can be None.
        line_code (Optional[str]): Line code (e.g., 'RD' for Red Line). Can be None.
    """

    train_id: str
    train_number: str
    car_count: int
    direction_num: int
    circuit_id: int
    seconds_at_location: int
    service_type: ServiceType
    destination_station_code: Optional[str] = None
    line_code: Optional[str] = None

    @staticmethod
    def from_json(json: Dict) -> 'TrainPosition':
        """
        Creates a TrainPosition instance from a WMATA API JSON dictionary.

        Args:
            json (Dict): Dictionary parsed from the WMATA API response.

        Returns:
            TrainPosition: A populated TrainPosition object.
        """

        return TrainPosition(
            train_id=json["TrainId"],
            train_number=json["TrainNumber"],
            car_count=json["CarCount"],
            direction_num=json["DirectionNum"],
            circuit_id=json["CircuitId"],
            seconds_at_location=json["SecondsAtLocation"],
            service_type=ServiceType(json["ServiceType"]),
            destination_station_code=json["DestinationStationCode"],
            line_code=json["LineCode"]
        )