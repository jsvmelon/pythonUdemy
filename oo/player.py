class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level < 1:
            print("Can't go lower than level 1 - setting to 1")
            level = 1

        diff = level - self._level
        self._level = level
        self._score += (1000 * diff)

    level = property(_get_level, _set_level)

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives: int):
        if lives >= 0:
            self._lives = lives
        else:
            self._lives = 0
            print("Lives cannot be negative - setting them to zero")

    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
