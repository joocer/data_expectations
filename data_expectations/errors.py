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


class ExpectationNotMetError(Exception):
    """Represents with an expection has failed to have been met"""

    def __init__(self, expectation, record):
        self.expectation = expectation
        self.record = record

        message = f"Record didn't meet expectations `{expectation}` ({str(record)})"
        super().__init__(message)


class ExpectationNotUnderstoodError(Exception):
    """Represents when an expectation isn't understood"""

    def __init__(self, expectation):
        self.expectation = expectation

        message = f"Expectation not understood `{expectation}`"
        super().__init__(message)
