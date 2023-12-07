import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

numbers_all = []
with open("20231203_input_example.txt", "r") as f:
    for line in f:
        numbers = []
        matches = re.finditer(r"(\d+)", line)
        for match in matches:
            numbers.append([
                match.group(),
                match.start(),
                match.end()
            ])
        numbers_all.extend(numbers)

print(numbers_all)