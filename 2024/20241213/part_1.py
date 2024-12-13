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
path = "20241213_input_example.txt" if use_example else "20241213_input.txt"
file_content = open(path, "r").read()

# 2. Extract the steps for button A and button B and the (x, y) coordinates of the prize
groups = [
    list(map(int, group))
    for group in re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", file_content)
    
]

# 3. Calculate the minimum number of tokens to push the A and B buttons to get to the prize
total_tokens = 0
group_id = 0
for ax, ay, bx, by, px, py in groups:
    min_tokens = float('inf')
    for i in range(100 + 1):
        for j in range(100 + 1):
            if ax * i + bx * j == px and ay * i + by * j == py:
                min_tokens = min(min_tokens, 3 * i + j)
    if min_tokens != float('inf'):
        print(f"Group {group_id}, move {i} times button A and {j} times button B to get to the prize")
        total_tokens += min_tokens
    group_id += 1

print(total_tokens)

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")