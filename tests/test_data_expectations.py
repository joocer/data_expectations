import datetime
import os
import sys
import pytest

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from data_expectations.errors import ExpectationNotMetError, ExpectationNotUnderstoodError
from rich import traceback

traceback.install()

# fmt:off
set_of_expectations = [
    {"expectation": "expect_column_to_exist", "column": "string_field"},
    {"expectation": "expect_column_values_to_not_be_null", "column": "string_field"},
    {"expectation": "expect_column_values_to_be_of_type","column": "boolean_field","expected_type": "bool"},
    {"expectation": "expect_column_values_to_match_like", "column": "string_field", "like":"%"}
]

set_of_unmet_expectations = [
    {"expectation": "expect_column_to_exist", "column": "value"}
]

set_of_unknown_expectations = [
    {"expectation": "expect_better_behavior", "column": "value"}
]
# fmt:on


def test_expectation():

    TEST_DATA = {
        "string_field": "string",
        "integer_field": 100,
        "boolean_field": True,
        "date_field": datetime.datetime.today(),
        "other_field": ["abc"],
        "nullable_field": None,
        "list_field": ["a", "b", "c"],
        "enum_field": "RED",
    }

    passing_test = de.Expectations(set_of_expectations)
    assert de.evaluate_record(passing_test, TEST_DATA)

    failing_test = de.Expectations(set_of_unmet_expectations)
    assert not de.evaluate_record(failing_test, TEST_DATA, suppress_errors=True)

    with pytest.raises(ExpectationNotMetError):
        de.evaluate_record(failing_test, TEST_DATA, suppress_errors=False)

    unknown_test = de.Expectations(set_of_unknown_expectations)

    assert not de.evaluate_record(unknown_test, TEST_DATA, suppress_errors=True)

    with pytest.raises(ExpectationNotUnderstoodError):
        de.evaluate_record(unknown_test, TEST_DATA, suppress_errors=False)

    print(passing_test.metrics_collector.collector)


if __name__ == "__main__":  # pragma: no cover
    test_expectation()

    print("okay")
