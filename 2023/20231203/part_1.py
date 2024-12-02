import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

numbers_found = []
# with open("20231203_input_example.txt", "r") as f:
with open("20231203_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
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
        numbers_found.extend(numbers)
        # print(line)

# print(numbers_found)

# filter qualified numbers
n_cols = len(lines[0])
n_rows = len(lines)
print(f"n_cols: {n_cols}, n_rows: {n_rows}")
qualified_numbers = []
disqualified_numbers_by_row = {i:[] for i in range(n_rows)}

for number, row, start, end in numbers_found:
    above = lines[row - 1][max(0, start-1):min(n_cols, end+1)] if row > 0 else "."
    below = lines[row + 1][max(0, start-1):min(n_cols, end+1)] if row < n_rows - 1 else "."
    left = lines[row][start-1] if start > 0 else "."
    right = lines[row][end] if end < n_cols else "."

    if (
        above == "." * len(above) and
        below == "." * len(below) and
        left == "." and
        right == "."
    ):
        disqualified_numbers_by_row[row].append(number)
        print(f"{above}\n{left}{number}{right}\n{below}")
        continue
    else:
        qualified_numbers.append(number)

# print(qualified_numbers)
print(f"Answer: {sum([int(n) for n in qualified_numbers])}")
print(f"Disqualified numbers by row: {disqualified_numbers_by_row}")


