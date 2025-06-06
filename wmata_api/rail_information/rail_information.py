import logging

from wmata_api.core.rest_adapter import RestAdapter
from wmata_api.rail_information.lines.line_information import LineInformation
from wmata_api.rail_information.stations.station_information import StationInformation


class RailInformation:

    def __init__(self, rest_adapter: RestAdapter, logger: logging.Logger):
        self.rest_adapter = rest_adapter
        self.logger = logger

        self.lines = LineInformation(rest_adapter=self.rest_adapter, logger=self.logger)
        self.stations = StationInformation(rest_adapter=self.rest_adapter, logger=self.logger)