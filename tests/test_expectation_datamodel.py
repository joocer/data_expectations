import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))


import json
import pytest
from data_expectations import Expectation, ColumnExpectation


def test_expectation_to_dict():
    exp = Expectation("test_expectation", {"some_key": "some_value"})
    assert exp.to_dict() == {"expectation": "test_expectation", "some_key": "some_value"}


def test_expectation_load_from_dict():
    serialized = {"expectation": "test_expectation", "some_key": "some_value"}
    exp = Expectation.load(serialized)
    assert exp.expectation == "test_expectation"
    assert exp.config == {"some_key": "some_value"}


def test_expectation_load_from_json_str():
    serialized = json.dumps({"expectation": "test_expectation", "some_key": "some_value"})
    exp = Expectation.load(serialized)
    assert exp.expectation == "test_expectation"
    assert exp.config == {"some_key": "some_value"}


def test_expectation_load_missing_key():
    serialized = {"some_key": "some_value"}
    with pytest.raises(ValueError):
        Expectation.load(serialized)


def test_column_expectation_to_dict():
    exp = ColumnExpectation("test_expectation", "test_column", {"some_key": "some_value"})
    assert exp.to_dict() == {"expectation": "test_expectation", "column": "test_column", "some_key": "some_value"}


def test_column_expectation_load_from_dict():
    serialized = {"expectation": "test_expectation", "column": "test_column", "some_key": "some_value"}
    exp = ColumnExpectation.load(serialized)
    assert exp.expectation == "test_expectation"
    assert exp.column == "test_column"
    assert exp.config == {"some_key": "some_value"}


def test_column_expectation_load_from_json_str():
    serialized = json.dumps({"expectation": "test_expectation", "column": "test_column", "some_key": "some_value"})
    exp = ColumnExpectation.load(serialized)
    assert exp.expectation == "test_expectation"
    assert exp.column == "test_column"
    assert exp.config == {"some_key": "some_value"}


def test_column_expectation_load_missing_key():
    serialized = {"expectation": "test_expectation", "some_key": "some_value"}
    with pytest.raises(ValueError):
        ColumnExpectation.load(serialized)


if __name__ == "__main__":  # pragma: no cover
    test_expectation_to_dict()
    test_expectation_load_from_dict()
    test_expectation_load_from_json_str()
    test_expectation_load_missing_key()

    test_column_expectation_to_dict()
    test_column_expectation_load_from_dict()
    test_column_expectation_load_from_json_str()
    test_column_expectation_load_missing_key()

    print("✅ okay")
