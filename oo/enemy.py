from typing import Tuple


class Enemy:

    def __init__(self, name="Enemy", hit_points=1, lives=1):
        self.name = name
        self.max_hit_points = hit_points
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage: int):
        self.hit_points -= damage
        if self.hit_points >= 1:
            print("Took {} damage. Remaining hit-points {}".format(damage, self.hit_points))
        elif self.lives <= 0:
            self.alive = False
            print("The enemy is dead (RIP)")
        else:
            self.lives -= 1
            self.hit_points = self.max_hit_points
            print("Took {} damage. Lost one life, remaining lives {}".format(damage, self.lives))

    def get_stats(self) -> Tuple[str, int, int, int, bool]:
        """Return a tuple of stats: (name, max_hit_points, hit_points, lives) """
        return self.name, self.max_hit_points, self.hit_points, self.lives, self.alive

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit-points: {0.hit_points}".format(self)
