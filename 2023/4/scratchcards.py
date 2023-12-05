INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def process_values(lines):
    values = []
    for line in lines:
        values.append([{int(j) for j in i.split()} for i in line.split(":")[1].split('|')])
    return values


def part1(raw_values):
    values = process_values(raw_values)
    final_sum = 0
    for winning_numbers, numbers in values:
        winning_count = len(winning_numbers & numbers)
        if winning_count > 0:
            final_sum += 2 ** (winning_count - 1)
    print(f"First part: {final_sum}")

def part2(raw_values):
    values = process_values(raw_values)
    card_counts = [1 for i in range(len(values))]
    for current_card, (winning_numbers, numbers) in enumerate(values):
        winning_count = len(winning_numbers & numbers)
        if winning_count == 0: continue
        for i in range(winning_count):
            card_counts[i + 1 + current_card] += card_counts[current_card]
    print(f"Second part: {sum(card_counts)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 27454
    part2(values) # Second part: 6857330

if __name__ == "__main__":
    main()