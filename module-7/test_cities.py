#Brett Fuller
#11/30/2024
#CSD 325  – Assignment 7.2
from city_functions import formatCityCountry

def test_city_country():
    """DO cites and countries like 'Santiago Chile' work?"""
    formattedCityCountry = formatCityCountry("Santiago", "Chile")
    assert formattedCityCountry == "Santiago, Chile"
