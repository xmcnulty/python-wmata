from dataclasses import dataclass

@dataclass(frozen=True)
class RailFare:
    off_peak: float
    peak: float
    senior_and_disabled: float

    @staticmethod
    def from_json(json: dict) -> "RailFare":
        return RailFare(
            off_peak=json["OffPeakTime"],
            peak=json["PeakTime"],
            senior_and_disabled=json["SeniorDisabled"],
        )

@dataclass(frozen=True)
class StationToStationInformation:
    miles: float
    origin_code: str
    destination_code: str
    rail_time: int
    fare: RailFare

    @staticmethod
    def from_json(json: dict) -> "StationToStationInformation":
        return StationToStationInformation(
            miles=json["CompositeMiles"],
            origin_code=json["SourceStation"],
            destination_code=json["DestinationStation"],
            rail_time=json["RailTime"],
            fare=RailFare.from_json(json["RailFare"]),
        )