with open("AOC2022-2.txt", "r") as f:
    games = f.read().strip().split("\n")

book1 = {"A X": 1+3, "A Y": 2+6, "A Z": 3, "B X": 1, "B Y": 2+3, "B Z": 3+6, "C X": 1+6, "C Y": 2, "C Z": 3+3}
book2 = {"A X": 0+3, "A Y": 3+1, "A Z": 6+2, "B X": 0+1, "B Y": 3+2, "B Z": 6+3, "C X": 0+2, "C Y": 3+3, "C Z": 6+1}

score1 = 0
score2 = 0
for game in games:
    score1 += book1[game]
    score2 += book2[game]


print("1:", score1)
print("2:", score2)
