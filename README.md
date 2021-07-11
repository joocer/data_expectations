<img src="icon.png" height="84px" />

**data_expectations**  
Is your data meeting your expectations?

----

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/joocer/data_expectations/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-yellowgreen)](https://github.com/joocer/data_expectations)
[![Regression Suite](https://github.com/joocer/data_expectations/actions/workflows/regression_suite.yaml/badge.svg)](https://github.com/joocer/data_expectations/actions/workflows/regression_suite.yaml)
[![Static Analysis](https://github.com/joocer/data_expectations/actions/workflows/static_analysis.yml/badge.svg)](https://github.com/joocer/data_expectations/actions/workflows/static_analysis.yml)

A delarative approach to asserting qualities of your datasets. Instead of a test such
as `is_sorted` to determine if a column is ordered, the expectation is
`column_values_are_increasing`. Most of the time you don't need to know _how_ it got
like that, you are only interested _what_ the data looks like.


> if data doesn't match, I'm not angry, I'm just disappointed.