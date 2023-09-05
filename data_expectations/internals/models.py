# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
    """
    Represents a general Data Expectation.
    """

    expectation: str
    config: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Expectation instance to a dictionary representation.

        Returns:
            A dictionary containing the expectation and its configuration.
        """
        return {"expectation": self.expectation, **self.config}

    @classmethod
    def load_base(cls: Type["Expectation"], serialized: Union[Dict[str, Any], str]) -> Dict[str, Any]:
        """
        Loads a serialized Expectation and returns it as a dictionary.

        Parameters:
            serialized: Serialized Expectation as a dictionary or JSON string.

        Returns:
            A dictionary representation of the serialized Expectation.
        """
        if isinstance(serialized, str):
            serialized = dict(json.loads(serialized))
        serialized_copy: dict = deepcopy(serialized)
        if "expectation" not in serialized_copy:
            raise ValueError("Missing 'expectation' key in Expectation.")
        return serialized_copy

    @classmethod
    def load(cls: Type["Expectation"], serialized: Union[Dict[str, Any], str]) -> "Expectation":
        """
        Loads a serialized Expectation and returns it as an instance.

        Parameters:
            serialized: Serialized Expectation as a dictionary or JSON string.

        Returns:
            An Expectation instance populated with the serialized data.
        """
        serialized_copy = cls.load_base(serialized)
        expectation = serialized_copy.pop("expectation")
        config = serialized_copy
        return cls(expectation=expectation, config=config)


class ColumnExpectation(Expectation):
    """
    Represents a Data Expectation related to a specific column.
    """

    def __init__(self, expectation: str, column: str, config: Dict[str, Any] = None):
        """
        Initializes a ColumnExpectation instance.

        Parameters:
            expectation: The expectation type as a string.
            column: The column the expectation applies to.
            config: Additional configuration as a dictionary.
        """
        super().__init__(expectation, config or {})
        self.column = column

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the ColumnExpectation instance to a dictionary representation.

        Returns:
            A dictionary containing the expectation, column, and its configuration.
        """
        return {"expectation": self.expectation, "column": self.column, **self.config}

    @classmethod
    def load(cls: Type["ColumnExpectation"], serialized: Union[Dict[str, Any], str]) -> "ColumnExpectation":
        """
        Loads a serialized ColumnExpectation and returns it as an instance.

        Parameters:
            serialized: Serialized ColumnExpectation as a dictionary or JSON string.

        Returns:
            A ColumnExpectation instance populated with the serialized data.
        """
        serialized_copy = cls.load_base(serialized)
        if "column" not in serialized_copy:
            raise ValueError("Missing 'column' key in Expectation.")
        expectation = serialized_copy.pop("expectation")
        column = serialized_copy.pop("column")
        config = serialized_copy
        return cls(expectation=expectation, column=column, config=config)
