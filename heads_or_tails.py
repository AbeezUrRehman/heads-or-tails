import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def play_game():
    name = input("Who are you?\n> ")
    print(f"Hello, {name}!")

    print("Tossing a coin...")
    results = [coin_toss() for _ in range(3)]
    heads = results.count("Heads")
    tails = results.count("Tails")

    for i, result in enumerate(results, start=1):
        print(f"Round {i}: {result}")

    print(f"Heads: {heads}, Tails: {tails}")

if __name__ == "__main__":
    play_game()
