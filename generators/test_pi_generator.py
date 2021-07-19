import math
from unittest import TestCase
import pi_generator


class Test(TestCase):
    def test_odd_numbers(self):
        gen = pi_generator.sign_flipping_odd_numbers()
        for i in range(0, 100):
            self.assertEqual(abs(next(gen)), i * 2 + 1)

    def test_pi_series(self):
        """Test that the approximation gets closer to pi in each step"""
        gen = pi_generator.pi_series()
        approximation = next(gen)
        for i in range(1000):
            next_iteration = next(gen)
            self.assertLess(abs(math.pi - next_iteration), abs(math.pi - approximation))
            approximation = next_iteration
