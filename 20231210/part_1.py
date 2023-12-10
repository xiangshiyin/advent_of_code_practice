import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

symbols = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[1, 1]],
    "J": [[1, -1]],
    "7": [[-1, -1]],
    "F": [[-1, 1]],
}

with open("20231210_input_example_1.txt", "r") as f:
    # with open("20231210_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

print(f"Number of lines: {len(lines)}")

# build the grids
n_rows = len(lines)
n_cols = len(lines[0])
grids = [[-1] * n_cols for i in range(n_rows)]
visited = [[0] * n_cols for i in range(n_rows)]

# find S
start = []
for line in lines:
    if "S" in line:
        start.append(line.index("S"))
        start.append(lines.index(line))
        break

print(f"Start: {start}")

# traverse the grids
stack = [start]
neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while stack:
    r_curr, c_curr = stack.pop()
    print(f"Current: {r_curr}, {c_curr}")
    for dr, dc in neighbors:
        r = r_curr + dr
        c = c_curr + dc
        if 0 <= r < n_rows and 0 <= c < n_cols and visited[r][c] == 0:
            if (
                (
                    lines[r][c] == "|"
                    and r > r_curr
                    and lines[r_curr][c_curr] not in ["J", "L"]
                )
                or (
                    lines[r][c] == "|"
                    and r < r_curr
                    and lines[r_curr][c_curr] not in ["7", "F"]
                )
                or (
                    lines[r][c] == "-"
                    and c > c_curr
                    and lines[r_curr][c_curr] not in ["|", "7"]
                )
                or (
                    lines[r][c] == "L"
                    and r > r_curr
                    and lines[r_curr][c_curr] not in ["-", "J", "L"]
                )
                or (
                    lines[r][c] == "J"
                    and r > r_curr
                    and lines[r_curr][c_curr] not in ["-", "J", "L"]
                )
                or (
                    lines[r][c] == "7"
                    and r < r_curr
                    and lines[r_curr][c_curr] not in ["-", "7", "F"]
                )
                or (
                    lines[r][c] == "F"
                    and r < r_curr
                    and lines[r_curr][c_curr] not in ["-", "7", "F"]
                )
            ):
                grids[r][c] = grids[r_curr][c_curr] + 1
                stack.append([r, c])
                visited[r][c] = 1
