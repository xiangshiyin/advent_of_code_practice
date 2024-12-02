import os

os.chdir(os.path.dirname(__file__))

# read the input file
with open('./20231204_input.txt', 'r') as f:
    lines = f.readlines()

# parse the input file
cards = [1 for i in range(len(lines))]
for idx,line in enumerate(lines):
    matches = 0
    line_cleaned = line.strip().split(':')[1].split('|')
    winning_numbers = line_cleaned[0].strip().split()
    candidate_numbers = line_cleaned[1].strip().split()
    for number in winning_numbers:
        if number in candidate_numbers:
            matches += 1

    if matches > 0:
        print(f"Card {idx} has {matches} matches.")
        # update the cards counter
        for i in range(matches):
            cards[idx + i + 1] += cards[idx]

print(f"Total number of cards: {sum(cards)}")
