from unittest import TestCase
from scratchpad import fibonacci


class Test(TestCase):
    def test_fibonacci(self):
        sequence = fibonacci(10)
        s_list = []
        for i in fibonacci(10):
            s_list.append(i)

        self.assertEqual(s_list, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
