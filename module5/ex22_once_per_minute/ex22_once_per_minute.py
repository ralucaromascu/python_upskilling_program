import time


class TooSoonError(Exception):
    pass


def once_per_minute(func):
    def wrapper(*args, **kwargs):
        actual_time = time.perf_counter()
        print(wrapper.start_time)
        print(actual_time)
        if (actual_time-wrapper.start_time) < 60 and wrapper.is_first_time is False:
            raise TooSoonError(f'Too soon: Wait another {60 - (actual_time-wrapper.start_time) % 60} seconds')
        wrapper.start_time = actual_time
        if wrapper.is_first_time is True:
            wrapper.is_first_time = False
        return func(*args, **kwargs)
    wrapper.start_time = time.perf_counter()
    wrapper.is_first_time = True
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
