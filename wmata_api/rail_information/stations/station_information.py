from typing import List

from wmata_api.core.wmata_api_module import WmataApiModule
from wmata_api.core.wmata_url import RailInfoEndpoint
from wmata_api.rail_information.lines.line_code import LineCode
from wmata_api.rail_information.stations.station import Station
from wmata_api.rail_information.stations.station_entrance import StationEntrance
from wmata_api.rail_information.stations.station_timing import StationTiming
from wmata_api.rail_information.stations.station_to_station_information import StationToStationInformation


class StationInformation(WmataApiModule):
    def get_all_station_entrances(self) -> List[StationEntrance]:
        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_ENTRANCES.full_url(),
            key="Entrances",
            parser=StationEntrance.from_json
        )

    def get_station_entrances(self, lat: float, lon: float, radius: int) -> List[StationEntrance]:
        params = {
            "Lat": lat,
            "Lon": lon,
            "Radius": radius
        }

        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_ENTRANCES.full_url(),
            key="Entrances",
            parser=StationEntrance.from_json,
            params=params
        )

    def get_all_stations(self) -> List[Station]:
        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_LIST,
            key="Stations",
            parser=Station.from_json
        )

    def get_all_stations_on_line(self, line_code: LineCode) -> List[Station]:
        params = {"LineCode": line_code.name}

        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_LIST,
            key="Stations",
            parser=Station.from_json,
            params=params
        )

    def get_station_information(self, station_code: str) -> Station:
        params = {"StationCode": station_code}

        return self._get_and_parse_object(
            url=RailInfoEndpoint.STATION_INFORMATION.full_url(),
            parser=Station.from_json,
            params=params
        )

    def get_all_station_timings(self) -> List[StationTiming]:
        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_TIMING.full_url(),
            key="StationTimes",
            parser=StationTiming.from_json
        )

    def get_station_timing(self, station_code: str) -> List[StationTiming]:
        params = {"StationCode": station_code}

        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_TIMING.full_url(),
            key="StationTimes",
            parser=StationTiming.from_json,
            params=params
        )

    def get_all_station_to_station_information(self) -> List[StationToStationInformation]:
        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_TO_STATION.full_url(),
            key="StationToStationInfos",
            parser=StationToStationInformation.from_json
        )

    def get_station_to_station_information(self, from_station_code: str, to_station_code: str) -> List[StationToStationInformation]:
        params = {
            "FromStationCode": from_station_code,
            "ToStationCode": to_station_code
        }

        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_TO_STATION.full_url(),
            key="StationToStationInfos",
            parser=StationToStationInformation.from_json,
            params=params
        )