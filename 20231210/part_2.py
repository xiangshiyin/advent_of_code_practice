import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# with open("20231210_input_example_5.txt", "r") as f:
# with open("20231210_input_example_4.txt", "r") as f:
# with open("20231210_input_example_3.txt", "r") as f:
with open("20231210_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

print(f"Number of lines: {len(lines)}")

# build the grids
n_rows = len(lines)
n_cols = len(lines[0])
visited = [[0] * n_cols for i in range(n_rows)]

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

# step 0: find S
start = []
for line in lines:
    if "S" in line:
        start.append(lines.index(line))
        start.append(line.index("S"))
        break

print(f"Start: {start}")

# step 1: traverse the grids from any point, find the main loop

queue = []
queue.append((start[0], start[1]))
visited[start[0]][start[1]] = 1

while queue:
    r, c = queue.pop()
    print(f"C: {r}, {c}, {lines[r][c]}, queue: {queue}")
    # choose one direction
    for r_move, c_move in moves_to_symbols:
        r_next = r + r_move
        c_next = c + c_move
        if (r_move, c_move) in moves_qualified[lines[r][c]] and 0 <= r_next < n_rows and 0 <= c_next < n_cols and lines[r_next][c_next] in moves_to_symbols[(r_move, c_move)]:
            if not visited[r_next][c_next]:
                queue.append((r_next, c_next))
                visited[r_next][c_next] = 1
                print(f"N: ({r_next}, {c_next}), {lines[r_next][c_next]}, moves: {(r_move, c_move)}")

# for line in visited:
#     print(line)

# step 2: find the closed areas
queue = []
visited2 = [[0] * n_cols for i in range(n_rows)]

qualified_tiles = 0
for i in range(n_rows):
    for j in range(n_cols):
        if visited[i][j] == 0 and not visited2[i][j]:
            queue.append((i, j))
            visited2[i][j] = 1
            counter = 0
            r_min, r_max, c_min, c_max = n_rows, 0, n_cols, 0
            while queue:
                r, c = queue.pop()
                counter += 1
                r_min = min(r_min, r)
                r_max = max(r_max, r)
                c_min = min(c_min, c)
                c_max = max(c_max, c)
                for r_move, c_move in moves_to_symbols:
                    r_next = r + r_move
                    c_next = c + c_move
                    if 0 <= r_next < n_rows and 0 <= c_next < n_cols and not visited2[r_next][c_next] and visited[r_next][c_next] == 0:
                        queue.append((r_next, c_next))
                        visited2[r_next][c_next] = 1
            if not (r_min == 0 or r_max == n_rows - 1 or c_min == 0 or c_max == n_cols - 1):        
                qualified_tiles += counter  
                print(f"Closed area started from ({i}, {j})!!")

for line in visited:
    print(line)

print(f"Qualified tiles: {qualified_tiles}")