INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(filename=INPUT_FILE):
    with open(filename) as f:
        return [int(i) for i in f.readline().strip().split(',')]

def first_solution(values):
    for day in range(80):
        for fish_id in range(len(values)):
            values[fish_id] -= 1
            if values[fish_id] < 0:
                values[fish_id] = 6
                values.append(8)
    return len(values)

def second_solution(values, days=80):
    fishes_cnt = [0] * 9
    for val in values:
        fishes_cnt[val] += 1
    for day in range(days):
        fishes_to_reset = fishes_cnt[0]
        for fish_idx in range(0, 8):
            fishes_cnt[fish_idx] = fishes_cnt[fish_idx + 1]
        fishes_cnt[8] = fishes_to_reset
        fishes_cnt[6] += fishes_to_reset
    return sum(fishes_cnt)

def part1(values):
    print(f"First part: {second_solution(values.copy())}")

def part2(values):
    print(f"Second part: {second_solution(values.copy(), days=256)}")

def main():
    values = get_input(INPUT_FILE)
    part1(values) # First part: 389726
    part2(values) # Second part: 1743335992042

if __name__ == '__main__':
    main()