import logging

from src.wmata_api.core.exceptions import WmataApiException
from src.wmata_api.core.rest_adapter import RestAdapter
from typing import TypeVar, Callable, List, Dict

T = TypeVar('T')

class WmataApiModule:
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

    def _get_and_parse_list(self, url, key: str, parser: Callable[[Dict], T], params: Dict = None) -> List[T]:
        result = self._rest_adapter.get(url, params)
        items = result.data.get(key)
        if items is None:
            self._logger.error(f"Missing key '{key}' in response from {url}")
            raise WmataApiException(f"Response missing expected key: {key}")

        if not isinstance(items, list):
            self._logger.error("Expected a list of items to parse, got: %s", type(items).__name__)
            raise WmataApiException("Invalid input: Expected a list of items.")

        parsed = []

        for i, item in enumerate(items):
            try:
                parsed.append(parser(item))
            except Exception as e:
                self._logger.error(f"Failed to parse {item} at index {i}: {e}")
                raise WmataApiException("Failed to parse JSON list.") from e

        return parsed

    def _get_and_parse_object(self, url, parser: Callable[[Dict], T], params: Dict = None) -> T:
        result = self._rest_adapter.get(url, params)

        try:
            obj = parser(result.data)
            return obj
        except Exception as e:
            self._logger.error(f"Failed to parse {result.data} returned from {url} with {parser.__name__}")
            raise WmataApiException(f"Failed to parse {result.data} returned from {url}") from e