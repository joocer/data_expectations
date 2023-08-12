import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import data_expectations as de


def test_expect_column_values_to_match_like():
    test_func = de.Expectations.expect_column_values_to_match_like

    assert test_func(row={"string": "surname"}, column="string", like="%name")
    assert not test_func(row={"string": "main"}, column="string", like="%name")
    assert test_func(row={"string": None}, column="string", like="%name")
    assert not test_func(row={"string": None}, column="string", like="%name", ignore_nulls=False)


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_values_to_match_like()
    print("✅ okay")
