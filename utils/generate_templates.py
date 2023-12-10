import os
import argparse
import datetime


parser = argparse.ArgumentParser()
parser.add_argument('--date', type=str, default=datetime.datetime.now().strftime('%Y%m%d'))
args = parser.parse_args()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.mkdir(f"../{args.date}")
os.chdir(f"../{args.date}")

with open(f"{args.date}_input.txt", "w") as f:
    pass

with open(f"{args.date}_input_example.txt", "w") as f:
    pass

with open(f"part_1.py", "w") as f:
    pass

with open(f"part_2.py", "w") as f:
    pass

with open(f"README.md", "w") as f:
    pass

