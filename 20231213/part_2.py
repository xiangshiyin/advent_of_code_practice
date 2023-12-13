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

# step 2: find the vertical and horizontal lines
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

def find_hlines(block):
    hlines = set()
    for i in range(1, len(block)):
        if (i <= len(block) // 2 and ','.join(block[:i][::-1]) == ','.join(block[i:i*2])) or (i > len(block) // 2 and ','.join(block[i - (len(block) - i):i][::-1]) == ','.join(block[i:])):
            hlines.add(i)
    return hlines

# step 3: find the smudges
def intro_smudge(block, r, c):
    block2 = block.copy()
    block2[r] = block[r][:c] + "#" + block[r][c+1:] if block[r][c] == "." else block[r][:c] + "." + block[r][c+1:]
    return block2

blocks_new = []
vlines = []
hlines = []
for idx, block in enumerate(blocks):
    found = 0
    for r in range(len(block)):
        for c in range(len(block[0])):
            new_block = intro_smudge(block, r, c)
            vline_new = find_vlines(new_block)
            vline_old = find_vlines(block)
            hline_new = find_hlines(new_block)
            hline_old = find_hlines(block)
            if (vline_new != vline_old or hline_new != hline_old) and (vline_new or hline_new):
                blocks_new.append(new_block)
                vlines.append(vline_new - vline_old)
                hlines.append(hline_new - hline_old)
                found = 1
                print(f"block: {idx}, vline_old: {vline_old}, vline_new: {vlines[-1]}, hline_old: {hline_old}, hline_new: {hlines[-1]}")
                break
        if found:
            break

## calculate the number of columns to the left
cols_to_the_left = sum([
    v
    for vline in vlines for v in vline
])

print(f"cols_to_the_left: {cols_to_the_left}")
## calculate the number of rows above
rows_above = sum([
    h
    for hline in hlines for h in hline
])
print(f"rows_above: {rows_above}")

# ste 5: find the total
total = rows_above * 100 + cols_to_the_left
print(f"total: {total}")

# step 6: visualize the horizontal and vertical lines
for idx, block in enumerate(blocks_new):
    vline = vlines[idx]
    hline = hlines[idx]
    print(f"block: {idx}, vline: {vline}, hline: {hline}")
