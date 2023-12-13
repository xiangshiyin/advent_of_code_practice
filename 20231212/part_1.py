import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# process the input
rows = []
damage_counts = []

with open("20231212_input_example.txt") as f:
    for line in f:
        rows.append(line.strip().split()[0])
        damage_counts.append([
            int(value)
            for value in line.strip().split()[1].split(",")
        ])

print(rows)
print(damage_counts)

n_rows = len(rows)
n_cols = len(rows[0])
# step 1: count the number of damages after every position
damage_counts_ranges = [[] for _ in range(n_rows)]
for r in range(n_rows):
    for c in range(n_cols):
        temp = [1,1] if rows[r][c] == "#" else [0,1] if rows[r][c] == "?" else [0,0]
        if c == 0:
            damage_counts_ranges[r].append(temp)
        else:
            damage_counts_ranges[r].append([
                damage_counts_ranges[r][c-1][0] + temp[0],
                damage_counts_ranges[r][c-1][1] + temp[1]
            ])
#         if rows[r][c] == "#":
#             damage_counts_from[r][c] = 1
#             if c < n_cols - 1:
#                 damage_counts_from[r][c] += damage_counts_from[r][c+1]
print(damage_counts_from)
