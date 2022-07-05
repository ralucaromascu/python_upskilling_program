if __name__ == '__main__':
    im = ImmutableMe(x=111, y=222, z=333)
    print(f"Before, vars(im) = {vars(im)}")
    im.x = 999
    im.a = "Hello"
