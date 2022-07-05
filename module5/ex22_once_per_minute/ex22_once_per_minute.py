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
