import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import data_expectations as de


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
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    de.Expectations.reset()

    # valid data is always valid
    for row in VALID_DATA:
        assert test_func(row=row, column="number")
        assert test_func(row=row, column="string")


def test_expect_column_values_to_be_decreasing_valid_with_nulls():
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    de.Expectations.reset()

    # valid data is always valid
    for row in VALID_DATA_SPARSE:
        assert test_func(row=row, column="number")
        assert test_func(row=row, column="string")


def test_expect_column_values_to_be_decreasing_valid_with_nulls_which_arent_ignored():
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    de.Expectations.reset()

    for i, row in enumerate(VALID_DATA_SPARSE):
        if i in (2,):
            assert not test_func(row=row, column="number", ignore_nulls=False)
            assert not test_func(row=row, column="string", ignore_nulls=False)
        else:
            assert test_func(row=row, column="number", ignore_nulls=False)
            assert test_func(row=row, column="string", ignore_nulls=False)


def test_expect_column_values_to_be_decreasing_invalid():
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    de.Expectations.reset()

    # invalid data is valid the first cycle
    for i, row in enumerate(INVALID_DATA):
        if i == 0:
            assert test_func(row=row, column="number")
            assert test_func(row=row, column="string")
        else:
            assert not test_func(row=row, column="number")
            assert not test_func(row=row, column="string")


def test_expect_column_values_to_be_decreasing_invalid_with_nulls():
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    de.Expectations.reset()

    # invalid data is valid the first cycle
    for i, row in enumerate(INVALID_DATA_SPARSE):
        if i in (0, 1):
            assert test_func(row=row, column="number")
            assert test_func(row=row, column="string")
        else:
            assert not test_func(row=row, column="number")
            assert not test_func(row=row, column="string")


def test_expect_column_values_to_be_decreasing_true():
    # Scenario where the column value is decreasing
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    record1 = {"column_name": 10}
    record2 = {"column_name": 5}

    assert test_func(row=record1, column="column_name", previous_value=15)
    assert test_func(row=record2, column="column_name", previous_value=10)


def test_expect_column_values_to_be_decreasing_false():
    # Scenario where the column value is not decreasing
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    record = {"column_name": 15}

    assert not test_func(row=record, column="column_name", previous_value=10)


def test_expect_column_values_to_be_decreasing_with_null():
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    # Scenario where the column value is null
    record = {"column_name": None}

    assert test_func(row=record, column="column_name", ignore_nulls=True, previous_value=10)
    assert not test_func(row=record, column="column_name", ignore_nulls=False, previous_value=10)


def test_expect_column_values_to_be_decreasing_no_previous_value():
    # Scenario where there's no previous value (first row in a dataset, for example)
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    record = {"column_name": 10}

    assert test_func(row=record, column="column_name", previous_value=None)


def test_expect_column_values_to_be_decreasing_column_missing():
    # Scenario where the column is missing
    test_func = de.Expectations.expect_column_values_to_be_decreasing
    record = {"other_column": 5}

    assert test_func(row=record, column="column_name", previous_value=10)


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_to_be_decreasing_valid()
    test_expect_column_values_to_be_decreasing_valid_with_nulls()
    test_expect_column_values_to_be_decreasing_valid_with_nulls_which_arent_ignored()
    test_expect_column_values_to_be_decreasing_invalid()
    test_expect_column_values_to_be_decreasing_invalid_with_nulls()

    test_expect_column_values_to_be_decreasing_column_missing()
    test_expect_column_values_to_be_decreasing_false()
    test_expect_column_values_to_be_decreasing_true()
    test_expect_column_values_to_be_decreasing_no_previous_value()
    test_expect_column_values_to_be_decreasing_with_null()

    print("✅ okay")
