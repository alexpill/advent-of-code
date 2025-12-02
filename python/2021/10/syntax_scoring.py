INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

char_couples = {'(': ')', '{': '}', '[': ']', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

def get_input(filename):
    with open(filename) as f:
        return f.read().splitlines()

def process(values):
    invalid_chars = []
    termination_sequence = []
    for val in values:
        expected_char = []
        invalid = False
        for idx, char in enumerate(val):
            if char in char_couples:
                expected_char.insert(0, char_couples[char])
            elif char == expected_char[0]:
                expected_char.pop(0)
            else:
                invalid_chars.append(char)
                invalid = True
                break
        if not invalid:
            termination_sequence.append("".join(expected_char))
    return invalid_chars, termination_sequence

def part1(values):
    invalid_chars, _ = process(values)
    print(f"First part: {sum(scores[char] for char in invalid_chars)}")
    pass

def get_part2_score(sequence):
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    total_score = 0
    for char in sequence:
        total_score = total_score * 5 + scores[char]
    return total_score

def part2(values):
    _, termination_sequence = process(values)
    scores = [get_part2_score(seq) for seq in termination_sequence]
    print(f"Second part: {sorted(scores)[len(scores) // 2]}")
    pass

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 315693
    part2(values) # Second part: 1870887234

if __name__ == "__main__":
    main()

