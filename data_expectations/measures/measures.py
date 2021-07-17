from typing import Any
from pydantic import BaseModel  # type:ignore


class Measures(BaseModel):
    minimum: Any = None
    maximum: Any = None
    count: int = 0
    missing: int = 0
    cummulative_sum: float = 0

    unqiue_items: int = 0
    unique_list: dict = {}
