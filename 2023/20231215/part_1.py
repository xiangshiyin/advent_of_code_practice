import os

os.chdir(os.path.dirname(__file__))

with open("20231215_input_example.txt") as f:
# with open("20231215_input.txt") as f:
    inputs = [string.strip() for string in f.readlines()[0].strip().split(',')]
# print(inputs)
print(f"Length of inputs: {len(inputs)}")

# To run the HASH algorithm on a string, start with a current value of 0. Then, for each character in the string starting from the beginning:

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.
def translate(sting):
    current_value = 0
    for character in sting:
        current_value += ord(character)
        current_value *= 17
        current_value %= 256
    return current_value

ans = 0
for input in inputs:
    translated = translate(input)
    ans += translated
    print(f"{input} becomes {translated}")

print(f"Answer: {ans}")
