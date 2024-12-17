import os
import sys
import time
import heapq
from collections import deque

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
def dijkstra(sr, sc, grid):
    pq = [(0, sr, sc, 0, 1)]
    seen = set()

    while pq:
        cost, r, c, dr, dc = heapq.heappop(pq)
        seen.add((r, c, dr, dc))
        if grid[r][c] == "E":
            return cost
        for ncost, nr, nc, ndr, ndc in [
            (cost + 1, r + dr, c + dc, dr, dc),
            (cost + 1000, r, c, dc, dr), 
            (cost + 1000, r, c, -dc, dr) if dr == 0 else (cost + 1000, r, c, dc, -dr),
        ]:
            if grid[nr][nc] == "#": continue
            if (nr, nc, ndr, ndc) in seen: continue
            heapq.heappush(pq, (ncost, nr, nc, ndr, ndc))

min_cost = dijkstra(sr, sc, grid)
print(f"Minimum cost: {min_cost}")

# 4. Given the total cost, find all the paths that have this cost
def dijkstra2(sr, sc, grid):
    pq = [(0, sr, sc, 0, 1, None, None, None, None)]
    lowest_cost = {(sr, sc, 0, 1): 0}
    backtrack = {}
    end_states = set()
    best_cost = float('inf')

    while pq:
        cost, r, c, dr, dc, pr, pc, pdr, pdc = heapq.heappop(pq)

        if (r, c, dr, dc) not in backtrack: backtrack[(r, c, dr, dc)] = set()
        backtrack[(r, c, dr, dc)].add((pr, pc, pdr, pdc))
        
        if cost > lowest_cost.get((r, c, dr, dc), float('inf')): continue
        lowest_cost[(r, c, dr, dc)] = cost

        if grid[r][c] == "E":
            if cost > best_cost: break
            best_cost = cost
            end_states.add((r, c, dr, dc))

        for ncost, nr, nc, ndr, ndc in [
            (cost + 1, r + dr, c + dc, dr, dc),
            (cost + 1000, r, c, dc, dr), 
            (cost + 1000, r, c, -dc, dr) if dr == 0 else (cost + 1000, r, c, dc, -dr),
        ]:
            if grid[nr][nc] == "#": continue
            if cost > lowest_cost.get((nr, nc, ndr, ndc), float('inf')): continue
            heapq.heappush(pq, (ncost, nr, nc, ndr, ndc, r, c, dr, dc))
    
    return backtrack, end_states
backtrack, end_states = dijkstra2(sr, sc, grid)

# 5. Find all the unique positions in all the paths
# print(end_states)
# print(backtrack)

states = deque(end_states)
seen = set(end_states)

while states:
    key = states.popleft()
    for last in backtrack.get(key, []):
        if last in seen: continue
        seen.add(last)
        states.append(last)


print(len(set([
    (r, c) for r, c, dr, dc in seen if r != None
])))

# # 6. Update the grid with the spots on the best paths
# for r, c, dr, dc in seen:
#     if r == None: continue
#     grid[r][c] = "0"

# for row in grid:
#     print("".join(row))


#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")