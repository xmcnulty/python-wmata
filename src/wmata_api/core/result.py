from typing import Any
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Result:
    """
    Result returned from RestAdapter.
    """
    status_code: int
    message: str = ''
    data: Any = field(default_factory=dict)
