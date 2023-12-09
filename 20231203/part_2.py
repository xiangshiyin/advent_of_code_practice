import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

numbers_found = {}
stars_found = []    
with open("20231203_input_example.txt", "r") as f:
# with open("20231203_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    for idx, line in enumerate(lines):
        # find the numbers
        matches = re.finditer(r"(\d+)", line)
        for match in matches:
            if idx not in numbers_found:
                numbers_found[idx] = []
            numbers_found[idx].append([
                match.group(),
                match.start(),
                match.end()
            ])
        # find the stars
        starts = re.finditer(r"\*", line)
        for star in starts:
            stars_found.append([
                idx,
                star.start()
            ])

print(numbers_found)
print(stars_found)

n_cols = len(lines[0])

# find the gears
for star_row, star_col in stars_found:
    numbers_adjacent = []
    if star_row > 0:
        for number, number_start, number_end in numbers_found[star_row - 1]:
            if number_end > max(0, star_col-1) and number_start <= min(n_cols, star_col+1):
                numbers_adjacent.append(number)


