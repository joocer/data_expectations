"""
Expectation: Column Values Are Increasing
"""
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from rich import traceback

traceback.install()


# fmt:off
VALID_DATA = [
    { "number": 1, "string": "a" },
    { "number": 3, "string": "b" },
    { "number": 5, "string": "c" },
    { "number": 7, "string": "d" },
]

VALID_DATA_SPARSE = [
    { "number": 1, "string": "a" },
    { "number": None, "string": None },
    { "number": 5, "string": "c" },
    { "number": 7, "string": "d" },
]

INVALID_DATA = [
    { "number": 7, "string": "d" },
    { "number": 5, "string": "c" },
    { "number": 3, "string": "b" },
    { "number": 1, "string": "a" },
]

INVALID_DATA_SPARSE = [
    { "number": 7, "string": "d" },
    { "number": 5, "string": "c" },
    { "number": None, "string": None },
    { "number": 1, "string": "a" },
]
# fmt:on


def test_expect_column_values_to_be_increasing_valid():

    test_func = de.Expectations([]).expect_column_values_to_be_increasing

    # valid data is always valid
    for row in VALID_DATA:
        assert test_func(row=row, column="number")
        assert test_func(row=row, column="string")


def test_expect_column_values_to_be_increasing_valid_with_nulls():

    test_func = de.Expectations([]).expect_column_values_to_be_increasing

    # valid data is always valid
    for row in VALID_DATA_SPARSE:
        assert test_func(row=row, column="number")
        assert test_func(row=row, column="string")

def test_expect_column_values_to_be_increasing_valid_with_nulls_which_arent_ignored():

    test_func = de.Expectations([]).expect_column_values_to_be_increasing

    for i, row in enumerate(VALID_DATA_SPARSE):
        if i in (1,):
            assert not test_func(row=row, column="number", ignore_nulls=False)
            assert not test_func(row=row, column="string", ignore_nulls=False)
        else:
            assert test_func(row=row, column="number", ignore_nulls=False)
            assert test_func(row=row, column="string", ignore_nulls=False)


def test_expect_column_values_to_be_increasing_invalid():

    test_func = de.Expectations([]).expect_column_values_to_be_increasing

    # invalid data is valid the first cycle
    for i, row in enumerate(INVALID_DATA):
        if i == 0:
            assert test_func(row=row, column="number")
            assert test_func(row=row, column="string")
        else:
            assert not test_func(row=row, column="number")
            assert not test_func(row=row, column="string")

def test_expect_column_values_to_be_increasing_invalid_with_nulls():

    test_func = de.Expectations([]).expect_column_values_to_be_increasing

    # invalid data is valid the first cycle
    for i, row in enumerate(INVALID_DATA_SPARSE):
        if i in (0,2):
            assert test_func(row=row, column="number")
            assert test_func(row=row, column="string")
        else:
            assert not test_func(row=row, column="number")
            assert not test_func(row=row, column="string")


if __name__ == "__main__":

    test_expect_column_values_to_be_increasing_valid()
    test_expect_column_values_to_be_increasing_valid_with_nulls()
    test_expect_column_values_to_be_increasing_valid_with_nulls_which_arent_ignored()
    test_expect_column_values_to_be_increasing_invalid()
    test_expect_column_values_to_be_increasing_invalid_with_nulls()

    print("test manually run")