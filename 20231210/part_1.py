import os
from collections import deque

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# with open("20231210_input_example_2.txt", "r") as f:
with open("20231210_input_example_1.txt", "r") as f:
# with open("20231210_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

print(f"Number of lines: {len(lines)}")

# find S
start = []
for line in lines:
    if "S" in line:
        start.append(lines.index(line))
        start.append(line.index("S"))
        break

print(f"Start: {start}")

# build the grids
n_rows = len(lines)
n_cols = len(lines[0])
grids = [['.'] * n_cols for i in range(n_rows)]
visited = [[0] * n_cols for i in range(n_rows)]
grids[start[0]][start[1]] = 0
visited[start[0]][start[1]] = 1

# traverse the grids
queue = deque([start])
# neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
moves_to_symbols = {
    (1, 0): ["|", "L", "J"],
    (-1, 0): ["|", "7", "F"],
    (0, 1): ["-", "J", "7"],
    (0, -1): ["-", "L", "F"]
}
moves_qualified = {
    "|": [(1,0), (-1,0)],
    "-": [(0,1), (0,-1)],
    "L": [(0,1), (-1,0)],
    "J": [(0,-1), (-1,0)],
    "7": [(0,-1), (1,0)],
    "F": [(0,1), (1,0)],
    "S": [(1,0), (-1,0), (0,1), (0,-1)]
}

farthest = 0
while queue:
    r_curr, c_curr = queue.popleft()
    # print(f"Current: {r_curr}, {c_curr}")
    for r_move, c_move in moves_to_symbols:
        r_next = r_curr + r_move
        c_next = c_curr + c_move
        if (r_move, c_move) in moves_qualified[lines[r_curr][c_curr]] and 0 <= r_next < n_rows and 0 <= c_next < n_cols:
            if lines[r_next][c_next] in moves_to_symbols[(r_move, c_move)] and not visited[r_next][c_next]:
                visited[r_next][c_next] = 1
                grids[r_next][c_next] = grids[r_curr][c_curr] + 1
                if grids[r_next][c_next] > farthest:
                    farthest = grids[r_next][c_next]
                queue.append([r_next, c_next])

# for line in visited:
for line in grids:
    print('|'.join(
        [str(x).ljust(2,' ') for x in line]
    ))
print(f"Farthest: {farthest}")