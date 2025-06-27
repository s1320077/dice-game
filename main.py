import random

def main():
    print("Rolling dice...")
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total value: {die1 + die2}")

if __name__ == "__main__":
    main()
