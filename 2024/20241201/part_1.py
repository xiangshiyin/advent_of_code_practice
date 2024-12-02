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

# 2. Sort the 2 lists
left.sort()
right.sort()

# 3. Find the median of the 2 lists
distance = 0
for l, r in zip(left, right):
    distance += abs(l - r)

print(distance)
