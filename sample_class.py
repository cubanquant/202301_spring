class Player:
    def __init__(self, name, number, sport):
        self.name = name
        self.number = number
        self.sport = sport

    def whoami(self):
        return f"I'm {self.name}. I play {self.sport}. I wear number {self.number}"

    def get_name(self):
        return self.name


def main():
    messi = Player("Lionel Messi", 10, "soccer")
    print(messi.whoami())
    print(messi.get_name())

    bueno = Player("Leonel Bueno", 4, "volleyball")
    print(bueno.whoami())


if __name__ == "__main__":
    main()
