
def convert(fromUnit, toUnit, value):
    """
    Converts between Fahrenheit, Celsius and Kelvin, and
    Converts between Miles, Yards and Meters.

    :param fromUnit:
    :param toUnit:
    :param value:
    :return:
    """
    if fromUnit.upper() == 'Celsius' and toUnit.upper() == 'Kelvin':
        return value + 273.15
    # TODO: implement the rest of the temperature conversions
    # TODO: implement the rest of the distance conversions
