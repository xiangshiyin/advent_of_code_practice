import os
import sys
import time
from collections import deque
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

# 2. Find the start position
for i, row in enumerate(rows):
    for j, cell in enumerate(row):
        if cell == "S":
            sr, sc = i, j
            break
print(f"Start: {sr}, {sc}")

# 3. Find the shortest path via BFS
def bfs(sr, sc, rows):
    q = deque([(sr, sc, 0)])
    visited = set([(sr, sc)])

    while q:
        r, c, d = q.popleft()
        if rows[r][c] == "E":
            return d
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(rows) and 0 <= nc < len(rows[nr]) and (nr, nc) not in visited and rows[nr][nc] != "#":
                q.append((nr, nc, d + 1))
                visited.add((nr, nc))
    return -1

print("Shortest distance:", bfs(sr, sc, rows))

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")