import os
import sys


sys.path.insert(1, os.path.join(sys.path[0], ".."))

from data_expectations import Expectation, Behaviors


def test_test_value_test():
    expect = Expectation(Behaviors.EXPECT_COLUMN_VALUES_LENGTH_TO_BE, column="value", config={"length": 5})
    assert expect.test_value("12345")
    assert not expect.test_value("")
    assert expect.test_value(None)


if __name__ == "__main__":  # pragma: no cover
    test_test_value_test()

    print("✅ okay")
