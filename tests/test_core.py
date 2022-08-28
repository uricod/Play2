import unittest
from src.main import print_something


class TestCore(unittest.TestCase):
    def test_print(self):
        self.assertEqual('hello', print_something('hello'))
        self.assertEqual('', print_something(''))
