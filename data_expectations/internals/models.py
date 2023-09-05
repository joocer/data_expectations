import json
from copy import deepcopy
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Type
from typing import Union


@dataclass
class Expectation:
    expectation: str
    config: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {"expectation": self.expectation, **self.config}

    @classmethod
    def load(cls: Type["Expectation"], serialized: Union[Dict[str, Any], str]) -> "Expectation":
        if isinstance(serialized, str):
            serialized = dict(json.loads(serialized))

        serialized_copy: dict = deepcopy(serialized)

        if "expectation" not in serialized_copy:
            raise ValueError("Missing 'expectation' key in Expectation." + str(serialized_copy))

        expectation = serialized_copy.pop("expectation")
        config = serialized_copy

        return cls(expectation=expectation, config=config)


class ColumnExpectation(Expectation):
    def __init__(self, expectation: str, column: str, config: Dict[str, Any] = None):
        super().__init__(expectation, config if config is not None else {})
        self.column = column

    def to_dict(self) -> Dict[str, Any]:
        return {"expectation": self.expectation, "column": self.column, **self.config}

    @classmethod
    def load(cls: Type["ColumnExpectation"], serialized: Union[Dict[str, Any], str]) -> "ColumnExpectation":
        if isinstance(serialized, str):
            serialized = dict(json.loads(serialized))

        serialized_copy: dict = deepcopy(serialized)

        if "expectation" not in serialized_copy:
            raise ValueError("Missing 'expectation' key in Expectation")
        if "column" not in serialized_copy:
            raise ValueError("Missing 'column' key in Expectation")

        expectation = serialized_copy.pop("expectation")
        column = serialized_copy.pop("column")
        config = serialized_copy
        return cls(expectation=expectation, column=column, config=config)
