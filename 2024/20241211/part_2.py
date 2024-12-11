"""
Dramatically slow down after 41 rounds
"""
import os
import sys
import time
from tqdm import tqdm
from functools import lru_cache

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
debug = '--debug' in sys.argv
path = "20241211_input_example.txt" if use_example else "20241211_input.txt"
grid = []
with open(path, "r") as file:
    for line in file:
        grid.extend(line.split())

# 2. Define the blink function with caching
@lru_cache(maxsize=None)
def blink(number):
    if int(number) == 0:
        return ['1']
    elif len(number) % 2 == 0:
        return [number[:len(number)//2], str(int(number[len(number)//2:]))]
    else:
        return [str(int(number) * 2024)]
    
# 3. Apply the blink function to the grid
round = 0

if debug:
    print(f"Initial grid: {grid}")

for round in tqdm(range(75), desc="Processing rounds"):
    tmp = []
    for number in grid:
        tmp.extend(blink(number))
    grid = tmp
    if debug:
        print(f"After round {round}: {grid}")

print(len(grid))
#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")