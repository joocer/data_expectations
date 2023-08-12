import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import data_expectations as de


def test_expect_column_values_to_be_less_than():
    test_func = de.Expectations.expect_column_values_to_be_less_than

    assert test_func(row={"key": "b"}, column="key", threshold="c")
    assert test_func(row={"key": "b"}, column="key", threshold="f")
    assert test_func(row={"key": "banana"}, column="key", threshold="carrot")
    assert not test_func(row={"key": "g"}, column="key", threshold="c")

    assert test_func(row={"key": 2}, column="key", threshold=3)
    assert test_func(row={"key": 2.0}, column="key", threshold=77)
    assert test_func(row={"key": 2}, column="key", threshold=3)
    assert not test_func(row={"key": 10}, column="key", threshold=3)

    assert test_func(row={"key": None}, column="key", threshold="c")


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_to_be_less_than()
    print("✅ okay")
