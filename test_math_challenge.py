import unittest
from math_challenge import count_connections

class TestCountConnections(unittest.TestCase):
    def test_small_number(self):
        self.assertEqual(count_connections(2), 1)  # Only one connection

    def test_medium_number(self):
        self.assertEqual(count_connections(5), 10)  # Standard case

    def test_large_number(self):
        self.assertEqual(count_connections(10), 45)  # Testing a larger input

    def test_zero_case(self):
        self.assertEqual(count_connections(0), 0)  # No computers, no connections

    def test_one_case(self):
        self.assertEqual(count_connections(1), 0)  # A single computer can't connect to anything


if __name__ == "__main__":
    unittest.main()

