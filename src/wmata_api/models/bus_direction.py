from enum import Enum


class BusDirection(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    WEST = "WEST"
    EAST = "EAST"
    LOOP = "LOOP"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_string(cls, string) -> "BusDirection":
        try:
            return BusDirection(string.upper())
        except (ValueError, AttributeError):
            return cls.UNKNOWN