# Test employee:
import unittest
from ch11_3 import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.adam = Employee('adam', 'golota', 55000)

    def test_give_default_raise(self):
        self.adam.give_raise()
        self.assertEqual(self.adam.salary, 60000)

    def test_give_custom_raise(self):
        self.adam.give_raise(10000)
        self.assertEqual(self.adam.salary, 65000)

unittest.main()