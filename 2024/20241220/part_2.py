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

# 3. Save the spots on the path to a dict
path_spots = {}
for i in range(nrows):
    for j in range(ncols):
        if dists[i][j] != -1:
            path_spots[(i, j)] = dists[i][j]

# print({key:path_spots[key] for key in sorted(path_spots, key=lambda x: path_spots[x])})

# 4. Traverse the spots on the path and find cheat points
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
counter = 0
steps_to_save = 100
steps_to_cheat = 20
visited = set()

for r, c in path_spots:
    q = deque([(r, c, 0)])
    visited2 = set()
    while q:
        cr, cc, steps = q.popleft()
        if steps > steps_to_cheat: break
        for dr, dc in drc:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < nrows and 0 <= nc < ncols and (nr, nc) not in visited2:
                visited2.add((nr, nc))
                if (nr, nc) in path_spots and (r, c, nr, nc) not in visited and (nr, nc, r, c) not in visited and abs(nr-r) + abs(nc-c) <= steps_to_cheat and path_spots[(nr, nc)] - path_spots[(r, c)] >= abs(nr-r) + abs(nc-c) + steps_to_save:
                    counter += 1
                    # print(f"Cheat point: ({r}, {c}) -> ({nr}, {nc}), old distance {path_spots[(nr, nc)] - path_spots[(r, c)]}, new distance: {abs(nr-r) + abs(nc-c)}, steps away from ({r}, {c}): {steps+1}")
                    visited.add((r, c, nr, nc))
                q.append((nr, nc, steps + 1))
print(counter)

# # example cases to test
# steps_to_save = [2,4,6,8,10,12,20,36,38,40,64]
# for step in steps_to_save:
#     print(f"Steps to save: {step}, Cheats: {num_cheats(step)}")

# print(num_cheats(100))
#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
