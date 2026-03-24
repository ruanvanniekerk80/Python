from Page_217 import get_city_country

def test_city_country():
    result = get_city_country("Santiago", "Chile")
    assert result == "Santiago, Chile"
def test_city_country_population():
    """Verify we can include a population value."""
    formatted_name = get_city_country('santiago', 'chile', population=5000000)
    assert formatted_name == 'Santiago, Chile - population 5000000'