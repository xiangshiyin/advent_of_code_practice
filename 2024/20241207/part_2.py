import os

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = False
path = "20241207_input_example.txt" if use_example else "20241207_input.txt"
test_values = []
test_inputs = []
with open(path, "r") as file:
    for line in file:
        test_values.append(int(line.split(":")[0]))
        test_inputs.append(list(map(int, line.split(":")[1].split())))

# print(test_values)
# print(test_inputs)

# 2. Find the number of test values that could be computed by the test inputs with operators + and * when evaluated from left to right
# For every input number in a test input, we can either add it to the previous number or multiply it to the previous output
# We can traverse all the possible ways via recursion, whenever we reach the end of the test input, we check if the computed value matches the test value
# If it does, we stop and count the test input as valid
# when validating, we will start from the last number and try to go back to the first number

def compute_value(test_input, test_value):
    if len(test_input) == 0:
        return test_value == 0
    if len(test_input) == 1:
        return test_input[0] == test_value
    return (
        compute_value(test_input[:-1], test_value - test_input[-1])
        or compute_value(test_input[:-1], test_value / test_input[-1])
    )

# test_input = [10, 19]
# test_value = 190
# print(compute_value(test_input, test_value))

counter = 0
sum_of_valid_test_values = 0
for i in range(len(test_values)):
    if compute_value(test_inputs[i], test_values[i]):
        counter += 1
        sum_of_valid_test_values += test_values[i]
print(counter)
print(sum_of_valid_test_values)
