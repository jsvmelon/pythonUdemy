class Wing:
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            return "Weee, this is fun"
        elif self.ratio == 1:
            return "This is hard work, but I'm flying"
        else:
            return "I think I'll just walk"


class Duck:
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        return "Waddle, waddle, waddle"

    def swim(self):
        return "Come on in, the water's lovely"

    def quack(self):
        return "Quack quack"

    def fly(self):
        return self._wing.fly()


class Penguin:
    def walk(self):
        return "Waddle, waddle, I waddle too"

    def swim(self):
        return "Come on in the water, but it's a bit chilly this far South"

    def quack(self):
        return "Are you 'avin' a larf? Penguin's don't quack!"
