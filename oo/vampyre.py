import random
from enemy import Enemy


class Vampyre(Enemy):

    def __init__(self, name="Dracula", lives=3, hit_points=12):
        super().__init__(name=name, lives=lives, hit_points=hit_points)

    @staticmethod
    def dodges():
        if random.randint(1, 3) == 3:
            return True
        else:
            return False

    def take_damage(self, damage: int, can_dodge: bool = True):
        if can_dodge and self.dodges():
            print("dodged")
        else:
            super().take_damage(damage=damage)
