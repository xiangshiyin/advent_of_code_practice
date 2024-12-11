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

# 2. Define the blink function using dynamic programming
@lru_cache(maxsize=None)
def output_length(number, rounds_to_go):
    if rounds_to_go == 0:
        # print(number)
        return 1
    else:
        if number == '0':
            return output_length('1', rounds_to_go - 1)
        elif len(number) % 2 == 0:
            return output_length(number[:len(number)//2], rounds_to_go - 1) + output_length(str(int(number[len(number)//2:])), rounds_to_go - 1)
        else:
            return output_length(str(int(number) * 2024), rounds_to_go - 1)


# 3. Test the function
# print(grid)
# print(output_length('125', 6))
# print(output_length('17', 6))

# 4. Run the full list of numbers
counter = 0
for number in grid:
    counter += output_length(number, 75)
print(counter)

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")