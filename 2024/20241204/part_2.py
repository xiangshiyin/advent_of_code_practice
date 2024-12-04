import os
import re

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
rows = []
# with open("20241204_input_example.txt", "r") as file:
with open("20241204_input.txt", "r") as file:
    for line in file:
        rows.append(line.strip())

# 2. Use a 3x3 sliding window to find the number of 3x3 squares that contain the pattern "M.S.A.M.S"
counter = 0
for i in range(len(rows) - 2):
    for j in range(len(rows[0]) - 2):
        if re.search(r"M.S.A.M.S", ''.join(rows[i+k][j:j+3] for k in range(3))):
            counter += 1
        if re.search(r"M.S.A.M.S"[::-1], ''.join(rows[i+k][j:j+3] for k in range(3))):
            counter += 1
        if re.search(r"S.S.A.M.M"[::-1], ''.join(rows[i+k][j:j+3] for k in range(3))):
            counter += 1
        if re.search(r"M.M.A.S.S"[::-1], ''.join(rows[i+k][j:j+3] for k in range(3))):
            counter += 1
print(counter)