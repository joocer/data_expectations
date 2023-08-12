import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import data_expectations as de


def test_expect_column_names_to_match_set():
    test_func = de.Expectations.expect_column_names_to_match_set

    assert test_func(row={"number": 7, "string": "d"}, columns=("number", "string"))
    assert test_func(
        row={"number": 7, "string": "d"},
        columns=("number", "string"),
        ignore_excess=True,
    )
    assert test_func(
        row={"number": 7, "string": "d"},
        columns=("number", "string"),
        ignore_excess=False,
    )

    assert test_func(row={"number": 7}, columns=("number", "string"))
    assert test_func(row={"number": 7}, columns=("number", "string"), ignore_excess=True)
    assert not test_func(row={"number": 7}, columns=("number", "string"), ignore_excess=False)


if __name__ == "__main__":  # pragma: no cover
    test_expect_column_names_to_match_set()
    print("✅ okay")
