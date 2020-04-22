import unittest

from city_functions import function_cc

class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = function_cc('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

unittest.main()