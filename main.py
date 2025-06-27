import random


class DiceGame:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def is_win(self) -> bool:
        return self.total > 7

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


def handle_input() -> str:
    name = ""
    while not name:
        name = input("> ")
    return name


def main():
    print("What is your name?")
    name = handle_input()
    print(f"Hello, {name}")

    game = DiceGame(name)
    game.start()


if __name__ == "__main__":
    main()
