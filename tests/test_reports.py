import unittest
class TestCase(unittest.TestCase):
    def test_average_balance(self):
        self.assertEqual(average_balance([]), 0.0)
        self.assertEqual(average_balance([3,4,5]), 4.0)