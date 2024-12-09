
import os
import sys
import time

start_time = time.time()
# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241209_input_example.txt" if use_example else "20241209_input.txt"
diskmap = ''
with open(path, "r") as file:
    for line in file:
        diskmap += line.strip()

n = len(diskmap)
# print(diskmap)

# 2. utility functions
def get_file_id_rep(i):
    return chr(48 + int(diskmap[i]))

def print_translated_diskmap(diskmap):
    n = len(diskmap)
    file_id_map = {}
    translated_diskmap = ''
    for i in range(n):
        if i % 2 == 0: # files
            mapped_char = chr(48 + i // 2)
            translated_diskmap += mapped_char * int(diskmap[i])
            file_id_map[mapped_char] = i // 2
        else: # spaces
            translated_diskmap += '.' * int(diskmap[i])

    return translated_diskmap, file_id_map

translated_diskmap, file_id_map = print_translated_diskmap(diskmap)
m = len(translated_diskmap)
print(f"Length of translated diskmap: {m}")

# 3. Use 4 pointers to locate the leftmost free space block and the rightmost file block
rl, rr = m - 1, m - 1
round = 0
while rl > int(diskmap[0]):
    print(f"Round {round}")
    # print(f"Round {round}, diskmap: {translated_diskmap}, rl: {rl}, rr: {rr}")
    ## First, find the rightmost file block
    while rl > 0 and translated_diskmap[rl] == '.':
        rl -= 1
        rr -= 1
    while rl > 0 and translated_diskmap[rl] != '.' and translated_diskmap[rl] == translated_diskmap[rr]:
        rl -= 1
    if rl == int(diskmap[0]):
        break

    ll, lr = 0, 0
    subround = 0

    while True:
        translated_diskmap_before = translated_diskmap
        # print(f"Subround {subround}: {(ll, lr), (rl, rr)}")
        if lr >= rl:
            break
        while lr < m and translated_diskmap[lr] != '.':
            ll += 1
            lr += 1
        while lr < m and translated_diskmap[lr] == '.':
            lr += 1


        # print(f"Free space block: {(ll, lr)}, File block: {(rl, rr)}")
        if rr - rl <= lr - ll and lr < rl:
            translated_diskmap = translated_diskmap[:ll] + translated_diskmap[rl+1: rr+1] + translated_diskmap[ll + (rr - rl):(rl+1)] + '.' * (rr - rl) + translated_diskmap[rr+1:]
            # print("Before:",translated_diskmap_before)
            # print("After:",translated_diskmap)        
            # print(translated_diskmap_before == translated_diskmap, len(translated_diskmap_before) == len(translated_diskmap))
            break

        ll = lr
        subround += 1
    rr = rl
    round += 1

# 3. calculate the checksum of file ids
checksum = 0
for i in range(m):
    if translated_diskmap[i] != '.':
        checksum += i * file_id_map[translated_diskmap[i]]

print(translated_diskmap[:300])
print(checksum)
print(translated_diskmap[-300:])
print(f"Length of translated diskmap: {m}")

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

# part 1: 6378826667552
# part 2: 6413328589346
