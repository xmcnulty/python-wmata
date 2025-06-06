import logging
from typing import TypeVar, List, Callable, Dict

from wmata_api.core.exceptions import WmataApiException

T = TypeVar('T')

class Parsing:
    @staticmethod
    def parse_list(items: Dict, parser: Callable[[Dict], T], logger: logging.Logger) -> List[T]:
        if not isinstance(items, list):
            logger.error("Expected a list of items to parse, got: %s", type(items).__name__)
            raise WmataApiException("Invalid input: Expected a list of items.")

        parsed = []

        for i, item in enumerate(items):
            try:
                parsed.append(parser(item))
            except Exception as e:
                logger.error(f"Failed to parse {item} at index {i}: {e}")
                raise WmataApiException("Failed to parse JSON list.") from e

        return parsed