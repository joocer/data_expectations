from enum import Enum


class Behaviors(str, Enum):
    EXPECT_COLUMN_TO_EXIST = "expect_column_to_exist"
    EXPECT_COLUMN_VALUES_TO_NOT_BE_NULL = "expect_column_values_to_not_be_null"
    EXPECT_COLUMN_VALUES_TO_BE_OF_TYPE = "expect_column_values_to_be_of_type"
    EXPECT_COLUMN_VALUES_TO_BE_IN_TYPE_LIST = "expect_column_values_to_be_in_type_list"
    EXPECT_COLUMN_VALUES_TO_BE_MORE_THAN = "expect_column_values_to_be_more_than"
    EXPECT_COLUMN_VALUES_TO_BE_LESS_THAN = "expect_column_values_to_be_less_than"
    EXPECT_COLUMN_VALUES_TO_BE_BETWEEN = "expect_column_values_to_be_between"
    EXPECT_COLUMN_VALUES_TO_BE_INCREASING = "expect_column_values_to_be_increasing"
    EXPECT_COLUMN_VALUES_TO_BE_DECREASING = "expect_column_values_to_be_decreasing"
    EXPECT_COLUMN_VALUES_TO_BE_IN_SET = "expect_column_values_to_be_in_set"
    EXPECT_COLUMN_VALUES_TO_MATCH_REGEX = "expect_column_values_to_match_regex"
    EXPECT_COLUMN_VALUES_TO_MATCH_LIKE = "expect_column_values_to_match_like"
    EXPECT_COLUMN_VALUES_LENGTH_TO_BE_BE = "expect_column_values_length_to_be_be"
    EXPECT_COLUMN_VALUES_LENGTH_TO_BE_BETWEEN = "expect_column_values_length_to_be_between"


from data_expectations.internals.expectations import Expectations
from data_expectations.internals.models import Expectation

from data_expectations.internals.evaluate import evaluate_list
from data_expectations.internals.evaluate import evaluate_record
