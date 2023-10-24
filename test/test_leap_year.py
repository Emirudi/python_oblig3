import pytest

from python_oblig3 import leap_year
''
from python_oblig3.leap_year import LeapYear

# testfixture for å kunne bruke leap_year som parameter
@pytest.fixture()
def leap_year():
    return LeapYear


# Sjekket at alle testene feilet først ved å putte inn tall som jeg forventet at skulle feile.

# Kan deles på 4 men ikke på 100
def test_is_divided_by_4_but_not_100(leap_year):
    year_checker = leap_year(2004)
    assert year_checker.is_leap_year() is False


# Kan deles på 400
def test_is_divided_by_400(leap_year):
    year_checker = leap_year(2000)
    assert year_checker.is_leap_year() is True


# Skuddår når det deles på 4
def test_is_divided_by_4(leap_year):
    year_checker = leap_year(1717)
    assert year_checker.is_leap_year() is False


# Kan deles på 100, men ikke 400
def test_is_divided_by_100_but_not_400(leap_year):
    year_checker = leap_year(3000)
    assert year_checker.is_leap_year() is False


# Kan ikke deles på 4000
def test_is_not_divided_by_4000(leap_year):
    year_checker = leap_year(4000)
    assert year_checker.is_leap_year() is False
