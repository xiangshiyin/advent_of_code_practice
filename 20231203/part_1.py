import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

rows_w_numbers = []
with open("20231203_input_example.txt", "r") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        numbers = []
        matches = re.finditer(r"(\d+)", line)
        for match in matches:
            numbers.append([
                match.group(),
                idx,
                match.start(),
                match.end()
            ])
        rows_w_numbers.extend(numbers)
        # print(line)

print(rows_w_numbers)

