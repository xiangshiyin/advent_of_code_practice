import os

os.chdir(os.path.dirname(__file__))

# step 1: collect input
with open("20231216_input_example.txt") as f:
# with open("20231216_input.txt") as f:
    input = f.read().splitlines()

print(input)
