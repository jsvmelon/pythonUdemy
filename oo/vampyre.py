from enemy import Enemy


class Vampyre(Enemy):

    def __init__(self, name="Dracula", lives=3, hit_points=12):
        super().__init__(name=name, lives=lives, hit_points=hit_points)
