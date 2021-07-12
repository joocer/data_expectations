import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
import data_expectations as de
from rich import traceback

traceback.install()


def test_expect_column_values_to_match_regex():

    test_func = de.Expectations([]).expect_column_values_to_match_regex

    assert test_func(row={"string": "test"}, column="string", regex="^test$")
    assert not test_func(row={"string": "main"}, column="string", regex="^test$")
    assert test_func(row={"string": None}, column="string", regex="^test$")
    assert not test_func(row={"string": None}, column="string", regex="^test$", ignore_nulls=False)
    

if __name__ == "__main__":  # pragma: no cover

    test_expect_column_values_to_match_regex()

    print("test manually run")
