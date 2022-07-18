def magic_tuples(total, max_value):
    for i in range(total - max_value + 1, max_value):
        if i > 0 and total - i > 0:
            yield i, total - i


if __name__ == '__main__':
    for t in magic_tuples(5, 4):
        print(t)
