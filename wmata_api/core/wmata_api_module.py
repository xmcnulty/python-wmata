import logging

from wmata_api.core.exceptions import WmataApiException
from wmata_api.core.parsing import Parsing
from wmata_api.core.rest_adapter import RestAdapter
from typing import TypeVar, Callable, List, Dict, Optional

T = TypeVar('T')

class WmataApiModule:
    _params: Optional[Dict[str, str]] = None

    def __init__(
            self,
            rest_adapter: RestAdapter,
            logger: logging.Logger
    ) -> None:
        """
        Initializes the TrainsPositionsApi client.

        Args:
            rest_adapter (RestAdapter): Performs http requests to the api.
            logger (logging.Logger, optional): Optional logger instance for debugging/logging.
        """

        self._logger = logger

        self._rest_adapter = rest_adapter

    def _get_and_parse_list(self, url, key: str, parser: Callable[[Dict], T]) -> List[T]:
        result = self._rest_adapter.get(url, self._params)
        items = result.data.get(key)
        if items is None:
            self._logger.error(f"Missing key '{key}' in response from {url}")
            raise WmataApiException(f"Response missing expected key: {key}")

        return Parsing.parse_list(items, parser, self._logger)

    def _get_and_parse_object(self, url, parser: Callable[[Dict], T]) -> T:
        result = self._rest_adapter.get(url, self._params)

        try:
            obj = parser(result.data)
            return obj
        except Exception as e:
            self._logger.error(f"Failed to parse {result.data} returned from {url} with {parser.__name__}")
            raise WmataApiException(f"Failed to parse {result.data} returned from {url}") from e