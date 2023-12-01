import re

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"
INPUT_FILE_SMALL_2 = f"{__file__.replace('.py', '_input_small_2.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def get_first_and_last_digit(word):
    first = -1
    first_index = -1
    end_index = -1
    end = -1
    for index in range(len(word)):
        if word[index].isdigit():
            if first == -1 and word:
                first = int(word[index])
                first_index = index
            end = int(word[index])
            end_index = index
    return first, end, first_index, end_index

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_with_text_digits(word):
    first, end , *indexes = get_first_and_last_digit(word)
    first_index, end_index = indexes
    for index, digit in enumerate(digits):
        found = [m.start() for m in re.finditer(digit, word)]
        if not found: continue
        if min(found) < first_index or first_index == -1:
            first_index = min(found)
            first = index + 1
        if max(found) > end_index:
            end_index = max(found)
            end = index + 1
    return first, end, first_index, end_index
    pass

def part1(values):
    results = []
    for value in values:
        first, end, *other = get_first_and_last_digit(value)
        results.append(first * 10 + end)
    print(f"First part: {sum(results)}")

def part2(values):
    results = []
    for value in values:
        first, end, *other = get_with_text_digits(value)
        results.append(first * 10 + end)
    print(f"Second part: {sum(results)}")

def part2_variant(values):
    # with the help of r/AdventOfCode
    results = []
    for value in values:
        first, end, *other = get_first_and_last_digit(
            value.replace('one', 'one1one')
                .replace('two', 'two2two')
                .replace('three', 'three3three')
                .replace('four', 'four4four')
                .replace('five', 'five5five')
                .replace('six', 'six6six')
                .replace('seven', 'seven7seven')
                .replace('eight', 'eight8eight')
                .replace('nine', 'nine9nine')
            )
        results.append(first * 10 + end)
    print(f"Second part variant: {sum(results)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 55538
    part2(values) # Second part: 54875
    part2_variant(values)

if __name__ == "__main__":
    main()