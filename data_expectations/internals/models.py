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
    """

    expectation: Behaviors
    column: str
    config: Dict[str, Any] = field(default_factory=dict)
    ignore_nulls: bool = True

    def dump(self) -> Dict[str, Any]:
        """
        Converts the Expectation instance to a dictionary representation.

        Returns:
            A dictionary containing the expectation and its configuration.
        """
        return {
            "expectation": self.expectation,
            "column": self.column,
            "ignore_nulls": self.ignore_nulls,
            **self.config,
        }

    @classmethod
    def load(cls: Type["Expectation"], serialized: Union[Dict[str, Any], str]) -> "Expectation":
        """
        Loads a serialized Expectation and returns it as an instance.

        Parameters:
            serialized: Serialized Expectation as a dictionary or JSON string.

        Returns:
            An Expectation instance populated with the serialized data.
        """
        if isinstance(serialized, str):
            serialized = dict(json.loads(serialized))
        serialized_copy: dict = deepcopy(serialized)
        if "expectation" not in serialized_copy:
            raise ValueError("Missing 'expectation' key in Expectation.")
        if "column" not in serialized_copy:
            raise ValueError("Missing 'column' key in Expectation.")
        expectation = serialized_copy.pop("expectation")
        column = serialized_copy.pop("column")
        ignore_nulls = serialized_copy.pop("ignore_nulls", True)
        config = serialized_copy
        return cls(expectation=expectation, column=column, ignore_nulls=ignore_nulls, config=config)

    def test_value(self, value: Any):
        """
        Test a single value against this expectation.

        Parameters:
            value: Any
                The value to be tested.
        """
        from data_expectations import Expectations

        test_logic = Expectations.all_expectations().get(self.expectation.value, None)
        if not test_logic:
            raise ExpectationNotUnderstoodError(expectation=self.expectation)
        return test_logic(row={"value": value}, column="value", ignore_nulls=self.ignore_nulls, **self.config)
