import os
import copy

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = False
path = "20241206_input_example.txt" if use_example else "20241206_input.txt"
grids = []
with open(path, "r") as file:
    for line in file:
        grids.append(list(line.strip()))

# print(grids)

# guard is represented by ^, obstacles are represented by #
nrows, ncols = len(grids), len(grids[0])
# print(nrows, ncols)
# whenever the guard reaches an obstacle, it turns 90 degrees clockwise
# otherwise, it moves straight based upon the current direction
# mark the positions the guard visits with letter X
# add 1 obstacle to the grid so the guard will stuck in a loop
# count the number of positions the obstacle could be placed in the grid

# 2.Find initial position of the guard
r, c = 0, 0
for i in range(nrows):
    for j in range(ncols):
        if grids[i][j] == "^":
            r, c = i, j
            break
print(f"start position: {r}, {c}")

def find_loop(grids, r, c, r_0, c_0):
    """
    If the guard visits a position that has been visited before following the same direction,
    return True. Otherwise, return False.
    """
    drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    grids[r_0][c_0] = "#"
    while True:
        visited.add((r, c, drc[0]))
        r_next, c_next = r + drc[0][0], c + drc[0][1]
        if r_next < 0 or r_next >= nrows or c_next < 0 or c_next >= ncols:
            grids[r_0][c_0] = "."
            return False
        if grids[r_next][c_next] == "#":
            drc.append(drc.pop(0))
            continue
        else:
            r, c = r_next, c_next
            if (r, c, drc[0]) in visited:
                grids[r_0][c_0] = "."
                return True

# 3. Try all the positions the guard could be stuck in and count the number of new obstacle positions that could get the guard stuck
counter = 0
for i in range(nrows):
    for j in range(ncols):
        if grids[i][j] == "." and (i != r or j != c):
            if find_loop(grids, r, c, i, j):
                print(f"obstacle position: {i}, {j}")
                counter += 1
print(counter)
# print(find_loop(grids, r, c, 6, 3))