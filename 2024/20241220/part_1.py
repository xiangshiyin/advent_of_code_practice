import os
import sys
import time
from collections import deque
from tqdm import tqdm
# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241220_input_example.txt" if use_example else "20241220_input.txt"
rows = []
with open(path, "r") as file:
    for line in file:
        rows.append(list(line.strip()))
nrows, ncols = len(rows), len(rows[0])

# 2. Find the start and endposition
for i, row in enumerate(rows):
    for j, cell in enumerate(row):
        if cell == "S": sr, sc = i, j
        if cell == "E": er, ec = i, j
print(f"Start: {sr}, {sc}, End: {er}, {ec}")

dists = [[-1] * ncols for _ in range(nrows)]
dists[sr][sc] = 0

q = deque([(sr, sc)])
while q:
    r, c = q.popleft()
    if rows[r][c] == "E": break
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < nrows and 0 <= nc < ncols and dists[nr][nc] == -1 and rows[nr][nc] != "#" and dists[nr][nc] == -1:
            dists[nr][nc] = dists[r][c] + 1
            q.append((nr, nc))

# find the longest distance
longest_dist = max(max(row) for row in dists)
print(f"Longest distance: {longest_dist}")

# # print the dists
# for row in dists:
#     print("|".join(f"{d:2}" for d in row))

# 3. Traverse the dist map to find the cheat points that can save us X steps to reach the end
def num_cheats(steps_to_save):
    cheats = 0
    for i in range(nrows):
        for j in range(ncols):
            if dists[i][j] == -1: continue
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = i + dr, j + dc
                if 0 <= nr < nrows and 0 <= nc < ncols and dists[nr][nc] == -1:
                    for dr2, dc2 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nnr, nnc = nr + dr2, nc + dc2
                        if 0 <= nnr < nrows and 0 <= nnc < ncols and dists[nnr][nnc] != -1 and abs(dists[nnr][nnc] - dists[i][j]) >= 2 + steps_to_save:
                            # print(f"Cheat point: {i}, {j} to {nr}, {nc} to {nnr}, {nnc}")
                            cheats += 1
    return cheats // 2

# # example cases to test
# steps_to_save = [2,4,6,8,10,12,20,36,38,40,64]
# for step in steps_to_save:
#     print(f"Steps to save: {step}, Cheats: {num_cheats(step)}")

print(num_cheats(100))
#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
