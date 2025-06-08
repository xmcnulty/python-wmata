from dataclasses import dataclass

@dataclass(frozen=True)
class BusRoute:
    id: str
    name: str
    line_description: str

    @staticmethod
    def from_json(json) -> "BusRoute":
        return BusRoute(
            id=json["RouteID"],
            name=json["Name"],
            line_description=json["LineDescription"]
        )