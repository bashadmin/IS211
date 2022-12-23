CONVERSION_FACTORS = {
    ("celsius", "kelvin"): lambda x: x + 273.15,
    ("celsius", "fahrenheit"): lambda x: (x * 1.8) + 32,
    ("fahrenheit", "celsius"): lambda x: (x - 32) * 5 / 9,
    ("fahrenheit", "kelvin"): lambda x: (x + 459.67) * 5/9,
    ("kelvin", "celsius"): lambda x: x - 273.15,
    ("kelvin", "fahrenheit"): lambda x: (x * 9/5 ) - 459.67,
    ("miles", "yards"): lambda x: x * 1760.0,
    ("miles", "meters"): lambda x: x * 1604.344,
    ("yards", "meters"): lambda x: x * 0.9144,
    ("yards", "miles"): lambda x: x / 1760.0,
    ("meters", "miles"): lambda x: x * 0.000621,
    ("meters", "yards"): lambda x: x * 1.0936,
}

def convert(from_unit, to_unit, value): 
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    value = float(value)
    if from_unit == to_unit:
        return value
    try:
        conversion_factor = CONVERSION_FACTORS[(from_unit, to_unit)]
    except KeyError:
        raise ConversionsNotPossible(
            "Conversion not possible between {} and {}".format(from_unit, to_unit)
        )
    return round(conversion_factor(value), 2)

# Use a dictionary to store the conversion factors, rather than using a series of if statements. This will make the code easier to read and maintain, and will allow you to easily add new units and conversions. For example:

# Use more descriptive variable names. For example, you could rename fromUnit and toUnit to from_unit and to_unit respectively, and value to value_to_convert.

# Remove the round function from the convert function,