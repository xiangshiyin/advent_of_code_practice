import os
import sys
import time
import heapq

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241216_input_example.txt" if use_example else "20241216_input.txt"
grid = []
with open(path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))
nrows, ncols = len(grid), len(grid[0])
print(f"Dimensions of the grid: {nrows}x{ncols}")

# 2. Find the start and end positions
for r in range(nrows):
    for c in range(ncols):
        if grid[r][c] == "S":
            sr, sc = r, c
        else:
            continue
        break

print(f"Start position: {sr, sc}")

# 3. Dijkstra's algorithm to find the shortest path
pq = [(0, sr, sc, 0, 1)]
seen = set()

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    seen.add((r, c, dr, dc))
    if grid[r][c] == "E":
        print(cost)
        break
    for ncost, nr, nc, ndr, ndc in [
        (cost + 1, r + dr, c + dc, dr, dc),
        (cost + 1000, r, c, dc, dr), 
        (cost + 1000, r, c, -dc, dr) if dr == 0 else (cost + 1000, r, c, dc, -dr),
    ]:
        if grid[nr][nc] == "#": continue
        if (nr, nc, ndr, ndc) in seen: continue
        heapq.heappush(pq, (ncost, nr, nc, ndr, ndc))


#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
