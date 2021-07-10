from ..errors import ExpectationNotMetError, ExpectationNotUnderstoodError


def evaluate_record(self, record, suppress_errors: bool = False):
    self.metrics_collector.add(record)
    full_suite = self._available_expectations()
    for expectation in self.set_of_expectations:
        if expectation["expectation"] in full_suite:
            if not full_suite[expectation["expectation"]](row=record, **expectation):
                if not suppress_errors:
                    raise ExpectationNotMetError(
                        f"{expectation['expectation']} - {record}"
                    )
                return False  # data failed to meet expectation
        else:
            if not suppress_errors:
                raise ExpectationNotUnderstoodError(expectation["expectation"])
            return False  # unknown expectation
    return True
