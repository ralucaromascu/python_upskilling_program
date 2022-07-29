import random


class RandMemory:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self._history = []

    @property
    def get(self):
        nr = random.randint(self.lowest, self.highest)
        self._history.append(nr)
        return nr

    def history(self):
        return self._history


if __name__ == '__main__':
    r = RandMemory(1, 100)
    print(r.get)
    print(r.get)
    print(r.get)
    print(r.history())
