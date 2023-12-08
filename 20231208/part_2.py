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

# print(nodes["AAA"])

# find all nodes ending with "A"
starts = []
for line in lines[2:]:
    # print(line)
    matches = re.findall(r"[0-9A-Z]{2}A", line)
    if matches:
        starts.extend(matches)
# print(starts)

# travel through the nodes
instructions = deque(instructions)
# print(instructions)

def all_end_with_Z(nodes):
    return all([node.endswith("Z") for node in nodes])

step = 0
current_nodes = deque(starts)
# l = len(current_nodes)
# while not all_end_with_Z(current_nodes):
#     instruction = instructions.popleft()
#     instructions.append(instruction)

#     for i in range(l):
#         current_node = current_nodes.popleft()
#         if instruction == "L":
#             current_nodes.append(nodes[current_node][0])
#         else:
#             current_nodes.append(nodes[current_node][1])

#     step += 1

# print(f"Step {step}: {current_nodes}, status: {all_end_with_Z(current_nodes)}, next: {instruction}")
# print(f"Answer: {step}")

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
    """
    Output:
    It takes 19199 steps for node HJZ to reach HJZ
    It takes 11309 steps for node SBZ to reach SBZ
    It takes 17621 steps for node RFZ to reach RFZ
    It takes 20777 steps for node VPZ to reach VPZ
    It takes 16043 steps for node ZZZ to reach ZZZ
    It takes 15517 steps for node PQZ to reach PQZ
    """

print(f"Answer: {math.lcm(*steps)} steps")

