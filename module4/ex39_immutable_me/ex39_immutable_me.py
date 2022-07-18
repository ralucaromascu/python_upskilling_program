class ImmutableMeansImmutableError(Exception):
    pass


class ImmutableParent:
    def __init__(self, attributes):
        for key, value in attributes:
            self.__dict__[key] = value

    def __setattr__(self, key, value):
        if key in vars(self):
            raise ImmutableMeansImmutableError('Cannot change an attribute!')
        else:
            raise ImmutableMeansImmutableError('Cannot add an attribute!')


class ImmutableMe(ImmutableParent):
    def __init__(self, **kwargs):
        super(ImmutableMe, self).__init__(kwargs.items())


if __name__ == '__main__':
    im = ImmutableMe(x=111, y=222, z=333)
    print(f'Before, vars(im) = {vars(im)}')
    im.x = 999
    im.a = 'Hello'
    print(f'After, vars(im) = {vars(im)}')


