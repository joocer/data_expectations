import os
import sys
import json


sys.path.insert(1, os.path.join(sys.path[0], ".."))

from data_expectations import Expectations, Expectation, ColumnExpectation


def test_expectations_initializer():
    # Create expectations as different types
    exp1 = Expectation("expect_test", {"key1": "value1"})
    exp2_dict = {"expectation": "expect_test2", "key2": "value2"}
    exp2 = Expectation.load(exp2_dict)
    exp3_json = json.dumps({"expectation": "expect_test3", "key3": "value3"})
    exp3 = Expectation.load(json.loads(exp3_json))

    col_exp1 = ColumnExpectation("expect_test_col", "col1", {"key1": "value1"})
    col_exp2_dict = {"expectation": "expect_test_col2", "column": "col2", "key2": "value2"}
    col_exp2 = ColumnExpectation.load(col_exp2_dict)
    col_exp3_json = json.dumps({"expectation": "expect_test_col3", "column": "col3", "key3": "value3"})
    col_exp3 = ColumnExpectation.load(json.loads(col_exp3_json))

    # Initialize Expectations class
    expectations = Expectations([exp1, exp2_dict, exp3_json, col_exp1, col_exp2_dict, col_exp3_json])

    # Validate
    assert len(expectations.set_of_expectations) == 6

    assert isinstance(expectations.set_of_expectations[0], Expectation)
    assert isinstance(expectations.set_of_expectations[1], Expectation)
    assert isinstance(expectations.set_of_expectations[2], Expectation)
    assert isinstance(expectations.set_of_expectations[3], ColumnExpectation)
    assert isinstance(expectations.set_of_expectations[4], ColumnExpectation)
    assert isinstance(expectations.set_of_expectations[5], ColumnExpectation)


if __name__ == "__main__":  # pragma: no cover
    test_expectations_initializer()

    print("✅ okay")
