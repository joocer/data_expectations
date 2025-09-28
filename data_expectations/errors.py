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

from typing import Any
from typing import Dict
from typing import Optional


class ExpectationNotMetError(Exception):
    """Raised when an expectation has failed to be met."""

    def __init__(self, expectation: str, record: Dict[str, Any], details: Optional[str] = None):
        self.expectation = expectation
        self.record = record
        self.details = details

        base_message = f"Record didn't meet expectation '{expectation}'"
        if details:
            base_message += f": {details}"

        # Truncate very long records for readability
        record_str = str(record)
        if len(record_str) > 200:
            record_str = record_str[:200] + "..."

        message = f"{base_message}\nRecord: {record_str}"
        super().__init__(message)


class ExpectationNotUnderstoodError(Exception):
    """Raised when an expectation isn't understood or recognized."""

    def __init__(self, expectation: str, available_expectations: Optional[list] = None):
        self.expectation = expectation
        self.available_expectations = available_expectations or []

        message = f"Expectation not understood: '{expectation}'"
        if available_expectations:
            # Show some suggestions
            suggestions = [exp for exp in available_expectations if expectation.lower() in exp.lower()]
            if suggestions:
                message += f"\nDid you mean one of: {suggestions[:3]}"
            else:
                message += f"\nAvailable expectations: {available_expectations[:5]}"
                if len(available_expectations) > 5:
                    message += f" (and {len(available_expectations) - 5} more)"

        super().__init__(message)
