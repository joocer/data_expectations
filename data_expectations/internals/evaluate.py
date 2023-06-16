# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing

from data_expectations.errors import ExpectationNotMetError
from data_expectations.errors import ExpectationNotUnderstoodError
from data_expectations.internals.expectations import all_expectations

ALL_EXPECTATIONS = all_expectations()


def evaluate_record(expectations, record: dict, suppress_errors: bool = False):
    """
    Test 'record' against a defined set of 'expectations'.
    """
    for expectation in expectations.set_of_expectations:
        if expectation["expectation"] not in ALL_EXPECTATIONS:
            raise ExpectationNotUnderstoodError(expectation=expectation["expectation"])

        if not ALL_EXPECTATIONS[expectation["expectation"]](row=record, **expectation):
            if not suppress_errors:
                raise ExpectationNotMetError(expectation["expectation"], record)
            return False  # data failed to meet expectation

    return True


def evaluate_list(expectations, dictset: typing.Iterable[dict], suppress_errors: bool = False):
    """
    Execute the expectation test against an iterable of dictionaries
    """
    for record in dictset:
        result = evaluate_record(expectations, record, suppress_errors)
        if not result:
            return False
    return True
