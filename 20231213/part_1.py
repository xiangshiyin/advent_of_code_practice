import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# step 1: parse the data
blocks = []
# with open("20231213_input_example.txt", "r") as f:
with open("20231213_input.txt", "r") as f:
    raw = f.read().split("\n\n")

for block in raw:
    blocks.append([line.strip() for line in block.split()])

# print(blocks)

# block_cols = []
# for block in block_rows:
#     cols = []
#     for j in range(len(block[0])):
#         col = ""
#         for i in range(len(block)):
#             col += block[i][j]
#         cols.append(col)
#         # print(cols)
#     block_cols.append(cols)

# # print(block_cols)


# step 2: find the reflection axis, both the horizontal and vertical axis
cols_to_the_left = 0
## vertical line
for block in blocks:
    v_axis = defaultdict(int)
    n_rows = len(block)
    n_cols = len(block[0])
    for row in block:
        # print(row)
        for j in range(1, n_cols):
            if (j <= n_cols // 2 and row[0:j] == row[j : j + j][::-1]) or (
                j > n_cols // 2 and row[j - (n_cols - j) : j] == row[j:n_cols][::-1]
            ):
                v_axis[j] += 1

    for col, freq in v_axis.items():
        if freq == n_rows:
            cols_to_the_left += col

print(f"cols_to_the_left: {cols_to_the_left}")

rows_above = 0
# horizontal line
for block in blocks:
    h_axis = defaultdict(int)
    for i in range(1, n_rows):
        if (
            i <= n_rows // 2
            and "\n".join(block[0:i][::-1]) == "\n".join(block[i : i + i])
        ) or (
            i > n_rows // 2
            and "\n".join(block[i - (n_rows - i) : i][::-1])
            == "\n".join(block[i:n_rows])
        ):
            h_axis[i] += 1
            # print(i, i <= n_rows // 2, i > n_rows // 2)
        # print(i, "\n".join(block[0:i][::-1]), "\n".join(block[i : i + i]))
# print(h_axis)

for row in h_axis:
    rows_above += row

print(f"Answer: {rows_above * 100 + cols_to_the_left}")
