<img src="icon.png" height="84px" />

## data_expectations  
_Is your data meeting your expectations?_

----

~~~diff
Data Expectations is in Alpha - interface and usage patterns are being stablized
~~~

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/joocer/data_expectations/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-yellowgreen)](https://github.com/joocer/data_expectations)
[![Regression Suite](https://github.com/joocer/data_expectations/actions/workflows/regression_suite.yaml/badge.svg)](https://github.com/joocer/data_expectations/actions/workflows/regression_suite.yaml)
[![Static Analysis](https://github.com/joocer/data_expectations/actions/workflows/static_analysis.yml/badge.svg)](https://github.com/joocer/data_expectations/actions/workflows/static_analysis.yml)
[![codecov](https://codecov.io/gh/joocer/data_expectations/branch/main/graph/badge.svg?token=XA60LUVH0W)](https://codecov.io/gh/joocer/data_expectations)
[![Downloads](https://pepy.tech/badge/data-expectations)](https://pepy.tech/project/data-expectations)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI Latest Release](https://img.shields.io/pypi/v/data-expectations.svg)](https://pypi.org/project/data-expectations/)

A delarative approach to asserting qualities of your datasets. Instead of tests like
`is_sorted` to determine if a column is ordered, the expectation is
`column_values_are_increasing`. Most of the time you don't need to know _how_ it got
like that, you are only interested _what_ the data looks like.

Expectations can be used alongside, or in place of a schema validator, however they
are not intended to perform validation of the data in a dataset, not just the structure
of a table. 

## Expectations

- expect_column_to_exist
- expect_column_names_to_match_set
- expect_column_values_to_not_be_null
- expect_column_values_to_be_of_type
- expect_column_values_to_be_in_type_list
- expect_column_values_to_be_between
- expect_column_values_to_be_increasing
- expect_column_values_to_be_decreasing
- expect_column_values_to_be_in_set
- expect_column_values_to_match_regex
- expect_column_values_to_match_like
- expect_column_values_length_to_be_be
- expect_column_values_length_to_be_between

## Install

~~~
pip install data_expectations
~~~

> if data doesn't match, I'm not angry, I'm just disappointed.