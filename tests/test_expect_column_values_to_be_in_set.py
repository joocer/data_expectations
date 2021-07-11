import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from rich import traceback

traceback.install()


def test_expect_column_values_to_be_in_set():

    test_func = de.Expectations([]).expect_column_values_to_be_in_set

    assert test_func(row={"key": "a"}, column="key", symbols=('a','b','c'))
    assert test_func(row={"key": None}, column="key", symbols=('a','b','c'))
    assert not test_func(row={"key": "g"}, column="key", symbols=('a','b','c'))

    assert test_func(row={"key": 1}, column="key", symbols=(1,2,3))
    assert test_func(row={"key": None}, column="key", symbols=(1,2,3))
    assert not test_func(row={"key": 8}, column="key", symbols=(1,2,3))

if __name__ == "__main__":

    test_expect_column_values_to_be_in_set()

    print("test manually run")
