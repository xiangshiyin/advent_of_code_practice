import os
import sys
import time
import re
from collections import deque
# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


#####################################################
def combo(operand, ra, rb, rc):
    if operand <= 3:
        return operand
    elif operand == 4:
        return ra
    elif operand == 5:
        return rb
    elif operand == 6:
        return rc
    elif operand == 7:
        raise ValueError("Invalid operand")
#####################################################
start_time = time.time()
#####################################################
# 1. Read the input file
use_example = '--example' in sys.argv
test_case = '--test' in sys.argv
test_case_fixed = '--fixed' in sys.argv

path = "20241217_input_example.txt" if use_example else "20241217_input.txt"
grid = []
with open(path, "r") as file:
    blob = file.read()
    register_blob, program_blob = blob.split("\n\n")
    program = list(map(int, re.findall(r'\d+', program_blob)))
    ra, rb, rc = map(int, re.findall(r'\d+', register_blob))

if test_case:
    program = [0,3,5,4,3,0]
    ra, rb, rc = 2024, 0, 0
if test_case_fixed:
    program = [0,3,5,4,3,0]
    ra, rb, rc = 117440, 0, 0

instructions =['adv', 'bxl', 'bst', 'jnz', 'bxc', 'out', 'bdv', 'cdv']

# 2. Execute the program, find the lowest number of ra so that the output repeats the program itself
def execute_program(ra, rb, rc, program):
    l = len(program)
    pointer = 0
    outputs = []
    while True:
        if pointer >= l: break
        opcode = instructions[program[pointer]]
        operand = program[pointer+1]
        # print(f"pointer: {pointer}, opcode: {opcode}, operand: {operand}, ra: {ra}, rb: {rb}, rc: {rc}")

        output = None
        if opcode == 'adv': ra = ra >> combo(operand, ra, rb, rc)
        if opcode == 'bxl': rb = rb ^ operand
        if opcode == 'bst': rb =combo(operand, ra, rb, rc) % 8
        if opcode == 'jnz' and ra != 0: pointer = operand; continue
        if opcode == 'bxc': rb = rb ^ rc
        if opcode == 'out': output = combo(operand, ra, rb, rc) % 8
        if opcode == 'bdv': rb = ra >> combo(operand, ra, rb, rc)
        if opcode == 'cdv': rc = ra >> combo(operand, ra, rb, rc)
        if output is not None: outputs.append(output)
        pointer += 2
    return ','.join(map(str, outputs))

# reverse engineering the program
program0 = program[:]
def find_ra(program, ans):
    if program == []: return ans
    for t in range(8):
        a = (ans << 3) + t
        b = a % 8
        b = b ^ 3
        c = a >> b
        b = b ^ c
        b = b ^ 3
        if b % 8 == program[-1]:
            if a == 0: continue # since 0 << 3 is still 0, we need to skip this answer
            print(f"program[-1]: {program[-1]}, b%8: {b % 8}, a: {a}, validation: {execute_program(a, 0, 0, program0)}")
            sub = find_ra(program[:-1], a)
            if sub is None: continue
            return sub

print(find_ra(program, 0))


#####################################################
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
