INPUT_FILE = "dive_input.txt"

def extract_commands_from_file(file_name):
    values = []
    with open(file_name) as f:
        for line in f:
            command, amount = line.strip().split()
            values.append((command, int(amount)))
    return values

def walk(commands):
    depth = 0
    horizontal_pos = 0
    for command, amount in commands:
        if command == "down":
            depth += amount
        elif command == "up":
            depth -= amount
        else:
            horizontal_pos += amount
    return horizontal_pos, depth

def walk_with_aim(commands):
    depth = 0
    horizontal_pos = 0
    aim = 0
    for command, amount in commands:
        if command == "down":
            aim += amount
        elif command == "up":
            aim -= amount
        else:
            horizontal_pos += amount
            depth += aim * amount
    return horizontal_pos, depth



def part1(values):
    horizontal_pos, depth = walk(values)
    print(f"First part: {horizontal_pos * depth}")

def part2(values):
    horizontal_pos, depth = walk_with_aim(values)
    print(f"Second part: {horizontal_pos * depth}")

def main():
    commands = extract_commands_from_file(INPUT_FILE)
    part1(commands)  # First part: 1580000
    part2(commands)  # First part: 1251263225

if __name__ == "__main__":
    main()