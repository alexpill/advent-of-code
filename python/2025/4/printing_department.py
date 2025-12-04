INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return [[0 if c == "." else 1 for c in s] for s in f.read().splitlines()]


def neighbours_count(row, col, values):
    count = 0
    for i in range(-1, 2):
        if row + i < 0 or row + i > len(values) - 1:
            continue
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if col + j < 0 or col + j > len(values[0]) - 1:
                continue
            count += values[row + i][col + j]
    return count


def part1(values):
    accessible = 0
    for row in range(len(values)):
        for col in range(len(values[0])):
            if values[row][col] and neighbours_count(row, col, values) < 4:
                accessible += 1
    print(f"First part: {accessible}")


def part2(values):
    grid = [row[:] for row in values]

    potential = set()
    accessible_cnt = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                potential.add((row, col))

    accessible = set()
    first_iteration = True

    while first_iteration or len(accessible) > 0:
        first_iteration = False

        accessible = set()
        for row, col in potential:
            if neighbours_count(row, col, grid) < 4:
                accessible.add((row, col))

        potential -= accessible
        accessible_cnt += len(accessible)

        for row, col in accessible:
            grid[row][col] = 0

    print(f"Second part: {accessible_cnt}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 1349
    part2(values)  # Second part: 8277


if __name__ == "__main__":
    main()
