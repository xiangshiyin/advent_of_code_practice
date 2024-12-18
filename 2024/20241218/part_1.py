import os
import sys
import time
from collections import deque

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241218_input_example.txt" if use_example else "20241218_input.txt"
bytes = []
with open(path, "r") as file:
    for line in file:
        bytes.append(tuple(map(int, line.strip().split(',')))[::-1])

print(f"Number of bytes: {len(bytes)}")
# 2. Find the shortest distance between the entrance and the exit
nrows = 7 if use_example else 71
ncols = 7 if use_example else 71

fallen_bytes = set(bytes[:1024])
# print(fallen_bytes)

for r in range(nrows):
    row = ['.' for _ in range(ncols)]
    for c in range(ncols):
        if (r, c) in fallen_bytes:
            row[c] = '#'
    print(''.join(row))

q = deque([(0, 0, 0)])
visited = set([(0, 0)])
backtrack = {(0, 0): (None, None)}
found_exit = False

while q:
    cr, cc, step = q.popleft()
    if (cr, cc) == (nrows - 1, ncols - 1):
        print(f"Shortest distance: {step}")
        found_exit = True
        break
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < nrows and 0 <= nc < ncols and (nr, nc) not in visited and (nr, nc) not in fallen_bytes:
            q.append((nr, nc, step + 1))
            visited.add((nr, nc))
            backtrack[(nr, nc)] = (cr, cc)

if not found_exit:
    print("No path to the exit was found.")

print(cr, cc)
# print(backtrack)
# # print out the shortest path
# curr = (nrows-1, ncols-1)
# while curr != (0,0):
#     print(curr)
#     curr = backtrack[curr]
# print(curr)

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
