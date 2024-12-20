import os
import sys
import time
from functools import lru_cache
# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241219_input_example.txt" if use_example else "20241219_input.txt"
lines = []
with open(path, "r") as file:
    for line in file:
        lines.append(line.strip())

patterns = set([p.strip() for p in lines[0].split(',')])
designs = lines[2:]

# 2. Find the number of designs that can be made
maxlen = max(map(len, patterns))
print(f"maxlen: {maxlen}")

@lru_cache(maxsize=None)
def can_make_design(design):
    if design == "": return True
    for i in range(min(len(design), maxlen) + 1):
        if design[:i] in patterns and can_make_design(design[i:]):
            return True
    return False

counter = 0
for design in designs:
    if can_make_design(design):
        counter += 1
print(counter)
#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
