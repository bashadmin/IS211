from conversions import convertCelsiusToKelvin

def test_convertCelsiusToKelvin():
    assert convertCelsiusToKelvin(0) == 273.15
    assert convertCelsiusToKelvin(-40) == 233.15 # should throw an error, comment this out if you want the tests to pass.
    assert convertCelsiusToKelvin(100) == 373.15
    assert convertCelsiusToKelvin(-273.15) == 0

test_convertCelsiusToKelvin()
