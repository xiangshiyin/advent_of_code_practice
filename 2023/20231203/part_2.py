import os
import re
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

numbers_found = []  
# with open("20231203_input_example.txt", "r") as f:
with open("20231203_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    for idx, line in enumerate(lines):
        # find the numbers
        matches = re.finditer(r"(\d+)", line)
        for match in matches:
            numbers_found.append([
                int(match.group()),
                idx,
                match.start(),
                match.end()
            ])

# print(numbers_found)

# find stars
n_cols = len(lines[0])
stars = defaultdict(list)
for num, row, start, end in numbers_found:
    above = lines[row-1][max(0, start-1):min(n_cols, end+1)] if row > 0 else '.'
    below = lines[row+1][max(0, start-1):min(n_cols, end+1)] if row < len(lines)-1 else '.'
    left = lines[row][start-1] if start > 0 else '.'
    right = lines[row][end] if end < n_cols else '.'
    
    stars_above = re.finditer(r"\*", above)
    if stars_above:
        for star_above in stars_above:
            stars[(row-1, star_above.start() + max(0, start-1))].append(num)

    stars_below = re.finditer(r"\*", below) 
    if stars_below:
        for star_below in stars_below:
            stars[(row+1, star_below.start() + max(0, start-1))].append(num)

    if left == "*":
        stars[(row, start-1)].append(num)
    
    if right == "*":
        stars[(row, end)].append(num)

    # print(f"num: {num}, row: {row}, start: {start}, stars: {stars}")

# print(stars)

result = 0
for star in stars:
    if len(stars[star]) == 2:
        result += stars[star][0] * stars[star][1]
print(f"result: {result}")


