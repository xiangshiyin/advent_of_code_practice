import os
import sys
import time
import re

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = "--example" in sys.argv
path = "20241214_input_example.txt" if use_example else "20241214_input.txt"
bots = []
with open(path, "r") as file:
    for line in file:
        pc, pr, vc, vr = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()
        bots.append((int(pr), int(pc), int(vr), int(vc)))

print(f"Number of bots: {len(bots)}")

# 2. Print the grid of bots' initial positions
if use_example:
    nrows, ncols = 7, 11
else:
    nrows, ncols = 103, 101

def print_grid(bots, nrows, ncols):
    grid = [["." for _ in range(ncols)] for _ in range(nrows)]
    for pr, pc, vr, vc in bots:
        grid[pr][pc] = "#"
    for row in grid:
        print("".join(row))
print_grid(bots, nrows, ncols)

# 3. Check if all bots are in unique positions
positions = set()
for pr, pc, vr, vc in bots:
    positions.add((pr, pc))
print(f"Number of unique positions: {len(positions)}")
print(f"Number of bots: {len(bots)}")

# 4. Find the second when all bots are in unique positions
second_range = nrows * ncols
for second in range(second_range + 1):
    positions = set()
    for pr, pc, vr, vc in bots:
        positions.add(
            (
                (pr + second * vr) % nrows,
                (pc + second * vc) % ncols,
                0,
                0,
            )
        )
    print(f"After {second} seconds, number of positions with bots: {len(positions)}")
    if len(positions) == len(bots):
        print(f"All bots are in unique position after {second} seconds")
        break

# 5. Print the grid of bots' positions after the second when all bots are in unique positions
print_grid(positions, nrows, ncols)
print(len(positions))

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
