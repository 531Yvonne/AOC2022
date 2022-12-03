with open("AOC2022-3.txt", "r") as f:
    bags = f.read().strip().split("\n")

# Create Scorebook
scorebook = {}
value1 = 1
for i in range(ord("a"), ord("z")+1):
    scorebook[chr(i)] = value1
    value1 += 1
value2 = 27
for i in range(ord("A"), ord("Z")+1):
    scorebook[chr(i)] = value2
    value2 += 1

# Part 1
common = []
for bag in bags:
    left = bag[:int(len(bag)/2)]
    right = bag[int(len(bag)/2):]
    for char in set(left):
        if char in set(right):
            common.append(char)
score1 = 0
for item in common:
    score1 += scorebook[item]
print("1:", score1)

# Part 2
pos = 0
badge_letters = []
while pos <= len(bags)-3:
    for char in set(bags[pos]):
        if char in set(bags[pos+1]) and char in set(bags[pos+2]):
            badge_letters.append(char)
    pos += 3

score2 = 0
for item in badge_letters:
    score2 += scorebook[item]
print("2:", score2)
