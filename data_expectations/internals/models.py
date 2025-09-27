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

from data_expectations import Behaviors
from data_expectations.errors import ExpectationNotUnderstoodError


@dataclass
class Expectation:
    """
    Represents a general Data Expectation.

    This class encapsulates the configuration for a single data expectation,
    including the expectation type, target column, and any additional parameters.
    """

    expectation: Behaviors
    column: str
    config: Dict[str, Any] = field(default_factory=dict)
    ignore_nulls: bool = True

    def __post_init__(self):
        """Validate expectation configuration after initialization."""
        if not self.column:
            raise ValueError("Column name cannot be empty")

        # Only convert string to Behaviors enum if it's a valid Behaviors value
        # This allows for test cases and custom expectations to use string names
        if isinstance(self.expectation, str):
            try:
                self.expectation = Behaviors(self.expectation)
            except ValueError:
                # Leave as string if not a valid Behaviors enum - this maintains
                # backward compatibility and allows for test cases
                pass

    def dump(self) -> Dict[str, Any]:
        """
        Converts the Expectation instance to a dictionary representation.

        Returns:
            A dictionary containing the expectation and its configuration.

        Example:
            >>> exp = Expectation(Behaviors.EXPECT_COLUMN_TO_EXIST, "name")
            >>> exp.dump()
            {'expectation': 'expect_column_to_exist', 'column': 'name', 'ignore_nulls': True}
        """
        # Handle both Behaviors enum and string expectation names
        expectation_value = self.expectation.value if isinstance(self.expectation, Behaviors) else self.expectation
        return {
            "expectation": expectation_value,
            "column": self.column,
            "ignore_nulls": self.ignore_nulls,
            **self.config,
        }

    @classmethod
    def load(cls: Type["Expectation"], serialized: Union[Dict[str, Any], str]) -> "Expectation":
        """
        Loads a serialized Expectation and returns it as an instance.

        Args:
            serialized: Serialized Expectation as a dictionary or JSON string.

        Returns:
            An Expectation instance populated with the serialized data.

        Raises:
            ValueError: If required keys are missing or data is invalid.
            json.JSONDecodeError: If JSON string is malformed.

        Example:
            >>> data = {"expectation": "expect_column_to_exist", "column": "name"}
            >>> exp = Expectation.load(data)
            >>> exp.column
            'name'
        """
        if isinstance(serialized, str):
            try:
                serialized = dict(json.loads(serialized))
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON string: {e}") from e

        if not isinstance(serialized, dict):
            raise ValueError(f"Expected dict or JSON string, got {type(serialized)}")

        serialized_copy: dict = deepcopy(serialized)

        if "expectation" not in serialized_copy:
            raise ValueError("Missing required 'expectation' key in Expectation.")
        if "column" not in serialized_copy:
            raise ValueError("Missing required 'column' key in Expectation.")

        expectation = serialized_copy.pop("expectation")
        column = serialized_copy.pop("column")
        ignore_nulls = serialized_copy.pop("ignore_nulls", True)
        config = serialized_copy

        return cls(expectation=expectation, column=column, ignore_nulls=ignore_nulls, config=config)

    def test_value(self, value: Any) -> bool:
        """
        Test a single value against this expectation.

        Args:
            value: The value to be tested.

        Returns:
            True if the value meets the expectation, False otherwise.

        Raises:
            ExpectationNotUnderstoodError: If the expectation type is not recognized.

        Example:
            >>> exp = Expectation(Behaviors.EXPECT_COLUMN_VALUES_TO_BE_OF_TYPE,
            ...                  "age", config={"expected_type": "int"})
            >>> exp.test_value(25)
            True
        """
        from data_expectations import Expectations

        # Handle both Behaviors enum and string expectation names
        expectation_name = self.expectation.value if isinstance(self.expectation, Behaviors) else self.expectation
        test_logic = Expectations.all_expectations().get(expectation_name, None)
        if not test_logic:
            available = list(Expectations.all_expectations().keys())
            raise ExpectationNotUnderstoodError(expectation_name, available)

        return test_logic(row={"value": value}, column="value", ignore_nulls=self.ignore_nulls, **self.config)
