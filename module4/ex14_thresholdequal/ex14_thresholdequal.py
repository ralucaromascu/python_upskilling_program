class ThresholdEqual:
    def __init__(self, x):
        self.x = x
        self.tolerance = 2

    def __eq__(self, other):
        return abs(self.x - other.x) <= self.tolerance

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        # test cu impartirea la 0
        return self.x / other.x

    def __mod__(self, other):
        return self.x % self.x

    def __pow__(self, other, modulo=None):
        return pow(self.x, other.x)


if __name__ == '__main__':
    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(6)
    print(te1 == te2)

    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(9)
    print(te1 == te2)
