from Page_217 import city_country

def test_city_country():
    result = city_country("santigo", "chile")
    assert result == "santiago, chile"
    