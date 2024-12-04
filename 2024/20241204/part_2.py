import os
import re

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# utils
def rotate_90(rows):
    return [''.join(row) for row in zip(*rows[::-1])]
def get_diagonals(rows):
    """
    slice the matrix diagonally
    """
    diagonals = []
    for i in range(len(rows)):
        diagonals.append(''.join(
            rows[j][i-j]
            for j in range(i + 1)
        ))
    
    rows_mirrored = rotate_90(rotate_90(rows))
    for i in range(len(rows_mirrored) - 1):
        diagonals.append(''.join(
            rows_mirrored[j][i-j]
            for j in range(i + 1)
        ))
    return diagonals

# 1. Read the input file
rows = []
# with open("20241204_input_example.txt", "r") as file:
with open("20241204_input.txt", "r") as file:
    for line in file:
        rows.append(line.strip())

# for r in get_diagonals(rows):
#     print(r)

# 2. Find the word "XMAS" in the rows, columns, diagonals, and the reversed rows, columns, and diagonals
counter = 0
for row in rows:
    counter += len(re.findall(r"XMAS", row))
    counter += len(re.findall(r"SAMX", row))
# print(counter)

for row in rotate_90(rows):
    counter += len(re.findall(r"XMAS", row))
    counter += len(re.findall(r"SAMX", row))
# print(counter)

for row in get_diagonals(rows):
    counter += len(re.findall(r"XMAS", row))
    counter += len(re.findall(r"SAMX", row))
# print(counter)

for row in get_diagonals(rotate_90(rows)):
    counter += len(re.findall(r"XMAS", row))
    counter += len(re.findall(r"SAMX", row))
print(counter)

