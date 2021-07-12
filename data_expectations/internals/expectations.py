"""
Inspired by the Great Expectations library.

Rather than testing for conformity through defining a schema, expectations are a set
of assertions we can apply to our data.

Whilst a schema-based approach isn't exactly procedural, expectations are a more
declarative way to define valid data.

These assertions can also define a schema (we can expect a set of columns, each with
an expected type), but they also allow us to have more complex assertions, such as
the values in a set of columns should add to 100, or the values in a column are
increasing.

This is designed to be applied to streaming data as each record passes through a point
in a flow - as such it is not intended to test an entire dataset at once to test its
validity, and some assertions are impractical - for example an expectation of the mean
of all of the values in a table.

To Be Added
* expect_column_values_to_be_more_than
* expect_column_values_to_be_less_than
* expect_column_a_value_to_be_more_than_column_b_value

* expect_table_row_count_to_be_less_than
* expect_table_row_count_to_be_more_than
* expect_table_row_count_to_be_between
* expect_table_row_count_to_be
* expect_column_values_to_be_unique


- if data doesn't match, I'm not cross, I'm just disappointed.
"""
import inspect
from functools import lru_cache
from typing import Any, Iterable
from .text import sql_like_to_regex, build_regex
from ..measures.collector import MeasuresCollector


class Expectations(object):
    def __init__(self, set_of_expectations: Iterable[dict]):
        self.set_of_expectations = set_of_expectations
        self.metrics_collector = MeasuresCollector()
        self._tracker: dict = {}

    ###################################################################################
    # COLUMN EXPECTATIONS
    ###################################################################################

    def expect_column_names_to_match_set(
        self,
        *,
        row: dict,
        columns: list,
        ignore_excess: bool = True,
        **kwargs,
    ):
        """
        Confirms that the columns in a record matches a given set.

        Ignore_excess, ignore columns not on the list, set to False to test against a
        fixed set.
        """
        if ignore_excess:
            return all(key in columns for key in row.keys())
        else:
            return sorted(columns) == sorted(list(row.keys()))

    def expect_column_to_exist(
        self,
        *,
        row: dict,
        column: str,
        **kwargs,
    ):
        """
        Confirms that a named column exists.

        Paramters:
            row: dictionary
                The dictionary to be tested
            column: string
                The name of the column we expect to exist

        Returns:
            True if the expectation is met
        """
        if isinstance(row, dict):
            return column in row.keys()
        return False

    def expect_column_values_to_not_be_null(
        self,
        *,
        row: dict,
        column: str,
        **kwargs,
    ):
        """
        Confirms the value in a column is not null, note that non-existant values
        are considered to be null.
        """
        return row.get(column) is not None

    def expect_column_values_to_be_of_type(
        self,
        *,
        row: dict,
        column: str,
        expected_type,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            return type(value).__name__ == expected_type
        return ignore_nulls

    def expect_column_values_to_be_in_type_list(
        self,
        *,
        row: dict,
        column: str,
        type_list: Iterable,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            return type(value).__name__ in type_list
        return ignore_nulls

    def expect_column_values_to_be_between(
        self,
        *,
        row: dict,
        column: str,
        minimum,
        maximum,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            return value >= minimum and value <= maximum
        return ignore_nulls

    def expect_column_values_to_be_increasing(
        self,
        *,
        row: dict,
        column: str,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            key = f"expect_column_values_to_be_increasing/{str(column)}"
            last_value = self._tracker.get(key)
            self._tracker[key] = value
            return last_value is None or last_value <= value
        return ignore_nulls

    def expect_column_values_to_be_decreasing(
        self,
        *,
        row: dict,
        column: str,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            key = f"expect_column_values_to_be_decreasing/{str(column)}"
            last_value = self._tracker.get(key)
            self._tracker[key] = value
            return last_value is None or last_value >= value
        return ignore_nulls

    def expect_column_values_to_be_in_set(
        self,
        *,
        row: dict,
        column: str,
        symbols: Iterable,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            return value in symbols
        return ignore_nulls

    def expect_column_values_to_match_regex(
        self,
        *,
        row: dict,
        column: str,
        regex: str,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            return build_regex(regex).match(str(value)) is not None
        return ignore_nulls

    def expect_column_values_to_match_like(
        self,
        *,
        row: dict,
        column: str,
        like: str,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            return sql_like_to_regex(like).match(str(value)) is not None
        return ignore_nulls

    def expect_column_values_length_to_be(
        self,
        *,
        row: dict,
        column: str,
        length: int,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        """Confirms the string length of the value in a column is a given length"""
        value = row.get(column)
        if value:
            if not hasattr(value, "__len__"):
                value = str(value)
            return len(value) == length
        return ignore_nulls

    def expect_column_values_length_to_be_between(
        self,
        *,
        row: dict,
        column: str,
        minimum: int,
        maximum: int,
        ignore_nulls: bool = True,
        **kwargs,
    ):
        value = row.get(column)
        if value:
            if not hasattr(value, "__len__"):
                value = str(value)
            return len(value) >= minimum and len(value) <= maximum
        return ignore_nulls

    @lru_cache(1)
    def _available_expectations(self):
        """
        Programatically get the list of expectations and build them into a dictionary.
        We then use this dictionary to look up the methods to test the expectations in
        the set of expectations for a dataset.
        """
        expectations = {}
        for handle, member in inspect.getmembers(self):
            if callable(member) and handle.startswith("expect_"):
                expectations[handle] = member
        return expectations
