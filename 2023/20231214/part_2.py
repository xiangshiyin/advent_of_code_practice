""" 
This takes forever to fnish. I think I need to find a way to optimize the tilt function.
"""
import os
from tqdm import tqdm
from collections import defaultdict

os.chdir(os.path.dirname(__file__))

input = []
# with open("20231214_input_example.txt", "r") as f:
with open("20231214_input.txt", "r") as f:
    for line in f:
        input.append([col for col in line.strip()])

print(f"n_rows: {len(input)}, n_cols: {len(input[0])}")

# tilt the matrix following the order north --> west --> south --> east
operations = [
    (-1, 0), # north
    (0, -1), # west
    (1, 0), # south
    (0, 1), # east
]

def tilt(matrix, operation):
    dr, dc = operation
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    lowest = []
    if dr != 0:
        for i in range(n_rows)[::(-1 *dr)]:
            if not lowest:
                lowest = [i if matrix[i][j] in ['O', '#'] else i + dr for j in range(n_cols)]
                continue
            for j in range(n_cols):
                if matrix[i][j] == "#":
                    lowest[j] = i
                elif matrix[i][j] == "O":
                    matrix[i][j] = "."
                    matrix[lowest[j] - dr][j] = "O"
                    lowest[j] -= dr

    if dc != 0:
        for j in range(n_cols)[::(-1 *dc)]:
            if not lowest:
                lowest = [j if matrix[i][j] in ['O', '#'] else j + dc for i in range(n_rows)]
                continue
            for i in range(n_rows):
                if matrix[i][j] == "#":
                    lowest[i] = j
                elif matrix[i][j] == "O":
                    matrix[i][j] = "."
                    matrix[i][lowest[i] - dc] = "O"
                    lowest[i] -= dc
        

def calculate_weight(matrix):
    """Total load on the north support beam"""
    total_weight = 0
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] == "O":
                total_weight += n_rows - i


    return total_weight                    

def to_string(matrix):
    return '\n'.join([''.join(line) for line in matrix])

matrix = input.copy()


cycles = 1000000000
# cycles = 10000000
# cycles = 3

def rotate(matrix, cycles):
    seen = defaultdict(list)
    pattern_repeated = ''
    for i in tqdm(range(cycles), ncols=70):
        for j in range(4):
            tilt(matrix, operations[j])
        hash = to_string(matrix)
        seen[hash].append(i + 1)
        if len(seen[hash]) == 3:
            # print(f"Cycle detected when hash = {hash}\nCorresponding cycles: {seen[hash]}, cycle period: {seen[hash][-1] - seen[hash][-2]}")
            pattern_repeated = hash
            print(f"Stopped at cycle {i + 1}")
            break

    cycle_period = seen[pattern_repeated][-1] - seen[pattern_repeated][-2]
    cycles_residual = (cycles - seen[pattern_repeated][-1]) % cycle_period
    print(f"cycles_residual: {cycles_residual}")

    for i in tqdm(range(cycles_residual), ncols=70):
        for j in range(4):
            tilt(matrix, operations[j])

rotate(matrix, cycles)

total_weight = calculate_weight(matrix)
print(f"Total load on the north support beam: {total_weight}")

# print(f"After the tilt:")
# for line in matrix:
#     print(' '.join(line))
