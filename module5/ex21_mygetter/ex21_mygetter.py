from operator import itemgetter


def mygetter(*args):
    if len(args) == 1:
        def g(obj):
            return obj[args[0]]
    else:
        def g(obj):
            return tuple(obj[arg] for arg in args)
    return g


if __name__ == '__main__':
    g1 = mygetter(-1)
    g_test = itemgetter(-1)
    print(g1([10, 20, 30]))
    g2 = mygetter(0, -1)
    print(g2([10, 20, 30]))

    g3 = mygetter('b')
    d = {'a': 1, 'b': 2, 'c': 3}
    print(g3(d))
