from data_expectations.errors import ExpectationNotMetError
from data_expectations.errors import ExpectationNotUnderstoodError


def evaluate_record(expectations, record, suppress_errors: bool = False):
    full_suite = expectations._available_expectations()
    for expectation in expectations.set_of_expectations:
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


def evaluate_list(expectations, dictset, suppress_errors: bool = False):
    for record in dictset:
        result = evaluate_record(expectations, record, suppress_errors)
        if not result:
            return False
    return True
