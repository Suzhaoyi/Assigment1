import pandas as pd

lights_df = pd.DataFrame(0, index=range(1000), columns=range(1000))

def apply_instruction_df(instruction: str):
    parts = instruction.split()
    if parts[0] == "toggle":
        coord1 = parts[1].split(",")
        coord2 = parts[3].split(",")
        x1, y1 = int(coord1[0]), int(coord1[1])
        x2, y2 = int(coord2[0]), int(coord2[1])
        lights_df.loc[x1:x2, y1:y2] = lights_df.loc[x1:x2, y1:y2] + 2
    else:
        action = parts[1]
        coord1 = parts[2].split(",")
        coord2 = parts[4].split(",")
        x1, y1 = int(coord1[0]), int(coord1[1])
        x2, y2 = int(coord2[0]), int(coord2[1])
        if action == "on":
            lights_df.loc[x1:x2, y1:y2] = lights_df.loc[x1:x2, y1:y2] + 1
        else:
            lights_df.loc[x1:x2, y1:y2] = (lights_df.loc[x1:x2, y1:y2] - 1).clip(lower=0)

with open("day6.txt", "r") as f:
    instructions = f.readlines()

for instr in instructions:
    apply_instruction_df(instr.strip())

total_brightness = lights_df.sum().sum()
print("Day 6 Part 2: The total brightness of all lights is", total_brightness)