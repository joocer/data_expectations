import os
import sys
import json


sys.path.insert(1, os.path.join(sys.path[0], ".."))

from data_expectations import Expectations, Expectation


def test_expectations_initializer():
    # Create expectations as different types

    col_exp1 = Expectation("expect_test_col", "col1", {"key1": "value1"})
    col_exp2_dict = {"expectation": "expect_test_col2", "column": "col2", "key2": "value2"}
    col_exp2 = Expectation.load(col_exp2_dict)
    col_exp3_json = json.dumps({"expectation": "expect_test_col3", "column": "col3", "key3": "value3"})
    col_exp3 = Expectation.load(json.loads(col_exp3_json))

    # Initialize Expectations class
    expectations = Expectations([col_exp1, col_exp2_dict, col_exp3_json])

    # Validate
    assert len(expectations.set_of_expectations) == 3

    assert isinstance(expectations.set_of_expectations[0], Expectation)
    assert isinstance(expectations.set_of_expectations[1], Expectation)
    assert isinstance(expectations.set_of_expectations[2], Expectation)


if __name__ == "__main__":  # pragma: no cover
    test_expectations_initializer()

    print("✅ okay")
