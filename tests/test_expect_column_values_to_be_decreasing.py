import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from rich import traceback

traceback.install()


# fmt:off
VALID_DATA = [
    { "number": 7, "string": "d" },
    { "number": 5, "string": "c" },
    { "number": 3, "string": "b" },
    { "number": 1, "string": "a" },
]

VALID_DATA_SPARSE = [
    { "number": 7, "string": "d" },
    { "number": 5, "string": "c" },
    { "number": None, "string": None },
    { "number": 1, "string": "a" },
]

INVALID_DATA = [
    { "number": 1, "string": "a" },
    { "number": 3, "string": "b" },
    { "number": 5, "string": "c" },
    { "number": 7, "string": "d" },
]

INVALID_DATA_SPARSE = [
    { "number": 1, "string": "a" },
    { "number": None, "string": None },
    { "number": 5, "string": "c" },
    { "number": 7, "string": "d" },
]
# fmt:on


def test_expect_column_values_to_be_decreasing_valid():

    test_func = de.Expectations([]).expect_column_values_to_be_decreasing

    # valid data is always valid
    for row in VALID_DATA:
        assert test_func(row=row, column="number")
        assert test_func(row=row, column="string")


def test_expect_column_values_to_be_decreasing_valid_with_nulls():

    test_func = de.Expectations([]).expect_column_values_to_be_decreasing

    # valid data is always valid
    for row in VALID_DATA_SPARSE:
        assert test_func(row=row, column="number")
        assert test_func(row=row, column="string")


def test_expect_column_values_to_be_decreasing_valid_with_nulls_which_arent_ignored():

    test_func = de.Expectations([]).expect_column_values_to_be_decreasing

    for i, row in enumerate(VALID_DATA_SPARSE):
        if i in (2,):
            assert not test_func(row=row, column="number", ignore_nulls=False)
            assert not test_func(row=row, column="string", ignore_nulls=False)
        else:
            assert test_func(row=row, column="number", ignore_nulls=False)
            assert test_func(row=row, column="string", ignore_nulls=False)


def test_expect_column_values_to_be_decreasing_invalid():

    test_func = de.Expectations([]).expect_column_values_to_be_decreasing

    # invalid data is valid the first cycle
    for i, row in enumerate(INVALID_DATA):
        if i == 0:
            assert test_func(row=row, column="number")
            assert test_func(row=row, column="string")
        else:
            assert not test_func(row=row, column="number")
            assert not test_func(row=row, column="string")


def test_expect_column_values_to_be_decreasing_invalid_with_nulls():

    test_func = de.Expectations([]).expect_column_values_to_be_decreasing

    # invalid data is valid the first cycle
    for i, row in enumerate(INVALID_DATA_SPARSE):
        if i in (0, 1):
            assert test_func(row=row, column="number")
            assert test_func(row=row, column="string")
        else:
            assert not test_func(row=row, column="number")
            assert not test_func(row=row, column="string")


if __name__ == "__main__":

    test_expect_column_values_to_be_decreasing_valid()
    test_expect_column_values_to_be_decreasing_valid_with_nulls()
    test_expect_column_values_to_be_decreasing_valid_with_nulls_which_arent_ignored()
    test_expect_column_values_to_be_decreasing_invalid()
    test_expect_column_values_to_be_decreasing_invalid_with_nulls()

    print("test manually run")
