import os
import sys
import time
from tqdm import tqdm

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
initial_pos_path = "20241215_initial_pos_example.txt" if use_example else "20241215_initial_pos.txt"
moves_path = "20241215_moves_example.txt" if use_example else "20241215_moves.txt"

grid = []
# Augment the grid
with open(initial_pos_path, "r") as file:
    for line in file:
        grid.append(list(line.strip().replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")))

nrows, ncols = len(grid), len(grid[0])
print(f"Dimensions of the grid after augmentation: {nrows}x{ncols}")

def print_grid(grid):
    for row in grid:
        print("".join(row))

print_grid(grid)

with open(moves_path, "r") as file:
    moves = file.read().strip().replace("\n", "")

# 2. Find the initial position of the bot
br, bc = None, None
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == "@":
            br, bc = r, c
            break
print(f"Initial position of the bot: {br}, {bc}")

# 3. Find out the number of boxes and walls
boxes, walls = 0, 0
for row in grid:
    for cell in row:
        if cell == "O":
            boxes += 1
        elif cell == "#":
            walls += 1
print(f"Number of boxes: {boxes}, number of walls: {walls}, number of grid cells: {nrows * ncols}")

# 5. Simulate the moves
def print_grid(grid):
    for row in grid:
        print(*row, sep="")

for idx, move in enumerate(tqdm(moves)):
    dr = {"v": 1, "^": -1}.get(move, 0)
    dc = {">": 1, "<": -1}.get(move, 0)
    # print(f"Move {idx + 1}: {dr}, {dc} || Bot: {br}, {bc}")
    targets = [(br, bc)]
    cbr, cbc = br, bc
    go = True
    while True:
        cbr, cbc = cbr + dr, cbc + dc
        if grid[cbr][cbc] == "#":
            go = False
            break
        if grid[cbr][cbc] == "O":
            targets.append((cbr, cbc))
        if grid[cbr][cbc] == ".":
            break
    if not go: continue
    grid[br][bc] = "."
    grid[br + dr][bc + dc] = "@"
    for r, c in targets[1:]:
        grid[r + dr][c + dc] = "O"
    br, bc = br + dr, bc + dc
    # print(f"After move {idx + 1}:")
    # print_grid(grid)

# 6. Calculate the answer
print(
    sum(
        r * 100 + c
        for r in range(nrows)
        for c in range(ncols)
        if grid[r][c] == "O"
    )
)



#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")