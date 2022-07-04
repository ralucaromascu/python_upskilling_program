def create_password_checker():
    pass


if __name__ == "__main__":
    pc1 = create_password_checker(2, 3, 1, 4)
    print(pc1('Ab!1'))
    print(pc1('ABcde!1234'))
