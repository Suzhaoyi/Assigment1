import pandas as pd
data = pd.read_csv("day1.txt", header=None)
instructions = data.iloc[0, 0]

floor = 0
for ch in instructions:
    if ch == "(":
        floor = floor + 1
    elif ch == ")":
        floor = floor - 1

print("Day 1 Part 1: The final floor is", floor)