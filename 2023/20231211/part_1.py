import os
from collections import deque

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# with open("20231211_input_example.txt") as f:
with open("20231211_input.txt") as f:
    lines = f.read().splitlines()

# for line in lines:
#     print(line)

# step 1: find all galaxies
n_rows = len(lines)
n_cols = len(lines[0])
galaxies = []
rows_galaxies_count = [0] * n_rows
cols_galaxies_count = [0] * n_cols

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            rows_galaxies_count[r] += 1
            cols_galaxies_count[c] += 1
            galaxies.append((r, c))

galaxies_count = len(galaxies)

def find_empty_rows_and_cols(start_r, start_c, end_r, end_c):
    start_r2, end_r2 = min(start_r, end_r), max(start_r, end_r)
    start_c2, end_c2 = min(start_c, end_c), max(start_c, end_c)

    empty_rows = 0
    empty_cols = 0
    for r in range(start_r2 + 1, end_r2):
        if rows_galaxies_count[r] == 0:
            empty_rows += 1
    for c in range(start_c2 + 1, end_c2):
        if cols_galaxies_count[c] == 0:
            empty_cols += 1
    return empty_rows, empty_cols

print(f"rows_galaxies_count: {rows_galaxies_count}")
print(f"cols_galaxies_count: {cols_galaxies_count}")

steps = 0 
for i in range(galaxies_count):
    for j in range(i + 1, galaxies_count):
        r1, c1 = galaxies[i]
        r2, c2 = galaxies[j]
        empty_rows, empty_cols = find_empty_rows_and_cols(r1, c1, r2, c2)
        distance = abs(r1 - r2) + abs(c1 - c2) - empty_rows - empty_cols + empty_rows * 2 + empty_cols * 2

        # print(f"Distance: {distance}, empty_rows: {empty_rows}, empty_cols: {empty_cols}, ({r1}, {c1}) -> ({r2}, {c2})")

        steps += distance

print(f"Steps: {steps}")