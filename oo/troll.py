from enemy import Enemy


class Troll(Enemy):

    def __init__(self, name):
        # Enemy.__init__(self, name=name, hit_points=23, lives=1)
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        return "Me {0.name}. {0.name} stomp you".format(self)
