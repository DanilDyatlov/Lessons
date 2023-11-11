import unittest
from task_two.number_in_out_interval import number_in_out_interval


class test_number_in_out_interval(unittest.TestCase):

    def test_number_in_out_interval_one(self):
        self.assertTrue(number_in_out_interval(26))
    
    def test_number_in_out_interval_two(self):
        self.assertFalse(number_in_out_interval(10))