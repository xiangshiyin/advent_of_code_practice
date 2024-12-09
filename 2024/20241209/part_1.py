
import os
import sys

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = '--example' in sys.argv
path = "20241209_input_example.txt" if use_example else "20241209_input.txt"
diskmap = ''
with open(path, "r") as file:
    for line in file:
        diskmap += line.strip()

# print(diskmap)

# 2. translate the diskmap into a string of file ids and spaces
n = len(diskmap)
file_id_current = 0
file_id_map = {}
idx = 0
translated_diskmap = ''
for i in range(n):
    if idx % 2 == 0: # files
        mapped_char = chr(48 + file_id_current)
        translated_diskmap += mapped_char * int(diskmap[idx])
        file_id_map[mapped_char] = file_id_current
        file_id_current += 1
    else: # spaces
        translated_diskmap += '.' * int(diskmap[idx])
    idx += 1

# print(file_id_map)

# 3. Move file blocks one at a time from the end of the disk to the leftmost free space block until there are no gaps remaining between file blcoks
translated_diskmap_list = list(translated_diskmap)
# print(''.join(translated_diskmap_list)[:100])
# use two pointers, one for the leftmost free space block and one for the rightmost file block
leftmost_free_space_idx = 0
rightmost_file_idx = len(translated_diskmap_list) - 1
while leftmost_free_space_idx < rightmost_file_idx:
    if translated_diskmap_list[leftmost_free_space_idx] != '.':
        leftmost_free_space_idx += 1
    else:
        # find the rightmost file block
        if translated_diskmap_list[rightmost_file_idx] == '.':
            rightmost_file_idx -= 1
        else:
            # swap the file block with the free space block
            translated_diskmap_list[leftmost_free_space_idx], translated_diskmap_list[rightmost_file_idx] = translated_diskmap_list[rightmost_file_idx], translated_diskmap_list[leftmost_free_space_idx]
            rightmost_file_idx -= 1
            leftmost_free_space_idx += 1

print(''.join(translated_diskmap_list)[:100])

# 3. calculate the checksum of file ids
checksum = 0
for i in range(len(translated_diskmap_list)):
    if translated_diskmap_list[i] != '.':
        checksum += i * file_id_map[translated_diskmap_list[i]]

print(checksum)
