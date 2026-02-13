import pandas as pd

data = pd.read_csv("day3.txt", header=None)
instructions = data.iloc[0, 0]

x, y = 0, 0
visited = [(x, y)]

for move in instructions:
    if move == "^":
        y = y + 1
    elif move == "v":
        y = y - 1
    elif move == ">":
        x = x + 1
    elif move == "<":
        x = x - 1
    if (x, y) not in visited:
        visited.append((x, y))

print("Day 3 Part 1: The minimum number of houses that received gifts is", len(visited))