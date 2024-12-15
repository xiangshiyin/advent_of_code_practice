import os
import sys
import time
import re
from tqdm import tqdm

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_time = time.time()
#####################################################
# 1. Read the input file
use_example = "--example" in sys.argv
path = "20241214_input_example.txt" if use_example else "20241214_input.txt"
bots = []
with open(path, "r") as file:
    for line in file:
        pc, pr, vc, vr = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()
        bots.append((int(pr), int(pc), int(vr), int(vc)))

# print(bots)

if use_example:
    nrows, ncols = 7, 11
else:
    nrows, ncols = 103, 101

max_sf = float("-inf")
max_sf_second = None

for second in tqdm(range(nrows * ncols * 2)):
    result = []
    for pr, pc, vr, vc in bots:
        result.append(
            (
                (pr + second * vr) % nrows,
                (pc + second * vc) % ncols,
            )
        )

    vm = nrows // 2
    hm = ncols // 2

    sf = 1
    tl, tr, bl, br = 0, 0, 0, 0
    for pr, pc in result:
        if pr < vm and pc < hm:
            tl += 1
        elif pr < vm and pc > hm:
            tr += 1
        elif pr > vm and pc < hm:
            bl += 1
        elif pr > vm and pc > hm:
            br += 1
    sf = tl * tr * bl * br
    if sf > max_sf:
        max_sf = sf
        max_sf_second = second
    print(f"After {second} seconds, sf: {sf}, tl: {tl}, tr: {tr}, bl: {bl}, br: {br}")

print(f"Max sf: {max_sf}, at second: {max_sf_second}")

#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
