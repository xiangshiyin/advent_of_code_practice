
import os
import sys

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241209_input_example.txt" if use_example else "20241209_input.txt"
grid = []
with open(path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))
