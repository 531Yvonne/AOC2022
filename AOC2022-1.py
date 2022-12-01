with open("AOC2022-1.txt", "r") as f:
    entire_text = f.read()
    foods = []
    n = 1
    for i in entire_text.split("\n"):
        if i != '':
            foods.append(int(i))
        else:
            n += 1
            foods.append(0)
t = 0
cal = []
for item in foods:
    if item != 0:
        t += item
    else:
        cal.append(t)
        t = 0
cal.sort()

print("1:", max(cal))
print("2:", sum(cal[-3:]))
