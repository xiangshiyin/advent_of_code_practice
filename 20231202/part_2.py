"""
Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes
"""

import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lookup = {
    "red": 12,
    "green": 13,
    "blue": 14
}

games = defaultdict(list)
qualified_games = []
sum_of_qualified_ids = 0
# with open("20231202_input_example.txt", "r") as f:
with open("20231202_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        id = int(line.split(":")[0].split()[1])
        for draw in line.split(":")[1].split(";"):
            cubes = {cube.strip().split()[1]: int(cube.strip().split()[0]) for cube in draw.split(",")}
            games[id].append(cubes)

# for game, draws in games.items():
#     for draw in draws:
#         if any([draw[cube] > lookup[cube] for cube in draw]):
#             break
#     else:
#         qualified_games.append(game)
#         sum_of_qualified_ids += game

# print(qualified_games)
# print(f"Sum of qualified game IDs: {sum_of_qualified_ids}")

# print(games)
minimum_requirements = []
for game, draws in games.items():
    for idx, draw in enumerate(draws):
        if idx == 0:
            minimum_requirement = draw
        else:
            for cube, count in draw.items():
                if cube in minimum_requirement:
                    minimum_requirement[cube] = max(minimum_requirement[cube], count)
                else:
                    minimum_requirement[cube] = count
    minimum_requirements.append(minimum_requirement)

print(minimum_requirements)

# find the power
powers = 0 
for requirement in minimum_requirements:
    power = 1
    for cube, count in requirement.items():
        power *= count
    powers += power

print(f"Sum of powers: {powers}")