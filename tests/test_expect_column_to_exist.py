"""
Expectation: Column To Exist
"""

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import data_expectations as de


# fmt:off
DATA = [
    { "number": 7, "string": "d" },   # pass
    { "number": 5, "string": "c" },   # pass
    { "number": 3, "string": None },  # the column exists but is None - pass
    { "number": 1 },                  # fail
]
# fmt:on


def test_expect_column_to_exist():
    test_func = de.Expectations.expect_column_to_exist

    assert not test_func(row='{"number":1}', column="number")

    for i, row in enumerate(DATA):
        assert test_func(row=row, column="number"), row
        if i in (3,):
            assert not test_func(row=row, column="string"), row
        else:
            assert test_func(row=row, column="string"), row


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_to_exist()
    print("✅ okay")
