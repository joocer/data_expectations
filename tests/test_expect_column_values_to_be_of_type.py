import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from rich import traceback

traceback.install()


def test_expect_column_values_to_be_of_type():

    test_func = de.Expectations([]).expect_column_values_to_be_of_type

    assert test_func(row={"key": "value"}, column="key", expected_type="str")
    assert not test_func(row={"key": 10}, column="key", expected_type="str")
    assert test_func(row={"key": 10}, column="key", expected_type="int")
    assert not test_func(row={"key": 10}, column="key", expected_type="str")

    assert test_func(row={"key": True}, column="key", expected_type="bool")
    assert test_func(row={"key": 0.1}, column="key", expected_type="float")

    assert test_func(row={"key": None}, column="key", expected_type="str", ignore_nulls=True)
    assert test_func(row={}, column="key", expected_type="str", ignore_nulls=True)


if __name__ == "__main__":

    test_expect_column_values_to_be_of_type()

    print("test manually run")