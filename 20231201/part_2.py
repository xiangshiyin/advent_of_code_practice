import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

str_to_number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

# pattern = '|'.join(list(str_to_number.values()))
pattern = '|'.join(list(str_to_number.keys()) + list(str_to_number.values()))
print(pattern)

sum_of_numbers = 0
# with open("20231201_input_example_2.txt", "r") as f:
# with open("20231201_input_example.txt", "r") as f:
with open("20231201_input.txt", "r") as f:
    for idx, line in enumerate(f):
        first = ''
        last = ''
        temp = ''
        for idx, char in enumerate(line):
            if char.isdigit():
                temp = char
            elif char.isalpha():
                if line[idx: idx+3] in str_to_number.keys():
                    temp = str_to_number[line[idx: idx+3]]
                elif line[idx: idx+4] in str_to_number.keys():
                    temp = str_to_number[line[idx: idx+4]]
                elif line[idx: idx+5] in str_to_number.keys():
                    temp = str_to_number[line[idx: idx+5]]
            if first == '':
                first = temp
        last = temp
        sum_of_numbers += int(first + last)
            
        # numbers_found = re.findall(pattern, line)
        # first = numbers_found[0] if numbers_found[0].isdigit() else str_to_number[numbers_found[0]]
        # last = numbers_found[-1] if numbers_found[-1].isdigit() else str_to_number[numbers_found[-1]]
        # sum_of_numbers += int(first + last)
print(f"Answer: {sum_of_numbers}")