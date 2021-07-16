import unittest
from enemy import Enemy


class TestEnemy(unittest.TestCase):

    def test_positive(self):
        random_monster = Enemy("Basic enemy", 12, 1)
        self.assertEqual(random_monster.hit_points, 12)
        self.assertEqual(random_monster.lives, 1)
        print(random_monster)

        random_monster.take_damage(4)
        self.assertEqual(random_monster.hit_points, 8)
        print(random_monster)

        random_monster.take_damage(8)
        self.assertEqual(random_monster.lives, 0)
        self.assertEqual(random_monster.hit_points, 12)
        print(random_monster)

        random_monster.take_damage(9)
        self.assertEqual(random_monster.lives, 0)
        self.assertEqual(random_monster.hit_points, 3)
        print(random_monster)

        random_monster.take_damage(3)
        self.assertEqual(random_monster.lives, 0)
        self.assertEqual(random_monster.hit_points, 0)
