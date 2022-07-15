def magic_tuples(total, max_value):
    for i in range(total - max_value + 1, max_value):
        yield i, total - i


if __name__ == '__main__':
    for t in magic_tuples(5, 4):
        print(t)
