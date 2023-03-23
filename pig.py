import random

MAX_SCORE = 20


def throw_die(sides=6):
    """
    Function that represent throwing a die

    :param sides:
    :return:
    """
    return random.randint(1, sides)


class Player:
    def __init__(self, name):
        self.myname = name
        self.total = 0

    def get_total(self):
        return self.total

    def get_name(self):
        return self.myname

    def show(self):
        print(f"{self.myname} has {self.total} points")

    def turn(self):
        """
        The player takes a turn

        :return:
        """
        turn_total = 0
        roll_hold = "r"
        while roll_hold != "h":
            die_value = throw_die()
            if die_value == 1:
                # scratch
                print(f"{self.myname} rolled a zero. SCRATCH!!! No points for you.")
                return

            print(f"{self.myname} rolled a {die_value}")
            turn_total += die_value
            print(f"{self.myname} has {turn_total} points so far - Possible Points {self.total + turn_total}")
            roll_hold = input("Roll(r) or Hold(h)? ").lower()

        # I press hold and banking points
        self.total += turn_total


class ComputerPlayer(Player):

    def turn(self):
        """
        The player takes a turn

        :return:
        """
        turn_total = 0
        while True:
            #
            if turn_total > min(25, 100 - self.total):
                break

            die_value = throw_die()
            if die_value == 1:
                # scratch
                print(f"{self.myname} rolled a zero. SCRATCH!!! No points for you.")
                return

            print(f"{self.myname} rolled a {die_value}")
            turn_total += die_value
            print(f"{self.myname} has {turn_total} points so far - Possible Points {self.total + turn_total}")

        # I press hold and banking points
        self.total += turn_total


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None

    def check_winner(self):
        """
        Check if there is a winner and stores the winner as an attribute

        :return:
        """
        for player in self.players:
            if player.get_total() >= MAX_SCORE:
                self.winner = player
                return True

        return False

    def play(self):
        """
        Play the game

        :return:
        """
        player_idx = 0
        current_player = self.players[player_idx]
        # Play until there is a winner
        while not self.check_winner():
            print(f"It's {current_player.get_name()} turn...")
            current_player.turn()
            current_player.show()
            if player_idx == 0:
                player_idx = 1
            else:
                player_idx = 0

            current_player = self.players[player_idx]
            print("--------------------------------------------------------")

        print(f"The winner is: {self.winner.get_name()}")
        self.winner.show()


class TimedGame(Game):
    def __init__(self, player1, player2, time_limit=60):
        super().__init__(player1, player2)
        self.time_limit = time_limit
        self.start_time = 0

    def check_winner(self):
        # if (current - start) > time_limit:
        #    Write a message that time expired
        #    Find the winner
        #    return True
        # if not, super().check_winner()
        pass

    def play(self):
        self.start_time = 0 # get the start time
        super().play()


if __name__ == "__main__":
    """Main entry point"""
    player1 = Player("AAAAA")
    player2 = Player("BBBBB")

    game = Game(player1, player2)
    game.play()

