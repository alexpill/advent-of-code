INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return [(1 if line[0] == 'R' else -1 , int(line[1:])) for line in f.read().splitlines()]

def part1(values):
    zero_count = 0
    dial = 50
    for sign, value in values:
        dial = (dial + sign * value) % 100
        zero_count += dial == 0
    print(f"First part: {zero_count}")

def part2(values):
    zero_count = 0
    dial = 50
    for sign, value in values:
        zero_count += ((100 + sign * dial) % 100 + value) // 100
        dial = (dial + sign * value) % 100
    print(f"Second part: {zero_count}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 1066
    part2(values)  # Second part: 6223

if __name__ == "__main__":
    main()
