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
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
regions = defaultdict(list)

for r in range(nrows):
    for c in range(ncols):
        if visited[r][c] == 0:
            region_id = rows[r][c]
            region_spot_count = 0
            region_perimeter = 0
            queue = deque([(r, c)])
            visited[r][c] = 1
            # BFS to find all the connected spots
            while queue:
                cr, cc = queue.popleft()
                region_spot_count += 1
                # Check the 4 directions of the current spot, if it's on the edge or next to a different region, add to perimeter
                region_perimeter += sum(
                    1 for dr, dc in drc if not (0 <= cr + dr < nrows and 0 <= cc + dc < ncols) or rows[cr + dr][cc + dc] != region_id
                )
                for dr, dc in drc:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < nrows and 0 <= nc < ncols and visited[nr][nc] == 0 and rows[nr][nc] == region_id:
                        queue.append((nr, nc))
                        visited[nr][nc] = 1
            regions[region_id].append((region_spot_count, region_perimeter))

# print(regions)

# 4. Calculate the total price
total_price = sum(region_spot_count * region_perimeter for region in regions.values() for region_spot_count, region_perimeter in region)
print(total_price)

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
