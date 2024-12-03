import os
import re

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
muls = []
enabled = True

with open("20241203_input.txt", "r") as file:
    for line in file:
        # Split the line into parts based on do() and don't() instructions
        parts = re.split(r"(do\(\)|don\'t\(\))", line)
        
        for part in parts:
            if part == "do()":
                enabled = True
            elif part == "don't()":
                enabled = False
            else:
                if enabled:
                    muls.extend(re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", part))

# 2. do the math
result = 0
for mul in muls:
    result += int(mul[0]) * int(mul[1])
print(result)
