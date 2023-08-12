"""
Expectation: Column To Exist
"""
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import data_expectations as de


def test_expect_column_values_to_not_be_null():
    test_func = de.Expectations.expect_column_values_to_not_be_null

    assert test_func(row={"key": "value"}, column="key")
    assert not test_func(row={"key": None}, column="key")
    assert not test_func(row={"key": "value"}, column="field")


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_to_not_be_null()
    print("✅ okay")
