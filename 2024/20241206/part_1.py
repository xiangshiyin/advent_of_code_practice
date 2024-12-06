import os

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = False
path = "20241206_input_example.txt" if use_example else "20241206_input.txt"
grids = []
with open(path, "r") as file:
    for line in file:
        grids.append(line.strip())

# print(grids)

# guard is represented by ^, obstacles are represented by #
nrows, ncols = len(grids), len(grids[0])
# whenever the guard reaches an obstacle, it turns 90 degrees clockwise
# otherwise, it moves straight based upon the current direction
# mark the positions the guard visits with letter X
# find all the positions the guard will be at before she leaves the grid

# 2.Find initial position of the guard
r, c = 0, 0
for i in range(nrows):
    for j in range(ncols):
        if grids[i][j] == "^":
            r, c = i, j
            break

# 3. Find all the positions the guard will be at before she leaves the grid
drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while True:
    grids[r] = grids[r][:c] + "X" + grids[r][c + 1 :]
    r_next, c_next = r + drc[0][0], c + drc[0][1]
    if r_next < 0 or r_next >= nrows or c_next < 0 or c_next >= ncols:
        break
    if grids[r_next][c_next] == "#":
        drc.append(drc.pop(0))
        continue
    else:
        r, c = r_next, c_next

# print(grids)

# 4. Count the number of X's in the grids
print(sum(row.count("X") for row in grids))
