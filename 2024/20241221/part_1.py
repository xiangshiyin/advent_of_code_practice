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
codes = []
with open(path, "r") as file:
    for line in file:
        codes.append(line.strip())

door_keypad = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [None,"0","A"],
]
dir_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]

# 2. Solve the problem
def solve(code, keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r, c)




#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")