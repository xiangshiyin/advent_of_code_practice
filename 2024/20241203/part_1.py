import os
import re

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
rows = []
# with open("20241203_input_example.txt", "r") as file:
with open("20241203_input.txt", "r") as file:
    for line in file:
        rows.extend(re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line))

# 2. do the math
result = 0
for row in rows:
    result += int(row[0]) * int(row[1])
print(result)
