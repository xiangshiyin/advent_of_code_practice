import os
import sys
import time
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
start_pos, end_pos = -1, -1
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == "S":
            start_pos = (r, c)
        elif cell == "E":
            end_pos = (r, c)
        if start_pos != -1 and end_pos != -1:
            break
print(f"Start position: {start_pos}")
print(f"End position: {end_pos}")

# 3. Find the cheapest path from start to end, 1 step corresponds to 1 point, 1 90 degree turn corresponds to 1000 points
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# Use DFS to find all the possible paths from the start position to the end position
valid_paths = []
def dfs(pos, path):
    if pos == end_pos:
        valid_paths.append(path)
        return
    for dr, dc in drc:
        nr, nc = pos[0] + dr, pos[1] + dc
        if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] != "#" and (nr, nc) not in path:
            dfs((nr, nc), path + [(nr, nc)])
    return

dfs(start_pos, [start_pos])

print(f"Number of valid paths: {len(valid_paths)}")

# 4. Calcualte the total cost of all the valid paths and find the minimum cost
def calculate_cost(path, diagnosis=False):
    cost = 0
    for i in range(len(path) - 1):
        if i == 0:
            next_dir = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
            delta = 1000 + 1 if next_dir != (0, 1) else 1
            cost += delta
            if diagnosis:
                print(f"Incremental cost at step {i} {path[i]} -> {path[i + 1]}: {delta}")
            continue
        curr, prev, next = path[i], path[i - 1], path[i + 1]
        curr_dir, next_dir = (curr[0] - prev[0], curr[1] - prev[1]), (next[0] - curr[0], next[1] - curr[1])
        delta = 1000 + 1 if curr_dir != next_dir else 1
        cost += delta
        if diagnosis:
            print(f"Incremental cost at step {i} {path[i]} -> {path[i + 1]}: {delta}")
    return cost

costs = [calculate_cost(path) for path in valid_paths]
min_cost = min(costs)
print(f"Minimum cost: {min_cost}")
# Find the path with the minimum cost
min_cost_path = valid_paths[costs.index(min_cost)]

# Print the path with the minimum cost
print("Path with the minimum cost:")
# print(calculate_cost(min_cost_path, diagnosis=True))



#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
