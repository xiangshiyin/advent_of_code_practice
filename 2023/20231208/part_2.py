import os
import re
from collections import deque
import math

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# with open("20231208_input_example.txt", "r") as f:
with open("20231208_input.txt", "r") as f:
    lines = f.readlines()

instructions = lines[0].strip()
nodes = {
    line.strip().split("=")[0].strip(): line.strip().split("=")[1].strip().lstrip("(").rstrip(")").replace(" ","").split(",")
    for line in lines[2:]
}

# find all nodes ending with "A"
starts = []
for line in lines[2:]:
    # print(line)
    matches = re.findall(r"[0-9A-Z]{2}A", line)
    if matches:
        starts.extend(matches)

# travel through the nodes
instructions = deque(instructions)

current_nodes = deque(starts)

steps = []
for current_node in current_nodes:
    step = 0
    while not current_node.endswith("Z"):
        instruction = instructions.popleft()
        instructions.append(instruction)
        if instruction == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        step += 1
    steps.append(step)
    print(f"It takes {step} steps for node {current_node} to reach {current_node}")

print(f"Answer: {math.lcm(*steps)} steps")

