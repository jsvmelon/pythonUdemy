from unittest import TestCase
from vampyre import Vampyre


def _get_test_tuple(vamp: Vampyre):
    return vamp.name, vamp.hit_points, vamp.lives


class TestVampyre(TestCase):
    def test_basic(self):
        vlad = Vampyre(name="Vlad")
        self.assertEqual(_get_test_tuple(vlad), ("Vlad", 12, 3))

        vlad.take_damage(1)
        self.assertEqual(_get_test_tuple(vlad), ("Vlad", 11, 3))

        vlad.take_damage(11)
        self.assertEqual(_get_test_tuple(vlad), ("Vlad", 12, 2))

        crazy_dog = Vampyre(name="Crazy Dog")
        self.assertEqual(_get_test_tuple(crazy_dog), ("Crazy Dog", 12, 3))

        crazy_dog.take_damage(100)
        self.assertEqual(_get_test_tuple(crazy_dog), ("Crazy Dog", 12, 2))

        angelo = Vampyre(name="Angelo")
        for i in range(0, 4*12):
            self.assertTrue(angelo.alive)
            angelo.take_damage(1)

        self.assertFalse(angelo.alive)
