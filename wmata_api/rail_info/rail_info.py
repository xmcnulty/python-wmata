from typing import List

from wmata_api.core.wmata_api_module import WmataApiModule
from wmata_api.core.wmata_url import RailInfoEndpoint
from wmata_api.rail_info.line_code import LineCode
from wmata_api.rail_info.rail_line import RailLine
from wmata_api.rail_info.station import Station


class RailInfo(WmataApiModule):

    def get_rail_lines(self) -> List[RailLine]:
        return self._get_and_parse_list(
            url=RailInfoEndpoint.RAIL_LINES.full_url(),
            key="Lines",
            parser=RailLine.from_json
        )

    def get_station_list(self, line: LineCode = None) -> List[Station]:
        params = None if line is None else {"LineCode": line.value}

        return self._get_and_parse_list(
            url=RailInfoEndpoint.STATION_LIST.full_url(),
            key="Stations",
            parser=Station.from_json,
            params=params
        )