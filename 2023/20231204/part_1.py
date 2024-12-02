import os

os.chdir(os.path.dirname(__file__))

# read the input file
with open('./20231204_input.txt', 'r') as f:
    lines = f.readlines()
print(lines[:1])

# parse the input file
points = 0
for idx,line in enumerate(lines):
    card_points = 0
    matches = 0
    line_cleaned = line.strip().split(':')[1].split('|')
    winning_numbers = line_cleaned[0].strip().split()
    candidate_numbers = line_cleaned[1].strip().split()
    for number in winning_numbers:
        if number in candidate_numbers:
            matches += 1
            if card_points == 0:
                card_points = 1
            else:
                card_points *= 2
    if card_points > 0:
        print(f"Card {idx} has {card_points} points from {matches} matches.")
    points += card_points

print(points)