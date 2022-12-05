with open("AOC2022-4.txt", "r") as f:
    pairs = f.read().strip().split("\n")
    all_pairs = []
    for pair in pairs:
        ranges = pair.split(",")
        for range in ranges:
            numbers = range.split("-")
            all_pairs.append([int(numbers[0]), int(numbers[1])])

# Part 1 Fully Included
i = 0
count = 0
while i <= len(all_pairs) - 2:
    if all_pairs[i][0] <= all_pairs[i+1][0]\
         and all_pairs[i][1] >= all_pairs[i+1][1]:
        count += 1
    elif all_pairs[i][0] >= all_pairs[i+1][0]\
         and all_pairs[i][1] <= all_pairs[i+1][1]:
        count += 1
    i += 2
print("1:", count)

# Part 2 Any Overlap (use the contrary: total - non-overlap)
j = 0
count2 = int(len(all_pairs) / 2)
while j <= len(all_pairs) - 2:
    if all_pairs[j][0] > all_pairs[j+1][1]:
        count2 -= 1
    elif all_pairs[j][1] < all_pairs[j+1][0]:
        count2 -= 1
    j += 2
print("2:", count2)
