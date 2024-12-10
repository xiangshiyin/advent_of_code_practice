import time
import os
import sys

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241210_input_example.txt" if use_example else "20241210_input.txt"
grid = []
with open(path, "r") as file:
    for line in file:
        grid.append([int(c) for c in line.strip()])

# print(grid)

# 2. find all candidates for being a trailhead
candidates = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            candidates.append((i, j))

# print(candidates)
# 3. iterate over all candidates, find all the candidates that can lead to a gradual and upward trail of height 9
## use a recursive function to find all the gradual and upward trails of height 9 from a candidate
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_all_paths(grid, pos, visited):
    r, c = pos
    if grid[r][c] == 9:
        return 1
    count = 0
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == grid[r][c] + 1:
            count += find_all_paths(grid, (nr, nc), visited + [(nr, nc)])    
    return count

total_scores = 0
for candidate in candidates:
    total_scores += find_all_paths(grid, candidate, [candidate])
print(total_scores)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
