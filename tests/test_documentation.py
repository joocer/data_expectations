# test the example in the documentation
# there are no assertions, we are ensuring it runs without error

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))


def test_example():

    import data_expectations as de

    TEST_DATA = {"name": "charles", "age": 12}

    set_of_expectations = [
        {"expectation": "expect_column_to_exist", "column": "name"},
        {"expectation": "expect_column_to_exist", "column": "age"},
        {
            "expectation": "expect_column_values_to_be_between",
            "column": "age",
            "minimum": 0,
            "maximum": 120,
        },
    ]

    expectations = de.Expectations(set_of_expectations)
    try:
        de.evaluate_record(expectations, TEST_DATA)
    except de.errors.ExpectationNotMetError:
        print("Data Didn't Meet Expectations")


if __name__ == "__main__":
    test_example()
    print("✅ okay")
