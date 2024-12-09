import os
import argparse
import datetime


parser = argparse.ArgumentParser()
parser.add_argument('--date', type=str, default=datetime.datetime.now().strftime('%Y%m%d'))
args = parser.parse_args()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(f"../{args.date[:4]}"):
    os.mkdir(f"../{args.date[:4]}")
os.mkdir(f"../{args.date[:4]}/{args.date}")
os.chdir(f"../{args.date[:4]}/{args.date}")

script_template = f"""
import os
import sys

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
use_example = '--example' in sys.argv
path = "{args.date}_input_example.txt" if use_example else "{args.date}_input.txt"
grid = []
with open(path, "r") as file:
    for line in file:
        grid.append(list(line.strip()))
"""

with open(f"{args.date}_input.txt", "w") as f:
    pass

with open(f"{args.date}_input_example.txt", "w") as f:
    pass

with open(f"part_1.py", "w") as f:
    f.write(script_template)

with open(f"part_2.py", "w") as f:
    f.write(script_template)

with open(f"README.md", "w") as f:
    f.write(f"Source: https://adventofcode.com/2024/day/{int(args.date[-2:])}")

