from troll import Troll
from unittest import TestCase


class TestTroll(TestCase):

    def test_basic(self):
        ugly_troll = Troll("Pug")
        self.assertTrue(len(ugly_troll.grunt()) > 0)
        print(ugly_troll.grunt())
        print("Ugly troll - {}".format(ugly_troll))
        ugly_troll.take_damage(2)
        self.assertEqual(ugly_troll.hit_points, 21)

        another_troll = Troll("Ug")
        print(another_troll.grunt())
        print("Another troll - {}".format(another_troll))

        brother = Troll("Urg")
        print(brother.grunt())
        print(brother)
