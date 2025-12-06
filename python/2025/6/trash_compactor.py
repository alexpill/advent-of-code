INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def part1(values):
    values = [f.split() for f in values[:]]
    grand_total = 0
    for i in range(len(values[0])):
        grand_total += eval(values[-1][i].join([values[j][i] for j in range(len(values) - 1)]))
    print(f"First part: {grand_total}")

def part2(values):
    values = [[s for s in f] for f in values[:]]
    buffer = []
    grand_total = 0
    for i in reversed(range(len(values[0]))):
        value = "".join([values[j][i] for j in range(len(values))])
        if not value.strip():
            operation = buffer[-1][-1]
            buffer[-1] = buffer[-1][:-1]
            grand_total+= eval(operation.join(buffer))
            buffer = []
        else:
            buffer.append(value)
    else:
        operation = buffer[-1][-1]
        buffer[-1] = buffer[-1][:-1]
        grand_total+= eval(operation.join(buffer))

    print(f"Second part: {grand_total}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 6417439773370
    part2(values)  # Second part: 11044319475191

if __name__ == "__main__":
    main()
