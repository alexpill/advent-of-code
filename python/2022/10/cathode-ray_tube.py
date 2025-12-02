INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return [i.split() for i in f.read().splitlines()]

def sum_of_signal_strengths(values):
    cycle = 0
    x_register = 1
    signals = []
    for val, *args in values:
        if val == 'noop':
            cycle += 1
            if (cycle + 20) % 40 == 0: signals.append(cycle * x_register)
        elif val == 'addx':
            for _ in range(2):
                cycle += 1
                if (cycle + 20) % 40 == 0: signals.append(cycle * x_register)
            x_register += int(args[0])
    return sum(signals)

def process_cycle(x_register, row: str):
    if len(row) < x_register - 1 or len(row) > x_register + 1:
        return row + '.'
    return row + '#'

def signal_printing(values):
    cycle = 0
    x_register = 1
    row = ''
    for val, *args in values:
        for _ in range(2 if val == 'addx' else 1):
            cycle += 1
            row = process_cycle(x_register, row)
            if cycle % 40 == 0:
                print(row)
                row = ''
        if val == 'addx': x_register += int(args[0])

def part1(values):
    print(f"First part: {sum_of_signal_strengths(values)}")

def part2(values):
    print(f"Second part:")
    signal_printing(values)

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 15260
    part2(values) # Second part: PGHFGLUG

if __name__ == "__main__":
    main()