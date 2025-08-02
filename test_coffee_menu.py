import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'), 2.75)

    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price('mocha'))

    def test_add_item_valid(self):
        self.menu.add_item('chai', 3.00)
        self.assertEqual(self.menu.get_price('chai'), 3.00)

    def test_add_item_zero_price(self):
       with self.assertRaises(ValueError):
        self.menu.add_item('mandazi', 0)

    def test_add_item2_valid(self):
        self.assertEqual(self.menu.get_price('samosa'), 1.50)

    def test_add_item_negative_price(self):
       with self.assertRaises(ValueError):
        self.menu.add_item('samosa', -1.50)

