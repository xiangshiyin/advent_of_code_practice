import os
from collections import deque

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("20231208_input.txt", "r") as f:
    lines = f.readlines()

instructions = lines[0].strip()
nodes = {
    line.strip().split("=")[0].strip(): line.strip().split("=")[1].strip().lstrip("(").rstrip(")").replace(" ","").split(",")
    for line in lines[2:]
}

print(nodes["AAA"])

# travel through the nodes
instructions = deque(instructions)
print(instructions)

step = 0
current_node = "AAA"
while current_node != "ZZZ":
    instruction = instructions.popleft()
    instructions.append(instruction)
    current_node = nodes[current_node][0] if instruction == "L" else nodes[current_node][1]
    step += 1

print(f"Answer: {step}")