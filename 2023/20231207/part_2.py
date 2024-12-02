import os
from collections import Counter

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# card sequence
# sequence = 'AKQJT98765432'[::-1]
sequence = 'AKQT98765432J'[::-1]
order = {sequence[i]: i+1 for i in range(len(sequence))}
print(f"Order: {order}")

def get_type_score(freq):
    return ''.join(str(digit) for digit in sorted(freq.values(), reverse=True)).ljust(5, '0')

def get_most_freq_cards(freq):   
    "find the top2"
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [sorted_freq[0][0], sorted_freq[1][0]] if len(sorted_freq) > 1 else [sorted_freq[0][0], '']

def get_card_order_score(card):
    scores = []
    for digit in card:
        scores.append(str(order[digit]).rjust(2, '0'))
    return ''.join(scores)

def max_type_score(freq):
    """
    freq is a dictionary of card frequency
    Use J to represent whatever card that could maximize the type score
    """
    most_freq_cards = get_most_freq_cards(freq)
    if freq['J'] > 0:
        if 'J' not in most_freq_cards:
            freq[most_freq_cards[0]] += freq['J']
            freq.pop('J')
        elif most_freq_cards[1] != '':
            if most_freq_cards[0] == 'J':
                freq[most_freq_cards[1]] += freq['J']
            else:
                freq[most_freq_cards[0]] += freq['J']
            freq.pop('J')
    
    return get_type_score(freq)




    

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
        ) # type score
        hands[-1].append(
            get_card_order_score(card)
        ) # card score
        hands[-1].append(
            freq['J'] 
        ) # number of J
        hands[-1].append(
            max_type_score(freq.copy())
        )

print(f"Number of hands: {len(hands)}")

# rank hands
hands.sort(key=lambda x: (
    x[5], # new type
    x[3] # card
))
 
for idx, hand in enumerate(hands):
    if idx < 10 or idx > len(hands) - 100:    
        print(f"{idx+1}: {hand}")

total_prize = 0
for idx, hand in enumerate(hands):
    total_prize += hand[1] * (idx + 1)

print(f"Total prize: {total_prize}")