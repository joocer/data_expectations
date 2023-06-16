import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from rich import traceback

traceback.install()


def test_expect_column_values_length_to_be():
    test_func = de.Expectations([]).expect_column_values_length_to_be

    assert test_func(row={"string": "value"}, column="string", length=5)
    assert not test_func(row={"string": "main"}, column="string", length=5)
    assert test_func(row={"string": None}, column="string", length=5)
    assert not test_func(row={"string": None}, column="string", length=5, ignore_nulls=False)
    assert test_func(row={"list": ["a", "b", "c"]}, column="list", length=3)
    assert test_func(row={"num": 100}, column="num", length=3)


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_length_to_be()
    print("✅ okay")
