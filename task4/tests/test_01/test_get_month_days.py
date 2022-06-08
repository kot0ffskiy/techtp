from simple_library_01.functions import get_month_days as get_month_day
from pytest import raises


def test_get_month_day():
    assert get_month_day(1930, 6) == 30
    assert get_month_day(2004, 2) == 29
    assert get_month_day(2007, 2) == 28
    assert get_month_day(2001, 11) == 30
    assert get_month_day(2001, 5) == 31
    with raises(AttributeError):
         get_month_day(2002, 1000)
