import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def reach_zero_sequences(sequence):
    rows = []
    current_row = sequence.copy()
    while any(current_row):
        rows.append(current_row)
        next_row = []
        for idx in range(1, len(current_row)):
            next_row.append(current_row[idx] - current_row[idx - 1])
        current_row = next_row
        # print(rows)
    # back propogation and find the sum of interpolated values
    next_value = 0
    for row in rows[::-1]:
        next_value = row[0] - next_value
    # print(f"Answer: {next_value}")
    return next_value


        

sequences = []
# with open("20231209_input_example.txt", "r") as f:
with open("20231209_input.txt", "r") as f:
    for line in f:
        sequences.append([
            int(x) for x in line.strip().split(" ")
        ])

answer = 0
for sequence in sequences:
    answer += reach_zero_sequences(sequence)
print(f"Answer: {answer}")
