import os
import sys
from collections import defaultdict
import itertools

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241208_input_example.txt" if use_example else "20241208_input.txt"
grid = []
with open(path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))

# print(grid)

# 2. Find distance vector between two points
def find_distance_vector(start_pos, end_pos):
    start_r, start_c = start_pos
    end_r, end_c = end_pos
    return (end_r - start_r, end_c - start_c)

def find_target_position(start_pos, distance_vector):
    start_r, start_c = start_pos
    distance_r, distance_c = distance_vector
    return (start_r + distance_r, start_c + distance_c)

# 3. Find all the antennas and their positions
antennas = defaultdict(list)
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c].isalpha() or grid[r][c].isdigit():
            antennas[grid[r][c]].append((r, c))

# 4. Define a util function to find all the unique pairs from a list of positions
def find_unique_pairs(positions):
    return list(itertools.combinations(positions, 2))

# 5. For each kind of antenna, find the all the unique pairs of distances
nrows, ncols = len(grid), len(grid[0])
target_positions = set()
for antenna_type in antennas:
    pairs = find_unique_pairs(antennas[antenna_type])
    for pair in pairs:
        distance_vector = find_distance_vector(pair[0], pair[1])
        distance_vector_opposite = (-distance_vector[0], -distance_vector[1])
        pos1 = find_target_position(pair[1], distance_vector)
        pos2 = find_target_position(pair[0], distance_vector_opposite)
        if 0 <= pos1[0] < nrows and 0 <= pos1[1] < ncols:
            target_positions.add(pos1)
        if 0 <= pos2[0] < nrows and 0 <= pos2[1] < ncols:
            target_positions.add(pos2)

print(target_positions)
print(len(target_positions))

