from datetime import datetime

from wmata_api.core.wmata_api_module import WmataApiModule
from typing import List, Optional, Dict, Any

from wmata_api.core.wmata_endpoints import BusInformation
from wmata_api.models.bus_position import BusPosition
from wmata_api.models.bus_path import BusPath
from wmata_api.models.bus_route import BusRoute
from wmata_api.models.bus_route_schedule import BusRouteSchedule
from wmata_api.models.bus_stop import BusStop
from wmata_api.models.bus_stop_schedule import BusStopSchedule


class BusInformationService(WmataApiModule):

    def get_all_bus_stops(self) -> List[BusStop]:
        return self._get_and_parse_list(
            url=BusInformation.STOP_SEARCH.full_url,
            key="Stops",
            parser=BusStop.from_json
        )

    def search_bus_stops(self, lat: float, lon: float, radius: int) -> List[BusStop]:
        params = {
            "Lat": lat,
            "Lon": lon,
            "Radius": radius
        }

        return self._get_and_parse_list(
            url=BusInformation.STOP_SEARCH.full_url,
            key="Stops",
            parser=BusStop.from_json,
            params=params
        )

    def get_bus_routes(self) -> List[BusRoute]:
        return self._get_and_parse_list(
            url=BusInformation.BUS_ROUTES.full_url,
            key="Routes",
            parser=BusRoute.from_json
        )

    def _get_bus_positions(self, params: Optional[Dict]) -> List[BusPosition]:
        return self._get_and_parse_list(
            url=BusInformation.BUS_POSITIONS.full_url,
            key="BusPositions",
            parser=BusPosition.from_json,
            params=params
        )

    def get_bus_positions_by_route(self, route_id: Optional[str] = None) -> List[BusPosition]:
        params = None if route_id is None else {"RouteID": route_id}
        return self._get_bus_positions(params)

    def get_bus_positions_nearby(self, lat: float, lon: float, radius: int, route_id: Optional[str]) -> List[BusPosition]:
        params: Dict[str, Any] = {
            "Lat": lat,
            "Lon": lon,
            "Radius": radius
        }

        if route_id is not None:
            params["RouteID"] = route_id

        return self._get_bus_positions(params)

    def get_bus_path(self, route_id: str, date: Optional[datetime] = None) -> BusPath:
        params = {
            "RouteID": route_id,
        }

        if date is not None:
            params["Date"] = date.strftime("%Y-%m-%d")

        return self._get_and_parse_object(
            url=BusInformation.BUS_PATH.full_url,
            parser=BusPath.from_json,
            params=params
        )

    def get_route_schedule(
            self,
            route_id: str,
            date: Optional[datetime] = None,
            include_variations: Optional[bool] = False
    ):
        params: Dict[str, Any] = {
            "RouteID": route_id,
            "IncludeVariations": include_variations
        }

        if date is not None:
            params["Date"] = date.strftime("%Y-%m-%d")

        return self._get_and_parse_object(
            url=BusInformation.ROUTE_SCHEDULE.full_url,
            parser=BusRouteSchedule.from_json,
            params=params
        )

    def get_stop_schedule(self, route_id: str, date: Optional[datetime] = None) -> BusStopSchedule:
        params: Dict[str, Any] = { "RouteID": route_id }

        if date is not None:
            params["Date"] = date.strftime("%Y-%m-%d")

        return self._get_and_parse_object(
            url=BusInformation.STOP_SCHEDULE.full_url,
            parser=BusStopSchedule.from_json,
            params=params
        )