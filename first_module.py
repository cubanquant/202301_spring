def plus2(x):
    """
    Function that adds 2 to the value passed

    :param x:
    :return:
    """
    return x + 2


if __name__ == "__main__":
    print("Welcome to the class")
    for x in range(6):
        y = plus2(x)
        print(f"{x} + 2 = {y}")
