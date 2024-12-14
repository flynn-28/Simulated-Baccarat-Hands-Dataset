import random
import csv

CARD_VALUES = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 0, "J": 0, "Q": 0, "K": 0
}

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = list(CARD_VALUES.keys())
DECK = [(rank, suit) for rank in RANKS for suit in SUITS]


def shuffle():
    deck = DECK * 8  
    random.shuffle(deck)
    return deck


def handValue(hand):
    total = sum(CARD_VALUES[card[0]] for card in hand) % 10
    return total


def simHand(deck):
    playerHand = [deck.pop(), deck.pop()]
    bankerHand = [deck.pop(), deck.pop()]

    playerVal = handValue(playerHand)
    bankerVal = handValue(bankerHand)

    if playerVal < 6:
        playerHand.append(deck.pop())
        playerVal = handValue(playerHand)

    if bankerVal < 6:
        bankerHand.append(deck.pop())
        bankerVal = handValue(bankerHand)

    if playerVal > bankerVal:
        winner = "Player"
    elif bankerVal > playerVal:
        winner = "Banker"
    else:
        winner = "Tie"

    return {
        "Player Hand": playerHand,
        "Player Value": playerVal,
        "Banker Hand": bankerHand,
        "Banker Value": bankerVal,
        "Winner": winner
    }


def save(rounds, output):
    deck = shuffle()
    results = []

    for _ in range(rounds):
        if len(deck) < 15:
            deck = shuffle()

        handResults = simHand(deck)
        results.append(handResults)

    with open(output, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Player Hand", "Player Value", "Banker Hand", "Banker Value", "Winner"])
        writer.writeheader()
        for result in results:
            writer.writerow({
                "Player Hand": "-".join([f"{rank} of {suit}" for rank, suit in result["Player Hand"]]),
                "Player Value": result["Player Value"],
                "Banker Hand": "-".join([f"{rank} of {suit}" for rank, suit in result["Banker Hand"]]),
                "Banker Value": result["Banker Value"],
                "Winner": result["Winner"]
            })

    print(f"Simulated {rounds} Baccarat hands. Results saved to {output}.")


if __name__ == "__main__":
    rounds = int(input("Enter rounds: "))
    output = f"data/baccarat_results_{rounds}.csv"
    save(rounds, output)
