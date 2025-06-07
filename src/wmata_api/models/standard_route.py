from dataclasses import dataclass
from typing import List

from src.wmata_api.models.track_circuit import SequencedTrackCircuit


@dataclass(frozen=True)
class StandardRoute:
    """
    Represents standard route data returned by the WMATA API.

    Attributes:
        line_code (str): Line code (e.g., 'RD' for Red Line).
        track_num (str): Track number (1 or 2).
        track_circuits_sequenced (List[SequencedTrackCircuit]): Array containing ordered track circuit information
    """
    line_code: str
    track_num: int
    track_circuits_sequenced: List[SequencedTrackCircuit]

    @staticmethod
    def from_json(json: dict) -> 'StandardRoute':
        return StandardRoute(
            line_code=json["LineCode"],
            track_num=json["TrackNum"],
            track_circuits_sequenced=[SequencedTrackCircuit.from_json(n) for n in json["TrackCircuits"]]
        )