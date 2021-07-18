from unittest import TestCase
from vampyre import Vampyre


def _get_test_tuple(vamp: Vampyre):
    return vamp.name, vamp.hit_points, vamp.lives


class TestVampyre(TestCase):
    def test_basic(self):
        vlad = Vampyre(name="Vlad")
        self.assertEqual(_get_test_tuple(vlad), ("Vlad", 12, 3))

        vlad.take_damage(1, can_dodge=False)
        self.assertEqual(_get_test_tuple(vlad), ("Vlad", 11, 3))

        vlad.take_damage(11, can_dodge=False)
        self.assertEqual(_get_test_tuple(vlad), ("Vlad", 12, 2))

        crazy_dog = Vampyre(name="Crazy Dog")
        self.assertEqual(_get_test_tuple(crazy_dog), ("Crazy Dog", 12, 3))

        crazy_dog.take_damage(100, can_dodge=False)
        self.assertEqual(_get_test_tuple(crazy_dog), ("Crazy Dog", 12, 2))

        angelo = Vampyre(name="Angelo")
        for i in range(0, 4*12):
            self.assertTrue(angelo.alive)
            angelo.take_damage(1, can_dodge=False)

        self.assertFalse(angelo.alive)

    def test_doges(self):
        vlad = Vampyre(name="Vlad")
        dodge_result = vlad.dodges()
        self.assertEqual(type(dodge_result), bool)

        # slightly dodgy test case: this can be unsuccessful in rare cases
        count_true = 0
        for i in range(0, 1000):
            if vlad.dodges():
                count_true += 1
        self.assertTrue(250 <= count_true <= 500)

        # now we check that a vampyre can still take damage and hence die if
        # we try long enough
        django = Vampyre(name="Django")
        while django.alive:
            previous_hit_points = django.hit_points
            previous_lives = django.lives
            django.take_damage(1)
            self.assertTrue(previous_hit_points >= django.hit_points
                            or previous_lives > django.lives)
