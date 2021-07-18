from vampyre import Vampyre
import math


class VampyreKing(Vampyre):

    def __init__(self):
        super().__init__(name="Count Dracula", lives=3, hit_points=140)

    def take_damage(self, damage: int, can_dodge: bool = True):
        real_damage: int = math.floor(damage / 4)
        super().take_damage(damage=real_damage)
