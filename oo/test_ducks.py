from unittest import TestCase
from ducks import Duck, Penguin


class TestDuck(TestCase):
    """This is not the right way to test - it is only to demonstrate that we can test a Penguin like a Duck because it
    has the same methods
    """

    def test_walk(self):
        donald = Duck()
        self.assertTrue("waddle" in donald.walk().casefold())

        percy = Penguin()
        self.assertTrue("waddle" in percy.walk().casefold())

    def test_swim(self):
        donald = Duck()
        self.assertTrue("water" in donald.swim().casefold())

        percy = Penguin()
        self.assertTrue("water" in percy.swim().casefold())

    def test_quack(self):
        donald = Duck()
        self.assertTrue("quack" in donald.quack().casefold())

        percy = Penguin()
        self.assertTrue("quack" in percy.quack().casefold())

    def test_fly(self):
        donald = Duck()
        self.assertTrue(len(donald.fly()) > 0)


class TestPenguin(TestCase):

    def test_walk(self):
        pass

    def test_swim(self):
        pass


    def test_quack(self):
        pass
