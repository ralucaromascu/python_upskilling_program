class ThresholdEqual:
    pass


if __name__ == '__main__':
    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(6)
    print(te1 == te2)

    te1 = ThresholdEqual(10)
    te2 = ThresholdEqual(9)
    print(te1 == te2)
