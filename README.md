<img src="icon.png" height="92px" />

### Data Expectations  
_Are your data meeting your expectations?_

----

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/joocer/data_expectations/blob/main/LICENSE)
[![Regression Suite](https://github.com/joocer/data_expectations/actions/workflows/regression_suite.yaml/badge.svg)](https://github.com/joocer/data_expectations/actions/workflows/regression_suite.yaml)
[![Static Analysis](https://github.com/joocer/data_expectations/actions/workflows/static_analysis.yml/badge.svg)](https://github.com/joocer/data_expectations/actions/workflows/static_analysis.yml)
[![codecov](https://codecov.io/gh/joocer/data_expectations/branch/main/graph/badge.svg?token=XA60LUVH0W)](https://codecov.io/gh/joocer/data_expectations)
[![Downloads](https://pepy.tech/badge/data-expectations)](https://pepy.tech/project/data-expectations)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI Latest Release](https://img.shields.io/pypi/v/data-expectations.svg)](https://pypi.org/project/data-expectations/)

A delarative approach to asserting qualities of your datasets. Instead of tests like `is_sorted` to determine if a column is ordered, the expectation is `column_values_are_increasing`. Most of the time you don't need to know _how_ it got like that, you are only interested _what_ the data looks like.

Expectations can be used alongside, or in place of a schema validator, however Expectations is intended to perform validation of the data in a dataset, not just the structure of a table. 

## Expectations

- **expect_column_to_exist** (column)
- **expect_column_names_to_match_set** (columns, ignore_excess:true)
- **expect_column_values_to_not_be_null** (column)
- **expect_column_values_to_be_of_type** (column, expected_type, ignore_nulls:true)
- **expect_column_values_to_be_in_type_list** (column, type_list, ignore_nulls:true)
- **expect_column_values_to_be_more_than** (column, threshold, ignore_nulls:true)
- **expect_column_values_to_be_less_than** (column, threshold, ignore_nulls:true)
- **expect_column_values_to_be_between** (column, maximum, minimum, ignore_nulls:true)
- **expect_column_values_to_be_increasing** (column, ignore_nulls:true)
- **expect_column_values_to_be_decreasing** (column, ignore_nulls:true)
- **expect_column_values_to_be_in_set** (column, symbols, ignore_nulls:true)
- **expect_column_values_to_match_regex** (column, regex, ignore_nulls:true)
- **expect_column_values_to_match_like** (column, like, ignore_nulls:true)
- **expect_column_values_length_to_be_be** (column, length, ignore_nulls:true)
- **expect_column_values_length_to_be_between**  (column, maximum, minimum, ignore_nulls:true)

## Install

~~~bash
pip install data_expectations
~~~

Data Expectations has no external dependencies, can be used ad hoc and in-the-moment without complex set up.

## Example Usage

~~~python
import data_expectations as de

TEST_DATA = {"name":"charles","age":12}

set_of_expectations = [
    {"expectation": "expect_column_to_exist", "column": "name"},
    {"expectation": "expect_column_to_exist", "column": "age"},
    {"expectation": "expect_column_values_to_be_between", "column": "age", "minimum": 0, "maximum": 120},
]

expectations = de.Expectations(set_of_expectations)
try:
    de.evaluate_record(expectations, TEST_DATA)
except de.errors.ExpectationNotMetError:
    print("Data Didn't Meet Expectations")
~~~