import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from rich import traceback

traceback.install()


def test_expect_column_values_to_be_in_type_list():
    test_func = de.Expectations([]).expect_column_values_to_be_in_type_list

    assert test_func(row={"key": "value"}, column="key", type_list=["str", "int"])
    assert test_func(row={"key": 10}, column="key", type_list=["str", "int"])
    assert not test_func(row={"key": 10}, column="key", type_list=["str", "bool"])

    assert test_func(row={"key": None}, column="key", type_list=["str", "int"], ignore_nulls=True)
    assert test_func(row={}, column="key", type_list=["str", "int"], ignore_nulls=True)


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_to_be_in_type_list()
    print("✅ okay")
