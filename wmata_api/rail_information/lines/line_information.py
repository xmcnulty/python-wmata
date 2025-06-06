from typing import List

from wmata_api.core.wmata_api_module import WmataApiModule
from wmata_api.core.wmata_url import RailInfoEndpoint
from wmata_api.rail_information.lines.metro_path_item import MetroPathItem
from wmata_api.rail_information.lines.rail_line import RailLine


class LineInformation(WmataApiModule):
    def get_path_between_stations(self, from_station_code: str, to_station_code) -> List[MetroPathItem]:
        params = {
            'FromStationCode': from_station_code,
            'ToStationCode': to_station_code
        }

        return self._get_and_parse_list(
            url=RailInfoEndpoint.PATH_BETWEEN_STATIONS.full_url(),
            key="Path",
            parser=MetroPathItem.from_json,
            params=params
        )

    def get_rail_lines(self) -> List[RailLine]:
        return self._get_and_parse_list(
            url=RailInfoEndpoint.RAIL_LINES.full_url(),
            key="Lines",
            parser=RailLine.from_json
        )