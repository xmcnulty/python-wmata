import logging

from src.wmata_api.core.rest_adapter import RestAdapter
from src.wmata_api.rail_information.lines.line_information_service import LineInformation
from src.wmata_api.rail_information.stations.station_information_service import StationInformation


class RailInformation:

    def __init__(self, rest_adapter: RestAdapter, logger: logging.Logger):
        self.rest_adapter = rest_adapter
        self.logger = logger

        self.lines = LineInformation(rest_adapter=self.rest_adapter, logger=self.logger)
        self.stations = StationInformation(rest_adapter=self.rest_adapter, logger=self.logger)