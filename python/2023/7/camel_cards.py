from collections import Counter
from functools import reduce, cmp_to_key
from operator import mul

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDS_JOKER = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def get_hand_value(hand):
    counter = Counter(hand)
    most_commons = counter.most_common(2)
    if len(most_commons) == 1: return (most_commons[0][1]) ** 2
    return (most_commons[0][1]) ** 2 + most_commons[1][1] ** 2

def get_max_hand_value(hand):
    max_ = 0
    for i in CARDS_JOKER[1:]:
        hand_value = get_hand_value(hand.replace('J', i))
        if max_ < hand_value:
            max_ = hand_value
    return max_

def get_hands_and_bids(lines):
    return [(i.split(' ')[0], int(i.split(' ')[1])) for i in lines]

def cmp_stronger_card(hand1, hand2, card_ref=CARDS):
    for card1, card2 in zip(hand1, hand2):
        card1_index, card2_index = (card_ref.index(card1), card_ref.index(card2))
        if card2_index == card1_index: continue
        return card1_index - card2_index
    else: return 0

def cmp_function(hand1, hand2):
    if hand1[2] != hand2[2]: return hand1[2] - hand2[2]
    return cmp_stronger_card(hand1[0], hand2[0])

def cmp_function_joker(hand1, hand2):
    if hand1[2] != hand2[2]: return hand1[2] - hand2[2]
    return cmp_stronger_card(hand1[0], hand2[0], CARDS_JOKER)

def part1(values):
    hands_bids_values = [(hand, bid, get_hand_value(hand)) for hand, bid in get_hands_and_bids(values)]
    sorted_values = sorted(hands_bids_values, key=cmp_to_key(cmp_function))
    reduce_lambda = lambda a,b: a + (b[0] + 1) * b[1][1]
    print(f"First part: {reduce(reduce_lambda, enumerate(sorted_values), 0)} ")


def part2(values):
    hands_bids_values = [(hand, bid, get_max_hand_value(hand)) for hand, bid in get_hands_and_bids(values)]
    sorted_values = sorted(hands_bids_values, key=cmp_to_key(cmp_function_joker))
    # [print(i) for i in sorted_values]
    reduce_lambda = lambda a,b: a + (b[0] + 1) * b[1][1]
    print(f"Second part: {reduce(reduce_lambda, enumerate(sorted_values), 0)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 250951660
    part2(values) # Second part:

if __name__ == "__main__":
    main()