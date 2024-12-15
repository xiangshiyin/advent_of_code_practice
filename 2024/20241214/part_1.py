import os
import sys
import time
import re

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241214_input_example.txt" if use_example else "20241214_input.txt"
bots = []
with open(path, "r") as file:
    for line in file:
        pc, pr, vc, vr = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()
        bots.append((int(pr), int(pc),int(vr), int(vc)))

# print(bots)

# 2. Define the function to move the bots
def move_a_bot(pr, pc, vr, vc, nrows, ncols, steps):
    for i in range(steps + 1):
        if i == 0:
            # print(f"After {i} seconds: Position: ({pr}, {pc})")
            continue
        else:
            pc += vc
            pr += vr

            pr = nrows - abs(pr) % nrows if pr < 0 else abs(pr) % nrows if pr >= nrows else pr
            pc = ncols - abs(pc) % ncols if pc < 0 else abs(pc) % ncols if pc >= ncols else pc
    # print(f"After {steps} seconds: Position: ({pr}, {pc})")
    return pr, pc

def print_grid(grid):
    for row in grid:
        print("|".join(str(cell) for cell in row))

# 3. Move the bots and count the number of bots in each position
if use_example:
    nrows, ncols = 7, 11
    seconds = 100
else:
    nrows, ncols = 103, 101
    seconds = 100
grid = [[0] * ncols for _ in range(nrows)]

for pr, pc, vr, vc in bots:
    pr, pc = move_a_bot(pr, pc, vr, vc, nrows, ncols, seconds)
    grid[pr][pc] += 1    

# print_grid(grid)

# 4, Find out the number of bots in each quadrant (ignore the middle row and column)
middle_row, middle_col = nrows // 2, ncols // 2
quadrants = [0] * 4

for i in range(nrows):
    for j in range(ncols):
        if i == middle_row or j == middle_col:
            continue
        quadrants[
            2 * (0 if i < middle_row else 1) + (0 if j < middle_col else 1)
        ] += grid[i][j]

# 5. Calculate the safe factor
safe_factor = 1
for i in range(4):
    safe_factor *= quadrants[i]

print(safe_factor)

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")