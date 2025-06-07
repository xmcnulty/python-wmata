from typing import List

from src.wmata_api.core.wmata_api_module import WmataApiModule
from src.wmata_api.core.wmata_endpoint import IncidentsEndpoint
from src.wmata_api.models.bus_incident import BusIncident
from src.wmata_api.models.elevator_escalator_outage import ElevatorEscalatorOutage
from src.wmata_api.models.rail_incident import RailIncident


class Incidents(WmataApiModule):

    def get_all_bus_incidents(self) -> List[BusIncident]:
        return self._get_and_parse_list(
            url=IncidentsEndpoint.BUS_INCIDENTS.full_url,
            key="BusIncidents",
            parser=BusIncident.from_json
        )

    def get_bus_incidents_for_route(self, route: str) -> List[BusIncident]:
        params = {"Route": route}

        return self._get_and_parse_list(
            url=IncidentsEndpoint.BUS_INCIDENTS.full_url,
            key="BusIncidents",
            parser=BusIncident.from_json,
            params=params
        )

    def get_rail_incidents(self) -> List[RailIncident]:
        return self._get_and_parse_list(
            url=IncidentsEndpoint.RAIL_INCIDENTS.full_url,
            key="Incidents",
            parser=RailIncident.from_json
        )

    def get_all_elevator_escalator_outages(self) -> List[ElevatorEscalatorOutage]:
        return self._get_and_parse_list(
            url=IncidentsEndpoint.ELEVATOR_ESCALATOR_INCIDENTS.full_url,
            key="ElevatorIncidents",
            parser=ElevatorEscalatorOutage.from_json
        )

    def get_elevator_escalator_outages(self, station_code: str) -> List[ElevatorEscalatorOutage]:
        params = {"StationCode": station_code}

        return self._get_and_parse_list(
            url=IncidentsEndpoint.ELEVATOR_ESCALATOR_INCIDENTS.full_url,
            key="ElevatorIncidents",
            parser=ElevatorEscalatorOutage.from_json,
            params=params
        )