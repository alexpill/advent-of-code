INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


def process_values(lines):
    return [[*map(int, line.split())] for line in lines]


def is_safe(row): # Incredible thanks for reddit to point out this solution
    variation = [row[i+1] - row[i] for i in range(len(row) - 1)]
    return True if set(variation) <= {1,2,3} or set(variation) <= {-1, -2, -3} else False

def part1(raw_values):
    values = process_values(raw_values)
    result = sum([is_safe(row) for row in values])
    print(f"First part: {result}")


def part2(raw_values):
    values = process_values(raw_values)
    # checking if any of the permutations of the row is safe when removing one element
    result = sum([any([is_safe(row[:i] + row[i+1:]) for i in range(len(row))]) for row in values])
    print(f"Second part: {result}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 306
    part2(values)  # Second part: 366


if __name__ == "__main__":
    main()
