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
def get_num_edges(positions, direction):
    """
    Given a list of positions, find the number of segments, segments are defined as connected positions, such as [(0,1), (0,2), (0,3)], or [(1,0), (2,0), (3,0)]
    - If the direction is horizontal, find the number of segments in the horizontal direction
    - If the direction is vertical, find the number of segments in the vertical direction
    """
    axis_index = 0 if direction == 'h' else 1
    positions_sorted = sorted(positions, key=lambda x: (x[axis_index], x[1-axis_index]))
    counter = 0
    for i, pos in enumerate(positions_sorted):
        if i == 0:
            counter += 1
        elif pos[axis_index] != positions_sorted[i - 1][axis_index]:
            counter += 1
        elif pos[1-axis_index] != positions_sorted[i - 1][1-axis_index] + 1:
            counter += 1
    return counter


drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
regions = defaultdict(list)

for r in range(nrows):
    for c in range(ncols):
        if visited[r][c] == 0:
            # a new region
            region_id = rows[r][c]
            region_spot_count = 0
            queue = deque([(r, c)])
            visited[r][c] = 1
            boundaries = defaultdict(list) # record all the boundaries so we can merge them later to find the number of sides
            # BFS to find all the connected spots
            while queue:
                cr, cc = queue.popleft()
                region_spot_count += 1
                # Check the 4 directions of the current spot, if it's on the edge or next to a different region, record the boundaries
                # region_perimeter += sum(
                #     1 for dr, dc in drc if not (0 <= cr + dr < nrows and 0 <= cc + dc < ncols) or rows[cr + dr][cc + dc] != region_id
                # )
                for dr, dc in drc:
                    if not (0 <= cr + dr < nrows and 0 <= cc + dc < ncols) or rows[cr + dr][cc + dc] != region_id:
                        boundaries[(dc, dr)].append((cr, cc))
                for dr, dc in drc:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < nrows and 0 <= nc < ncols and visited[nr][nc] == 0 and rows[nr][nc] == region_id:
                        queue.append((nr, nc))
                        visited[nr][nc] = 1
            num_sides = sum([
                get_num_edges(boundaries[dr, dc], 'h' if dr == 0 else 'v')
                for dr, dc in boundaries.keys()
            ])
            print(f"region_id: {region_id}, region_spot_count: {region_spot_count}, num_sides: {num_sides}")
            regions[region_id].append((region_spot_count, num_sides))

# print(regions)

# 4. Calculate the total price
total_price = sum(region_spot_count * num_sides for region in regions.values() for region_spot_count, num_sides in region)
print(total_price)

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
