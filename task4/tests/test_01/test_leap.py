from simple_library_01.functions import is_leap
import pytest


def test_is_leap():
    assert is_leap(2004) is True
    assert is_leap(100) is False
    assert is_leap(1600) is True
    assert is_leap(201) is False
    with pytest.raises(AttributeError):
        is_leap(-1)