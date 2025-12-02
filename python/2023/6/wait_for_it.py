INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def part1(raw_values):
    values = organize_values(raw_values)
    full_way_to_win = 1
    for time, win_distance in values:
        winning_count = 0
        for hold_time in range(1, time):
            distance = hold_time * (time - hold_time)
            if distance > win_distance:
                winning_count += 1
        full_way_to_win *= winning_count
    print(f"First part: {full_way_to_win}")

def part2(raw_values):
    time, win_distance = [int(i.split(':')[1].replace(' ', '')) for i in raw_values]
    winning_count = 0
    for hold_time in range(1, time):
        distance = hold_time * (time - hold_time)
        if distance > win_distance:
            winning_count += 1
    print(f"Second part: {winning_count}")

def part2_optimized(raw_values):
    time, win_distance = [int(i.split(':')[1].replace(' ', '')) for i in raw_values]
    winning_count = 0
    for hold_time in range(1, time):
        distance = hold_time * (time - hold_time)
        if distance > win_distance:
            # winning_count = time - (hold_time - 1) - hold_time
            winning_count = time -  2 * hold_time + 1
            break
    print(f"Second part optimized: {winning_count}")

def organize_values(values):
    times = [int(i) for i in values[0].split(':')[1].split()]
    distances = [int(i) for i in values[1].split(':')[1].split()]
    values = []
    for time, distance in zip(times, distances):
        values.append((time, distance))
    return values

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 500346
    part2(values) # Second part: 42515755
    part2_optimized(values) # Second part: 42515755

if __name__ == "__main__":
    main()