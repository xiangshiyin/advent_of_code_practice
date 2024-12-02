import os

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
left = []
right = []
# with open("20241201_input_example.txt", "r") as file:
with open("20241201_input.txt", "r") as file:
    for line in file:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

# 2. Build a frequency map in the right list
frequency_map = {}
for r in right:
    frequency_map[r] = frequency_map.get(r, 0) + 1

# 3. Get the output
output = 0
for l in left:
    output += l * frequency_map.get(l, 0)

print(output)
