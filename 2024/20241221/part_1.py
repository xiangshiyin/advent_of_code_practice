import os
import sys
import time
from collections import deque, defaultdict

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = "--example" in sys.argv
path = "20241221_input_example.txt" if use_example else "20241221_input.txt"
lines = []
with open(path, "r") as file:
    for line in file:
        lines.append(line.strip())

num_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]
dir_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]


def get_all_shortest_seqs(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r, c)
    seqs = defaultdict(list)
    # find the shortest path between any pair of positions
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            q = deque([(pos[x], "")])
            # visited = set([pos[x]])
            min_moves = float("inf")
            while q:
                (r, c), moves = q.popleft()
                if min_moves < len(moves) + 1:
                    break
                for nr, nc, nm in [
                    (r - 1, c, "^"),
                    (r + 1, c, "v"),
                    (r, c - 1, "<"),
                    (r, c + 1, ">"),
                ]:
                    if (
                        0 <= nr < len(keypad)
                        and 0 <= nc < len(keypad[r])
                        and keypad[nr][nc] is not None
                        # and (nr, nc) not in visited
                    ):
                        if keypad[nr][nc] == y:
                            seqs[(x, y)].append(moves + nm + "A")
                            min_moves = len(moves) + 1
                            # print(f"{x} -> {y}: {moves + nm + 'A'}")
                        else:
                            q.append(((nr, nc), moves + nm))
                            # visited.add((nr, nc))
    return seqs


shortest_seqs_num = get_all_shortest_seqs(num_keypad)
shortest_seqs_dir = get_all_shortest_seqs(dir_keypad)

# print(shortest_seqs_num)

code = "A029A"
for i in range(len(code) - 1):
    print(f"{code[i]} -> {code[i+1]}")
    print(shortest_seqs_num[(code[i], code[i + 1])])

# for line in lines:
#     print(line)
#     solve(line, num_keypad)


#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
