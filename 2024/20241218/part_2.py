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

def bfs(fallen_bytes, nrows, ncols):
    q = deque([(0, 0, 0)])
    visited = set([(0, 0)])

    while q:
        cr, cc, step = q.popleft()
        if (cr, cc) == (nrows - 1, ncols - 1):
            print(f"Shortest distance: {step}")
            return True
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < nrows and 0 <= nc < ncols and (nr, nc) not in visited and (nr, nc) not in fallen_bytes:
                q.append((nr, nc, step + 1))
                visited.add((nr, nc))
    return False

# brutal force
fallen_bytes = bytes[:2856]
print(f"Number of fallen bytes: {len(fallen_bytes)}")
print(bfs(fallen_bytes, nrows, ncols))
print(fallen_bytes[-1][::-1])


#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
