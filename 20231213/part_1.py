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
def find_vlines(block):
    vlines = set()
    for i, line in enumerate(block):
        n_cols = len(line)
        for j in range(1, n_cols):
            if (i == 0) and ((j <= n_cols // 2 and line[:j] == line[j:j*2][::-1]) or (j > n_cols // 2 and line[j - (n_cols - j):j] == line[j:][::-1])):
                vlines.add(j)
            elif (i > 0) and (j in vlines) and not ((j <= n_cols // 2 and line[:j] == line[j:j*2][::-1]) or (j > n_cols // 2 and line[j - (n_cols - j):j] == line[j:][::-1])):
                vlines.remove(j)
        if not vlines:
            break
    return vlines

cols_to_the_left = sum([
    vline
    for block in blocks for vline in find_vlines(block)
])

print(f"cols_to_the_left: {cols_to_the_left}")

# step 3: find the horizontal lines
def find_hlines(block):
    hlines = set()
    for i in range(1, len(block)):
        if (i <= len(block) // 2 and ','.join(block[:i][::-1]) == ','.join(block[i:i*2])) or (i > len(block) // 2 and ','.join(block[i - (len(block) - i):i][::-1]) == ','.join(block[i:])):
            hlines.add(i)
    return hlines


## calculate the number of rows above
rows_above = sum([
    hline
    for block in blocks for hline in find_hlines(block)
])
print(f"rows_above: {rows_above}")

# ste 5: find the total
total = rows_above * 100 + cols_to_the_left
print(f"total: {total}")             
print(f"Number of blocks: {len(blocks)}")

# step 6: visualize the horizontal and vertical lines
for idx, block in enumerate(blocks):
    vline = find_vlines(block)
    hline = find_hlines(block)
    print(f"block: {idx}, vline: {vline}, hline: {hline}")

