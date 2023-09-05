import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))


import json
import pytest
from data_expectations import Expectation


def test_column_expectation_to_dict():
    exp = Expectation("test_expectation", "test_column", {"some_key": "some_value"})
    assert exp.dump() == {
        "expectation": "test_expectation",
        "column": "test_column",
        "some_key": "some_value",
        "ignore_nulls": True,
    }


def test_column_expectation_load_from_dict():
    serialized = {"expectation": "test_expectation", "column": "test_column", "some_key": "some_value"}
    exp = Expectation.load(serialized)
    assert exp.expectation == "test_expectation"
    assert exp.column == "test_column"
    assert exp.config == {"some_key": "some_value"}
    assert exp.ignore_nulls == True


def test_column_expectation_load_from_json_str():
    serialized = json.dumps(
        {"expectation": "test_expectation", "column": "test_column", "some_key": "some_value", "ignore_nulls": False}
    )
    exp = Expectation.load(serialized)
    assert exp.expectation == "test_expectation"
    assert exp.column == "test_column"
    assert exp.config == {"some_key": "some_value"}
    assert exp.ignore_nulls == False


def test_column_expectation_load_missing_key():
    serialized = {"expectation": "test_expectation", "some_key": "some_value"}
    with pytest.raises(ValueError):
        Expectation.load(serialized)
    serialized = {"column": "column"}
    with pytest.raises(ValueError):
        Expectation.load(serialized)


if __name__ == "__main__":  # pragma: no cover
    test_column_expectation_to_dict()
    test_column_expectation_load_from_dict()
    test_column_expectation_load_from_json_str()
    test_column_expectation_load_missing_key()

    print("✅ okay")
