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

import logging
import typing
from typing import Dict, Any

from data_expectations import Expectations
from data_expectations import Behaviors
from data_expectations.errors import ExpectationNotMetError
from data_expectations.errors import ExpectationNotUnderstoodError

# Cache the expectations dictionary for better performance
_EXPECTATIONS_CACHE: Dict[str, Any] = {}


def _get_expectations() -> Dict[str, Any]:
    """Get cached expectations dictionary."""
    global _EXPECTATIONS_CACHE
    if not _EXPECTATIONS_CACHE:
        _EXPECTATIONS_CACHE = Expectations.all_expectations()
    return _EXPECTATIONS_CACHE


def evaluate_record(expectations: Expectations, record: dict, suppress_errors: bool = False) -> bool:
    """
    Test a single record against a defined set of expectations.

    Args:
        expectations: The Expectations instance.
        record: The dictionary record to be tested.
        suppress_errors: Whether to suppress expectation errors and return False instead.

    Returns:
        True if all expectations are met, False otherwise.

    Raises:
        ExpectationNotUnderstoodError: If an expectation is not recognized.
        ExpectationNotMetError: If an expectation fails and suppress_errors is False.
        TypeError: If record is not a dictionary.
    """
    all_expectations = _get_expectations()

    # Check for unknown expectations first (before type checking record)
    # This maintains backward compatibility with tests that rely on this behavior
    for expectation_definition in expectations.set_of_expectations:
        # get the name of the expectation - handle both Behaviors enum and string names
        expectation = expectation_definition.expectation
        if isinstance(expectation, Behaviors):
            expectation_name = expectation.value
        else:
            expectation_name = expectation

        if expectation_name not in all_expectations:
            available = list(all_expectations.keys())
            raise ExpectationNotUnderstoodError(expectation_name, available)

    # Now check record type
    if not isinstance(record, dict):
        if not suppress_errors:
            raise TypeError(f"Record must be a dictionary, got {type(record)}")
        return False

    # Evaluate each expectation against the record
    for expectation_definition in expectations.set_of_expectations:
        expectation = expectation_definition.expectation
        if isinstance(expectation, Behaviors):
            expectation_name = expectation.value
        else:
            expectation_name = expectation

        base_config = {"row": record, "column": expectation_definition.column, **expectation_definition.config}

        try:
            result = all_expectations[expectation_name](**base_config)
            if not result:
                if not suppress_errors:
                    raise ExpectationNotMetError(expectation_name, record)
                return False  # data failed to meet expectation
        except Exception as e:
            if not suppress_errors:
                # Wrap unexpected errors with more context
                raise ExpectationNotMetError(expectation_name, record, str(e)) from e
            return False

    return True


def evaluate_list(expectations: Expectations, dictset: typing.Iterable[dict], suppress_errors: bool = False) -> bool:
    """
    Evaluate a set of records against a defined set of Expectations.

    Args:
        expectations: The Expectations instance.
        dictset: The iterable set of dictionary records to be tested.
        suppress_errors: Whether to suppress expectation errors and return False for the entire set.

    Returns:
        True if all records meet all Expectations, False otherwise.

    Raises:
        ExpectationNotUnderstoodError: If an expectation is not recognized.
        ExpectationNotMetError: If an expectation fails and suppress_errors is False.
    """
    try:
        return all(evaluate_record(expectations, record, suppress_errors) for record in dictset)
    except (ExpectationNotUnderstoodError, ExpectationNotMetError):
        # Re-raise these specific errors even if suppress_errors is True
        # as they indicate configuration issues, not data validation issues
        raise
