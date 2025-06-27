import random


def handle_input() -> str:
    name = ""
    while not name:
        name = input("> ")
    return name


def is_win(total: int) -> bool:
    return total > 7


def main():
    print("What is your name?")
    name = handle_input()
    print(f"Hello, {name}")

    print("Rolling dice...")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total value: {total}")

    if is_win(total):
        print(f"{name} won!")
    else:
        print(f"{name} lost")


if __name__ == "__main__":
    main()
