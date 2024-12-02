from typing import Counter


INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def process_values(lines):
    col1 = []
    col2 = []
    for line in lines:
        col1.append(int(line.split()[0]))
        col2.append(int(line.split()[1]))
    return col1, col2

def part1(raw_values):
    col1, col2 = process_values(raw_values)
    col1.sort(), col2.sort()
    result = sum([abs(a - b) for a, b in zip(col1, col2)])
    print(f"First part: {result}")

def part2(raw_values):
    col1, col2 = process_values(raw_values)
    counter = Counter(col2)
    result = sum([counter[value] * value for value in col1])
    print(f"Second part: {result}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 2285373
    part2(values) # Second part: 21142653

if __name__ == "__main__":
    main()

# Other possible solutions that I found interesting:
# data = [*map(int, open('in.txt').read().split())]
# A, B = sorted(data[0::2]), sorted(data[1::2])
# print(sum(map(lambda a, b: abs(a-b), A, B)),
#       sum(map(lambda a: a * B.count(a), A)))