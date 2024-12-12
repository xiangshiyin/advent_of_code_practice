import os
import sys
import time
from collections import deque, defaultdict

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241212_input_example.txt" if use_example else "20241212_input.txt"
rows = []
with open(path, "r") as file:
    for line in file:
        rows.append(line.strip())

nrows, ncols = len(rows), len(rows[0])
print(nrows, ncols)

# 2. Build a grid to record visited spots
visited = [[0] * ncols for _ in range(nrows)]
# print(visited)

# 3. Use BFS to find all the regions where the spots are connected and have the same letter
"""
Under the bulk discount, instead of using the perimeter to calculate the price, you need to use the number of sides each region has. 
Each straight section of fence counts as a side, regardless of how long it is.
"""
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
regions = defaultdict(list)

for r in range(nrows):
    for c in range(ncols):
        if visited[r][c] == 0:
            region_id = rows[r][c]
            subregion = []
            queue = deque([(r, c)])
            visited[r][c] = 1
            # BFS to find all the connected spots
            while queue:
                cr, cc = queue.popleft()
                subregion.append((cr, cc))
                for dr, dc in drc:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < nrows and 0 <= nc < ncols and visited[nr][nc] == 0 and rows[nr][nc] == region_id:
                        queue.append((nr, nc))
                        visited[nr][nc] = 1
            # Sort the subregion by the row number, then by the column number
            subregion.sort(key=lambda x: (x[0], x[1]))
            regions[region_id].append(subregion)

print(regions)

# 4. Traverse each region, count the number of spots and the number of sides based upon direction changes
def direction(current_pos, next_pos):
    return (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])

## 4.1 Find all the boundary points
def find_boundary_points(subregion):
    boundary_points = []
    for r, c in subregion:
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in subregion:
                boundary_points.append((r, c))
                break
    return boundary_points
    

# # 4. Calculate the total price
# total_price = sum(region_spot_count * region_perimeter for region in regions.values() for region_spot_count, region_perimeter in region)
# print(total_price)

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
