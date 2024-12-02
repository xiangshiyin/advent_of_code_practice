import os
from collections import Counter

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# card sequence
sequence = 'AKQJT98765432'[::-1]
order = {sequence[i]: i+1 for i in range(len(sequence))}
print(f"Order: {order}")

def get_card_order_score(card):
    scores = []
    for digit in card:
        scores.append(str(order[digit]).rjust(2, '0'))
    return ''.join(scores)

hands = []

# clean the hands and append types
with open('20231207_input.txt','r') as file:
# with open('20231207_input_example.txt','r') as file:
    for line in file:
        card, bid = line.strip().split()
        hands.append([card, int(bid)]) 
        freq = Counter(card)
        hands[-1].append(
            ''.join(str(digit) for digit in sorted(freq.values(), reverse=True)).ljust(5, '0')
        )
        hands[-1].append(
            get_card_order_score(card)
        )

print(f"Number of hands: {len(hands)}")

# rank hands
hands.sort(key=lambda x: (
    x[2], # type
    x[3] # card
))
 
for idx, hand in enumerate(hands):
    if idx < 10 or idx > len(hands) - 10:    
        print(f"{idx+1}: {hand}")

total_prize = 0
for idx, hand in enumerate(hands):
    total_prize += hand[1] * (idx + 1)

print(f"Total prize: {total_prize}")