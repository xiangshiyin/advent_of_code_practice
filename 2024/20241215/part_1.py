import os
import sys
import time

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
# path = "20241215_input_example.txt" if use_example else "20241215_input.txt"
initial_pos_path = "20241215_initial_pos_example.txt" if use_example else "20241215_initial_pos.txt"
moves_path = "20241215_moves_example.txt" if use_example else "20241215_moves.txt"

grid = []
with open(initial_pos_path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))

with open(moves_path, "r") as file:
    moves = file.read().strip().replace("\n", "")
print(moves)

# 2. Find the initial position of the bot
br, bc = None, None
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == "@":
            br, bc = r, c
            break
print(f"Initial position of the bot: {br}, {bc}")

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")