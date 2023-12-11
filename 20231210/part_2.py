import os
from collections import deque

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# with open("20231210_input_example_5.txt", "r") as f:
# with open("20231210_input_example_4.txt", "r") as f:
# with open("20231210_input_example_3.txt", "r") as f:
with open("20231210_input.txt", "r") as f:
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
# neighbors = [[1, 0], [0, -1], [-1, 0], [0, 1]]
nexts_qualified = {
    (1, 0): ["|", "L", "J"],
    (-1, 0): ["|", "7", "F"],
    (0, -1): ["-", "L", "F"],
    (0, 1): ["-", "J", "7"]
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

# step 1: find the farthest point and mark the loop
farthest = 0
while queue:
    r_curr, c_curr = queue.popleft()
    # print(f"Current: {r_curr}, {c_curr}")
    for r_move, c_move in nexts_qualified:
        r_next = r_curr + r_move
        c_next = c_curr + c_move
        if (r_move, c_move) in moves_qualified[lines[r_curr][c_curr]] and 0 <= r_next < n_rows and 0 <= c_next < n_cols:
            if lines[r_next][c_next] in nexts_qualified[(r_move, c_move)] and not visited[r_next][c_next]:
                visited[r_next][c_next] = 1
                grids[r_next][c_next] = grids[r_curr][c_curr] + 1
                if grids[r_next][c_next] > farthest:
                    farthest = grids[r_next][c_next]
                queue.append([r_next, c_next])

# # for line in visited:
# for line in grids:
#     print('|'.join(
#         [str(x).ljust(3,' ') for x in line]
#     ))
# print(f"Farthest: {farthest}")

# step 2: trace the loop
visited2 = [[0] * n_cols for i in range(n_rows)]
queue = []
queue.append(start)
loop_trace = []
loop_found = 0
while queue:
    r_curr, c_curr = queue.pop()
    visited2[r_curr][c_curr] = 1
    loop_trace.append([r_curr, c_curr])
    # print(f"Current: {r_curr}, {c_curr}")
    for r_move, c_move in nexts_qualified:
        r_next = r_curr + r_move
        c_next = c_curr + c_move
        if (r_move, c_move) in moves_qualified[lines[r_curr][c_curr]] and 0 <= r_next < n_rows and 0 <= c_next < n_cols:
            if lines[r_next][c_next] in nexts_qualified[(r_move, c_move)] and not visited2[r_next][c_next]:
                queue.append([r_next, c_next])   
    if loop_found:
        break

# print(f"Loop trace: {loop_trace}")

## visualize the loop
grids2 = [['.'] * n_cols for i in range(n_rows)]
for idx, rc in enumerate(loop_trace):
    grids2[rc[0]][rc[1]] = idx

for line in grids2:
    print('|'.join(
        [str(x).ljust(3,' ') for x in line]
    ))

# step 3: use winding number to find the number of loops
def winding_number(point, polygon):
    count = 0
    for i in range(len(polygon)):
        p1 = polygon[i - 1]
        p2 = polygon[i]
        if p1[1] <= point[1] < p2[1] and (point[1] - p1[1]) * (p2[0] - p1[0]) > (point[0] - p1[0]) * (p2[1] - p1[1]):
            count += 1
        elif p2[1] <= point[1] < p1[1] and (point[1] - p1[1]) * (p2[0] - p1[0]) < (point[0] - p1[0]) * (p2[1] - p1[1]):
            count -= 1
    return count


answer = 0
for i in range(n_rows):
    for j in range(n_cols):
        counter = 0
        if grids[i][j] == '.':
            if winding_number([i, j], loop_trace) != 0:
                counter += 1
        if counter > 0:
            answer += 1
            grids[i][j] = 'X'

print(f"Answer: {answer}")

# for line in grids:
#     print('|'.join(
#         [str(x).ljust(2,' ') for x in line]
#     ))