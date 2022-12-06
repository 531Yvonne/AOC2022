import re

# Read original stacks (store each stack in a list) [[column 1: top ..... bottom]....]
with open("AOC2022-5.txt", "r") as f:
    original = [[] for i in range(9)]
    for i in range(8):
        line = f.readline().strip().split(" ")
        column = 0
        for char in line:
            if char != "":
                original[int(column)].append(char)
                column += 1
            else:
                column += 0.25
    f.readline()

# Read all moves and store in a list [[#, from, to].......]
    lines = f.read().strip().split("\n")
    moves = []
    for i in lines:
        matches = re.search(r'.+(\d+).+(\d+).+(\d+)', i)
        moves.append([int(matches.group(1)), int(matches.group(2)), int(matches.group(3))])



# Part 1 Fully Included


# Part 2 Any Overlap (use the contrary: total - non-overlap)

