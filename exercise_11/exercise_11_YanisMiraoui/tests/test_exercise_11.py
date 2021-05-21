import logging
import pytest


class DummyError(Exception):
    pass


d = []


def info(msg):
    """Monkey-patch logging for testing."""
    d.append(msg)


logging.info = info

from groups.groups import Group, CyclicGroup, GeneralLinearGroup

try:
    from log_decorator.log_decorator import log_call
except ImportError:
    pass


@pytest.mark.e11_1
def test_import():
    from log_decorator import log_call


@pytest.mark.e11_1
def test_decorator():
    @log_call
    def foo(*args, **kwargs):
        pass

    foo("a", d="b", c=2)
    print(d)
    logmsg = d.pop()
    assert logmsg == "Calling: foo('a', d='b', c=2)"


@pytest.mark.e11_2
def test_logger_called():

    C = CyclicGroup(2)
    C(1)
    logmsg = d.pop()
    assert logmsg == "Calling: _validate(CyclicGroup(2), 1)"


@pytest.mark.e11_2
def test_logger_in_original_location():
    def _validate(self, value):
        raise DummyError

    Group._validate = _validate

    C = CyclicGroup(2)
    with pytest.raises(DummyError):
        C(1)
