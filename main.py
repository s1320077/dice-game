import random
from functools import reduce


class DiceGame:
    def __init__(self, name, winning_threshold):
        self.name = name
        self.total = 0
        self.is_winning_condition = lambda x: x > winning_threshold

    def is_win(self) -> bool:
        return self.is_winning_condition(self.total)

    def start(self):
        print("Rolling dice...")
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self.total = die1 + die2
        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        print(f"Total value: {self.total}")

        if self.is_win():
            print(f"{self.name} won!")
        else:
            print(f"{self.name} lost")

    def print_value_table(self) -> None:
        print("value table")
        print("   1  2  3  4  5  6")
        for i in range(1, 7):
            print(f"{i} ", end="")
            for j in range(1, 7):
                print(f"{i + j:2} ", end="")
            print("")

    def calc_win_probability(self) -> float:
        win_count = sum(
            self.is_winning_condition(i + j) for i in range(1, 7) for j in range(1, 7)
        )
        return win_count / 36


def handle_input() -> str:
    name = ""
    while not name:
        name = input("> ")
    return name


def main():
    print("What is your name?")
    name = handle_input()
    print(f"Hello, {name}")

    game = DiceGame(name, 7)
    game.print_value_table()
    print(f"yout win probability: {game.calc_win_probability()}")
    game.start()


if __name__ == "__main__":
    main()
