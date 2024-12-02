import os
import re
from tqdm import tqdm
from collections import defaultdict, deque

os.chdir(os.path.dirname(__file__))

# with open("20231215_input_example.txt") as f:
with open("20231215_input.txt") as f:
    inputs = [string.strip() for string in f.readlines()[0].strip().split(',')]
# print(inputs)
print(f"Length of inputs: {len(inputs)}")

# step 1: util functions
"""
To run the HASH algorithm on a string, start with a current value of 0. Then, for each character in the string starting from the beginning: 
Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.
"""
def translate(sting):
    current_value = 0
    for character in sting:
        current_value += ord(character)
        current_value *= 17
        current_value %= 256
    return current_value

""" 
The focusing power of a single lens is the result of multiplying together:

One plus the box number of the lens in question.
The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
The focal length of the lens.
"""
def focusing_power(box, box_number):
    ans = 0
    for label in box:
        slot_number, focal_length = box[label]
        slot_number = slot_number - removals_sofar(boxe_removals, box_id, slot_number)
        ans += (box_number + 1) * (slot_number + 1) * focal_length
    return ans

def removals_sofar(box_removals, box_id, slot_number):
    removals = 0
    for removal in box_removals[box_id]:
        if removal < slot_number:
            removals += 1
    return removals

# step 2: traverse the list of inputs
boxes = [defaultdict(list) for i in range(256)]
boxe_removals = defaultdict(list)

for input in tqdm(inputs, ncols=70):
    label, suffix = re.split('[=,-]', input)
    box_id = translate(label)
    box = boxes[box_id]
    if box:
        l = max([box[key][0] for key in box])
    else:
        l = -1
    if "=" in input:
        focal_length = int(suffix)
        if (label not in box):
            box[label] = [l+1, focal_length]
        elif label in box and box[label][1] != 0:
            box[label][1] = focal_length
        else:
            box[label] = [l+1, focal_length]
    elif "-" in input:
        if label in box and box[label][1] != 0:
            box[label][1] = 0
            boxe_removals[box_id].append(box[label][0])
    # if box_id == 6:
    #     print("\n")
    #     print(f"Input: {input}")
    #     print(f"Box 6: {box}")
    #     print(f"Box 6 removals: {boxe_removals[6]}")
    #     print(f"Box {box_id} has a focusing power of {focusing_power(box, box_id)}")

        
# step 3: calculate the focusing power
ans = 0
for box_id, box in enumerate(boxes):
    if len(box) == 0:
        continue
    print(f"Box {box_id} has a focusing power of {focusing_power(box, box_id)}")
    ans += focusing_power(box, box_id)

print(f"Answer: {ans}")

