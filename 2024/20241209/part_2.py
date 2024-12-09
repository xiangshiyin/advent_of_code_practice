
import os
import sys
import time

start_time = time.time()
# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = '--example' in sys.argv
enable_debug = '--debug' in sys.argv
path = "20241209_input_example.txt" if use_example else "20241209_input.txt"
diskmap = ''
with open(path, "r") as file:
    for line in file:
        diskmap += line.strip()

n = len(diskmap)
if enable_debug:
    print(diskmap)

# 2. utility functions
def translate_diskmap(diskmap):
    diskmap_translated = []
    for i in range(n):
      if i % 2 == 0: # files
          diskmap_translated.extend(
              [str(i // 2)] * int(diskmap[i])
          )
      else: # spaces
          diskmap_translated.extend(
              ['.'] * int(diskmap[i])
          )
    return diskmap_translated

diskmap_translated = translate_diskmap(diskmap)
print(f"Before traversal: {'|'.join(diskmap_translated[:300])}")

# 3. Traverse the translated diskmap
m = len(diskmap_translated)
r = m - 1

while r > int(diskmap[0]):
    l = 0
    while l < r:
    # while r > 0:
        if diskmap_translated[l] != '.':
            l += 1
        elif diskmap_translated[r] == '.':
            r -= 1
        elif l == r or l == m - int(diskmap[-1]):
            break
        else:
            len_current_file_block = int(
                diskmap[
                    int(diskmap_translated[r]) * 2
                ]
            )
            if enable_debug:
                print(f"Current file block length: {len_current_file_block}, file ID: {diskmap_translated[r]}")
            if ''.join(diskmap_translated[l:l + len_current_file_block]) == '.' * len_current_file_block:
                # swap the free space block and the current file block
                if enable_debug:
                    print(f"Before swap: {diskmap_translated}")
                diskmap_translated[l:l+len_current_file_block] = diskmap_translated[r+1-len_current_file_block:r+1]
                diskmap_translated[r+1-len_current_file_block:r+1] = '.' * len_current_file_block
                if enable_debug:
                    print(f"After swap: {diskmap_translated}")
                break
            else: # not enough space to swap
                while l < r and diskmap_translated[l] == '.':
                    l += 1
    r -= len_current_file_block
    


print(f"After traversal: {'|'.join(diskmap_translated[:300])}")

# 4. Calculate the checksum
checksum = 0
for i in range(m):
    if diskmap_translated[i] != '.':
        checksum += i * int(diskmap_translated[i])
print(f"Checksum: {checksum}")

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

# import random

# random_string = ''.join(random.choices('0123456789', k=100))
# print(f"Generated random string: {random_string}")

# part 2: 
# Checksum: 6413328569890
# Time taken: 27.19003701210022 seconds