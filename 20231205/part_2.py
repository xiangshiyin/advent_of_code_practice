import os
import re

os.chdir(os.path.dirname(__file__))

# read the input file
with open("20231205_input.txt", "r") as file:
    input = file.read()
blobs = re.split("\n[^\n]+:", input)

# clean seeds
seeds_blob = [int(v) for v in blobs[0].lstrip("seeds:").strip().split()]
seeds = [
    (seeds_blob[i], seeds_blob[i] + seeds_blob[i + 1])
    for i in range(0, len(seeds_blob), 2)
]
print(sorted(seeds, key=lambda x: x[0]))

# iterate over the blobs
for blob in blobs[1:]:
    maps = []
    # parse the maps
    for row in blob.strip().splitlines():
        maps.append([int(v) for v in row.strip().split()])

    targets = []
    while len(seeds) > 0:
        l, h = seeds.pop()  # get the seed range
        for t, s, interval in maps:
            # calculate the overlap
            overlap_start = max(l, s)
            overlap_end = min(h, s + interval)
            if overlap_start < overlap_end:
                # if there is overlap, add the new seed
                targets.append([overlap_start - s + t, overlap_end - s + t])
                # add the new seeds
                if overlap_start > l:
                    seeds.append([l, overlap_start])
                if h > overlap_end:
                    seeds.append([overlap_end, h])
                break
        else:
            # if there is no overlap, add the seed
            targets.append([l,h])
    seeds = targets

print(min(seeds)[0])
