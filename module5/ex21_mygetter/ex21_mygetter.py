def mygetter():
    pass


if __name__ == '__main__':
    g1 = mygetter(-1)
    print(g1([10, 20, 30]))

    g2 = mygetter(0, -1)
    print(g2([10, 20, 30]))

    g3 = mygetter('b')
    d = {'a': 1, 'b': 2, 'c': 3}
    print(g3(d))
