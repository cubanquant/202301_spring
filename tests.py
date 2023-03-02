import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit

from conversions_refactored import convert


class ConversionsCheck(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        value = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)

    def test_convertCelsiusToKelvin_2(self):
        value = convertCelsiusToKelvin(300.)
        expected = 573.15
        self.assertAlmostEqual(value, expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        value = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertAlmostEqual(value, expected, places=2)

    def test_convertCelsiusToFahrenheit_2(self):
        value = convertCelsiusToKelvin(300.)
        expected = 572.0
        self.assertAlmostEqual(value, expected, places=2)

    # TODO: Add tests for the new functions to convert F to C and F to K

    def test_convert_CelsiusToKelvin(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)

    # TODO: Add tests for the new functions to convert temperatures and distances


if __name__ == '__main__':
    unittest.main()
