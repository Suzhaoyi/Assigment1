import pandas as pd

data = pd.read_csv("input/day3.txt", header=None)
instructions = data.iloc[0, 0]

santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0
visited = [(0, 0)]

for i in range(len(instructions)):
    move = instructions[i]
    if i % 2 == 0:
        if move == "^":
            santa_y = santa_y + 1
        elif move == "v":
            santa_y = santa_y - 1
        elif move == ">":
            santa_x = santa_x + 1
        elif move == "<":
            santa_x = santa_x - 1
        pos = (santa_x, santa_y)
    else:
        if move == "^":
            robo_y = robo_y + 1
        elif move == "v":
            robo_y = robo_y - 1
        elif move == ">":
            robo_x = robo_x + 1
        elif move == "<":
            robo_x = robo_x - 1
        pos = (robo_x, robo_y)

    if pos not in visited:
        visited.append(pos)

print("Day 3 Part 2: The minimum number of houses that received gifts is", len(visited))