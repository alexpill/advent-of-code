INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

import functools as ft

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def get_intersection(sack):
    first_half = set(sack[:len(sack)//2])
    second_half = set(sack[len(sack)//2:])
    return first_half.intersection(second_half)

def get_priority(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return ord(character) - 96
    elif ord(character) >= 65 and ord(character) <= 90:
        return ord(character) - 38

def get_sum_of_priorities(sacks):
    total = 0
    for sack in sacks:
        intersection = get_intersection(sack).pop()
        priority = get_priority(intersection)
        total += priority
    return total

def gen_groups(sacks):
    curr_group = []
    for sack in sacks:
        curr_group.append(set(sack))
        if len(curr_group) == 3:
            yield curr_group
            curr_group = []

def get_sum_of_priorities2(sacks):
    total = 0
    for group in gen_groups(sacks):
        intersection = ft.reduce(lambda a, b: a & b, group)
        total += get_priority(intersection.pop())
    return total

def part1(values):
    print(f"First part: {get_sum_of_priorities(values)}")

def part2(values):
    print(f"Second part: {get_sum_of_priorities2(values)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 7581
    part2(values) # Second part: 2525

if __name__ == "__main__":
    main()