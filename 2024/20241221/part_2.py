import os
import sys
import time

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241221_input_example.txt" if use_example else "20241221_input.txt"
grid = []
with open(path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")