import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# step 1: parse the data
blocks = []

# with open("20231213_input_example2.txt", "r") as f:
# with open("20231213_input_example.txt", "r") as f:
with open("20231213_input.txt", "r") as f:
    raw = f.read().split("\n\n")

for block in raw:
    blocks.append([line.strip() for line in block.split()])

# step 2: find the vertical lines
vlines = []
for k, block in enumerate(blocks):
    b_vlines = set()
    for i, line in enumerate(block):
        n_cols = len(line)
        for j in range(1, n_cols):
            # print(f"block: {k}, line: {line}, b_vlines: {b_vlines}, i: {i}, j: {j}")
            if (i == 0) and ((j <= n_cols // 2 and line[:j] == line[j:j*2][::-1]) or (j > n_cols // 2 and line[j - (n_cols - j):j] == line[j:][::-1])):
                b_vlines.add(j)
            elif (i > 0) and (j in b_vlines) and not ((j <= n_cols // 2 and line[:j] == line[j:j*2][::-1]) or (j > n_cols // 2 and line[j - (n_cols - j):j] == line[j:][::-1])):
                b_vlines.remove(j)
        if len(b_vlines) == 0:
            no_lines = 1
            break
    vlines.append(b_vlines)
# print(f"vlines: {vlines}")

## calculate the number of cols to the left
cols_to_the_left = 0
for block in vlines:
    for cols in block:
        cols_to_the_left += cols
print(f"cols_to_the_left: {cols_to_the_left}")

# step 3: find the horizontal lines
hlines = []

for block in blocks:
    b_hlines = set()
    for i in range(1, len(block)):
        if (i <= len(block) // 2 and ','.join(block[:i][::-1]) == ','.join(block[i:i*2])) or (i > len(block) // 2 and ','.join(block[i - (len(block) - i):i][::-1]) == ','.join(block[i:])):
            b_hlines.add(i)
    hlines.append(b_hlines)
# print(f"hlines: {hlines}")

## calculate the number of rows above
rows_above = 0
for block in hlines:
    for rows in block:
        rows_above += rows
print(f"rows_above: {rows_above}")

# ste 5: find the total
total = rows_above * 100 + cols_to_the_left
print(f"total: {total}")             
print(f"Number of blocks: {len(blocks)}")

