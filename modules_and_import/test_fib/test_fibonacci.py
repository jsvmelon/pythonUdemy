import unittest
from scope import fib


class TestFibonacciFunction(unittest.TestCase):

    def test_simple(self):
        expected_results = [1, 1, 2, 3, 5, 8, 13, 21]
        for index, result in enumerate(expected_results):
            self.assertEqual(fib(index+1), result)


if __name__ == "__main__":
    unittest.main()
