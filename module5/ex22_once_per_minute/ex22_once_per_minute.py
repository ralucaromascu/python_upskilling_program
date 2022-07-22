import time
from math import trunc

start_time = 0
is_first_time = True


class TooSoonError(Exception):
    pass


def once_per_minute(func):
    def wrapper(*args, **kwargs):
        global start_time
        global is_first_time
        actual_time = time.perf_counter()
        if is_first_time is True:
            start_time = actual_time
            is_first_time = False
        print(actual_time)
        print(start_time)
        time_diff = actual_time-start_time
        if trunc(time_diff) % 60 != 0:
            raise TooSoonError(f'Too soon: Wait another {60 - time_diff % 60} seconds')
        else:
            func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    @once_per_minute
    def hello(name):
        return 'Hello, {}'.format(name)


    for i in range(30):
        print(i)
        try:
            time.sleep(3)
            print(hello(f'attempt {i}'))
        except TooSoonError as e:
            print(f'Too soon: {e}')
