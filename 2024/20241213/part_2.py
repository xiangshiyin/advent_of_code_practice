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
    map(int, group)
    for group in re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", file_content)
    
]

# 3. Calculate the minimum number of tokens to push the A and B buttons to get to the prize
def solve(group):
    """
    Solve the following equations for (x, y):
    ax + by = c
    dx + ey = f
    """
    a, d, b, e, c, f = group
    if a * e - b * d == 0:
        if c * e != f * b:
            return -1, -1
        else:
            for x in range(c // a + 1):
                for y in range(f //d + 1):
                    if (3 * b - a) * x + c > 0 and (a - 3 * b) * y + 3 * c > 0 and ((3 * b - a) * x + c) % b == 0 and ((a - 3 * b) * y + 3 * c) % a == 0:
                        return x, y
                    elif (3 * b - a) * x + c < 0 or (a - 3 * b) * y + 3 * c < 0:
                        return -1, -1

    elif (c * e - f * b) % (a * e - b * d) == 0 and (f * a - c * d) % (a * e - b * d) == 0:
        return (c * e - f * b) // (a * e - b * d), (f * a - c * d) // (a * e - b * d)
    else:
        return -1, -1

total_tokens = 0
group_id = 0
for ax, ay, bx, by, px, py in groups:
    px += 10000000000000
    py += 10000000000000
    x, y = solve([ax, ay, bx, by, px, py])
    if x != -1 and y != -1:
        total_tokens += 3 * x + y
        print(f"Group {group_id}, move {x} times button A and {y} times button B to get to the prize")
    group_id += 1

print(total_tokens)


#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")