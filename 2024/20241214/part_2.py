import os
import sys
import time
import re
from tqdm import tqdm

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
        print("".join('.' if cell == 0 else str(cell) for cell in row))

# 3. Move the bots and count the number of bots in each position
if use_example:
    nrows, ncols = 7, 11
    seconds = 100
else:
    nrows, ncols = 103, 101
    seconds = 100

def move_bots(bots, seconds):
    grid = [[0] * ncols for _ in range(nrows)]
    for pr, pc, vr, vc in bots:
        pr, pc = move_a_bot(pr, pc, vr, vc, nrows, ncols, seconds)
        grid[pr][pc] += 1    
    return grid

# 4, Get the safe factor
def get_safe_factor(grid):
    middle_row, middle_col = nrows // 2, ncols // 2
    quadrants = [0] * 4
    for i in range(nrows):
        for j in range(ncols):
            if i == middle_row or j == middle_col:
                continue
            quadrants[
                2 * (0 if i < middle_row else 1) + (0 if j < middle_col else 1)
            ] += grid[i][j]
    safe_factor = 1
    for i in range(4):
        safe_factor *= quadrants[i]
    return safe_factor, quadrants

# safe_factor, quadrants = get_safe_factor(move_bots(bots, seconds))
# print(safe_factor)
# print(quadrants)

# 5. Find the the mininum value of the safe factor and the corresponding seconds
min_sf = float('inf')
min_sf_seconds = None
for i in tqdm(range(nrows * ncols)):
    grid = move_bots(bots, i)
    sf, _ = get_safe_factor(grid)
    if sf < min_sf:
        min_sf = sf
        min_sf_seconds = i

print(min_sf_seconds)

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
