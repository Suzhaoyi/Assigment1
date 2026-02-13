import pandas as pd
data = pd.read_csv("input/day1.txt", header=None)
instructions = data.iloc[0, 0]

floor = 0
position = 0
for ch in instructions:
    position = position + 1
    if ch == "(":
        floor = floor + 1
    elif ch == ")":
        floor = floor - 1
    if floor == -1:
        print("Day 1 Part 2: The location where Santa first entered the basement is", position)
        break