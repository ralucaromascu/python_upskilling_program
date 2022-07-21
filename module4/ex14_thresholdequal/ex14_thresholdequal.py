class ThresholdEqual:
    def __init__(self, x):
        if type(x) != int and type(x) != float:
            raise TypeError("attribute x for class ThresholdEqual should be a number")
        self.x = x
        self.tolerance = 2

    def __eq__(self, other):
        if not isinstance(other, ThresholdEqual):
            raise TypeError(f'The object {other} is not an instance of ThresholdEqual class')
        return abs(self.x - other.x) <= self.tolerance

    def __lt__(self, other):
        return self.x - other.x < 0 and abs(self.x - other.x) > self.tolerance

    def __gt__(self, other):
        return self.x - other.x > 0 and abs(self.x - other.x) > self.tolerance

    def __add__(self, other):
        if not isinstance(other, ThresholdEqual):
            raise TypeError(f'The object {other} is not an instance of ThresholdEqual class')
        return self.x + other.x

    def __iadd__(self, other):
        if not isinstance(other, ThresholdEqual):
            raise TypeError(f'The object {other} is not an instance of ThresholdEqual class')
        self.x += other.x
        return self

    def __sub__(self, other):
        if not isinstance(other, ThresholdEqual):
            raise TypeError(f'The object {other} is not an instance of ThresholdEqual class')
        return self.x - other.x

    def __mul__(self, other):
        if not isinstance(other, ThresholdEqual):
            raise TypeError(f'The object {other} is not an instance of ThresholdEqual class')
        return self.x * other.x

    def __truediv__(self, other):
        if not isinstance(other, ThresholdEqual):
            raise TypeError(f'The object {other} is not an instance of ThresholdEqual class')
        return self.x / other.x

    def __mod__(self, other):
        if not isinstance(other, ThresholdEqual):
            raise TypeError(f'The object {other} is not an instance of ThresholdEqual class')
        return self.x % self.x

    def __pow__(self, other, modulo=None):
        if not isinstance(other, ThresholdEqual):
            raise TypeError(f'The object {other} is not an instance of ThresholdEqual class')
        return pow(self.x, other.x)


if __name__ == '__main__':
    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(6)
    print(te1 == te2)

    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(9)
    print(te1 == te2)
    print(type(te1 + te2))
    te2 += te1
    print(te2.x)
    # print(te1 == 'bad')
    te5 = ThresholdEqual('bad attr')
