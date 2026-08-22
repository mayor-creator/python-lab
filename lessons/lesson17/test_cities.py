import unittest

from city_country_function import city_country


class CityCountryTestCase(unittest.TestCase):
    "Test Case for city_country function"

    def test_city_country(self):
        """Test for return of city and country"""
        city = city_country("santiago", "chile")
        self.assertEqual(city, "Santiago, Chile")

    def test_city_country_population(self):
        """Test for return city, country and population"""
        city = city_country("lyon", "france", "519000")
        self.assertEqual(city, "Lyon, France - population 519000")


if __name__ == "__main__":
    unittest.main(verbosity=2)
