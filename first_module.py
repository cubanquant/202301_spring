class Player:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def who_are_you(self):
        return f"My name is {self.name}. I am a {self.sport} player"


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

    p1 = Player("Lionel Messi", "Football")
    p2 = Player("Lebron James", "Basketball")

    print(p1.who_are_you())
    print(p2.who_are_you())
