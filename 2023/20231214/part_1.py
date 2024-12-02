import os

os.chdir(os.path.dirname(__file__))

# with open("20231214_input_example.txt", "r") as f:
with open("20231214_input.txt", "r") as f:
    input = f.read().splitlines()

# print(input)

# step 1: build the grid of weights (with transposed coordinates)
# n_rows = len(input)
# n_cols = len(input[0])
transposed = []

for i in range(len(input[0])):
    transposed.append([input[j][i] for j in range(len(input))])

# step 2: move round rocks left
n_rows = len(transposed)
n_cols = len(transposed[0])

for i in range(n_rows):
    # print(f"row {i} before: {transposed[i]}")
    start = -1
    round_rocks_found = 0
    for j in range(n_cols):
        if transposed[i][j] == '#':
            start = j
            round_rocks_found = 0
        elif transposed[i][j] == 'O':
            round_rocks_found += 1
            space = j - start
            # print(f"row {i}, col {j}, start:{start}, round rocks found: {round_rocks_found}, space: {space}")
            if space > round_rocks_found:
                transposed[i][start + round_rocks_found] = 'O'
                transposed[i][j] = '.'
    # print(f"row {i} after: {transposed[i]}")


# step 3: calculate the weight of each round rock 'O' and sum them up
total_weight = 0
for i in range(n_rows):
    for j in range(n_cols):
        if transposed[i][j] == 'O':
            total_weight += n_cols - j

print(f"total weight: {total_weight}")

