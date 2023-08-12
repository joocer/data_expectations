import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import data_expectations as de


def test_expect_column_values_to_be_between():
    test_func = de.Expectations.expect_column_values_to_be_between

    assert test_func(row={"key": "b"}, column="key", minimum="a", maximum="c")
    assert test_func(row={"key": "b"}, column="key", minimum="a", maximum="b")
    assert test_func(row={"key": "b"}, column="key", minimum="b", maximum="c")
    assert not test_func(row={"key": "g"}, column="key", minimum="a", maximum="c")

    assert test_func(row={"key": 2}, column="key", minimum=1, maximum=3)
    assert test_func(row={"key": 2}, column="key", minimum=1, maximum=2)
    assert test_func(row={"key": 2}, column="key", minimum=2, maximum=3)
    assert not test_func(row={"key": 10}, column="key", minimum=1, maximum=3)

    assert test_func(row={"key": None}, column="key", minimum="a", maximum="c")


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_to_be_between()
    print("✅ okay")
