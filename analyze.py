import csv

def calculate(data):
    total = 0
    playerWins = 0
    bankerWins = 0
    ties = 0
    playerPairs = 0
    bankerPairs = 0
    perfectPairs = 0
    bigHands = 0
    smallHands = 0

    with open(data, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += 1

            if row["Winner"] == "Player":
                playerWins += 1
            elif row["Winner"] == "Banker":
                bankerWins += 1
            elif row["Winner"] == "Tie":
                ties += 1

            playerHand = row["Player Hand"].split("-")
            bankerHand = row["Banker Hand"].split("-")

            if playerHand[0].split(" of ")[0] == playerHand[1].split(" of ")[0]:
                playerPairs += 1
            if bankerHand[0].split(" of ")[0] == bankerHand[1].split(" of ")[0]:
                bankerPairs += 1
            if (playerHand[0].split(" of ")[0] == playerHand[1].split(" of ")[0] and
                bankerHand[0].split(" of ")[0] == bankerHand[1].split(" of ")[0]):
                perfectPairs += 1

            totalCards = len(playerHand) + len(bankerHand)
            if totalCards == 4:
                smallHands += 1
            elif totalCards >= 5:
                bigHands += 1

    if total == 0:
        print("No data found in the CSV file.")
        return

    player = (playerWins / total) * 100
    banker = (bankerWins / total) * 100
    tie = (ties / total) * 100
    playerPair = (playerPairs / total) * 100
    bankerPair = (bankerPairs / total) * 100
    perfectPair = (perfectPairs / total) * 100
    big = (bigHands / total) * 100
    small = (smallHands / total) * 100

    print(f"Total Hands: {total}")
    print(f"Player Win Probability: {player:.2f}%")
    print(f"Banker Win Probability: {banker:.2f}%")
    print(f"Tie Probability: {tie:.2f}%")
    print(f"Player Pair Probability: {playerPair:.2f}%")
    print(f"Banker Pair Probability: {bankerPair:.2f}%")
    print(f"Perfect Pair Probability: {perfectPair:.2f}%")
    print(f"Big Hand Probability: {big:.2f}%")
    print(f"Small Hand Probability: {small:.2f}%")

if __name__ == "__main__":
    data = "data/baccarat_results_1000000.csv" # change based on data file
    calculate(data)
