from dataclasses import dataclass
from typing import Optional, Dict

@dataclass(frozen=True)
class PredictionTrainInfo:
    """
    Data class storing fields of AIMPredictionTrainInfo returned by WMATA API.
    https://developer.wmata.com/api-details#AIMPredictionTrainInfo

    Attributes:
        num_cars (str): Number of cars on a train, usually 6 or 8, but might also return - or NULL.
        destination (str): Abbreviated version of the final destination for a train.
        destination_code (str): Destination station code. Can be NULL
        destination_name (str): When DestinationCode is populated, this is the full name of the destination station, as shown on the WMATA website.
        group (str): Denotes the track this train is on, but does not necessarily equate to Track 1 or Track 2.
        line_code (str): Two-letter abbreviation for the line (e.g.: RD, BL, YL, OR, GR, or SV). May also be blank or No for trains with no passengers.
        location_code (str): Station code for where the train is arriving.
        location_name (str): Full name of the station where the train is arriving.
        minutes (str): Minutes until arrival. Can be a numeric value, ARR (arriving), BRD (boarding), ---, or empty.
    """
    num_cars: Optional[str]
    destination: str
    destination_code: Optional[str]
    destination_name: str
    group: str
    line_code: str
    location_code: str
    location_name: str
    minutes: str

    @staticmethod
    def from_json(json: Dict) -> "PredictionTrainInfo":
        return PredictionTrainInfo(
            num_cars=json["Car"],
            destination=json["Destination"],
            destination_code=json["DestinationCode"],
            destination_name=json["DestinationName"],
            group=json["Group"],
            line_code=json["Line"],
            location_code=json["LocationCode"],
            location_name=json["LocationName"],
            minutes=json["Min"]
        )