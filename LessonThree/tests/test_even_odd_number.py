import unittest
from task_one.even_odd_number import even_odd_number


class test_even_odd_number(unittest.TestCase):

    def test_even_number_one(self):
        self.assertTrue(even_odd_number(6))
    
    def test_even_number_two(self):
        self.assertFalse(even_odd_number(17))