import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from rich import traceback

traceback.install()


def test_expect_column_values_length_to_be_between():
    test_func = de.Expectations([]).expect_column_values_length_to_be_between

    assert test_func(row={"string": "value"}, column="string", minimum=3, maximum=7)
    assert not test_func(row={"string": "main"}, column="string", minimum=5, maximum=7)
    assert test_func(row={"string": None}, column="string", minimum=5, maximum=7)
    assert not test_func(
        row={"string": None}, column="string", minimum=5, maximum=7, ignore_nulls=False
    )
    assert test_func(row={"list": ["a", "b", "c"]}, column="list", minimum=1, maximum=5)
    assert test_func(row={"num": 100}, column="num", minimum=1, maximum=7)


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_length_to_be_between()
    print("✅ okay")
