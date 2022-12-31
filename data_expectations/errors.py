"""
#nodoc - don't add to the documentation wiki
"""


class BaseException(Exception):
    def __call__(self, *args):  # pragma: no cover
        return self.__class__(*(self.args + args))


class ExpectationNotMetError(BaseException):
    pass


class ExpectationNotUnderstoodError(BaseException):
    pass
