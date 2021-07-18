from unittest import TestCase
from vampyre_king import VampyreKing


class TestVampyreKing(TestCase):
    def test_take_damage(self):
        dracula = VampyreKing()
        self.assertEqual(dracula.hit_points, 140)
        self.assertEqual(dracula.lives, 3)
        self.assertEqual(dracula.name, "Count Dracula")

        while True:
            previous_hit_points = dracula.hit_points
            dracula.take_damage(100)
            if dracula.hit_points < previous_hit_points:
                self.assertEqual(dracula.hit_points, 115)
                break
