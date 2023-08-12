import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import data_expectations as de


def test_expect_column_values_to_be_more_than():
    test_func = de.Expectations.expect_column_values_to_be_more_than

    assert test_func(row={"key": "b"}, column="key", threshold="a")
    assert test_func(row={"key": "z"}, column="key", threshold="f")
    assert test_func(row={"key": "watermelon"}, column="key", threshold="carrot")
    assert not test_func(row={"key": "c"}, column="key", threshold="g")

    assert test_func(row={"key": 1}, column="key", threshold=0)
    assert test_func(row={"key": 0.0}, column="key", threshold=-3.4)
    assert test_func(row={"key": 100.0}, column="key", threshold=3)
    assert not test_func(row={"key": 3}, column="key", threshold=10)

    assert test_func(row={"key": None}, column="key", threshold="c")


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_to_be_more_than()
    print("✅ okay")
