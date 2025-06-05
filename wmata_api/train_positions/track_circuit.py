from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

@dataclass(frozen=True)
class TrackCircuit:
    """
    Base representation of a WMATA track circuit.

    Attributes:
        circuit_id (int): Unique identifier for the track circuit.
    """
    circuit_id: int

@dataclass(frozen=True)
class SequencedTrackCircuit(TrackCircuit):
    """
    A track circuit that is part of a sequenced route, possibly associated with a station, as returned by the WMATA API 'Standard Routes' endpoint.

    Attributes:
        seq_num (int): The order number of this circuit in a route sequence.
        station_code (Optional[str]): The station code associated with this circuit, if any.
    """
    seq_num: int
    station_code: Optional[str] = None

    @staticmethod
    def from_json(json: dict) -> 'SequencedTrackCircuit':
        return SequencedTrackCircuit(
            seq_num=json["SeqNum"],
            circuit_id=json["CircuitId"],
            station_code=json["StationCode"]
        )

class NeighborType(Enum):
    """
    Enum representing the direction of a neighboring circuit.

    Attributes:
        LEFT: The neighbor is to the left.
        RIGHT: The neighbor is to the right.
    """

    LEFT = "Left"
    RIGHT = "Right"


@dataclass(frozen=True)
class Neighbor:
    """
    Represents a set of neighboring track circuits in a particular direction.
    https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57644238031f59363c586dcb

    Attributes:
        neighbor_type (NeighborType): Indicates whether neighbors are to the left or right.
        circuit_ids (List[int]): List of circuit IDs that are neighbors in the given direction.
    """


    neighbor_type: NeighborType
    circuit_ids: List[int]

    @staticmethod
    def from_json(json: dict) -> "Neighbor":
        return Neighbor(
            neighbor_type=NeighborType(json["NeighborType"]),
            circuit_ids=json["CircuitIds"]
        )


@dataclass(frozen=True)
class DetailedTrackCircuit(TrackCircuit):
    """
    A detailed representation of a track circuit, as returned by the WMATA API track circuits endpoint.
    https://developer.wmata.com/api-details#api=5763fa6ff91823096cac1057&operation=57644238031f59363c586dcb

    Attributes:
        track (int): Identifier for the track that this circuit is part of.
        neighbors (List[Neighbor]): List of neighboring track circuits.
    """

    track: int
    neighbors: List[Neighbor]

    @staticmethod
    def from_json(json) -> "DetailedTrackCircuit":
        return DetailedTrackCircuit(
            track=json["Track"],
            circuit_id=json["CircuitId"],
            neighbors=[Neighbor.from_json(n) for n in json["Neighbors"]]
        )