from math import prod

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return [[int(j) for j in i] for i in f.read().splitlines() ]

def is_lowest_point(values, ridx, cidx):
    neighbours = get_neighbours(values, ridx, cidx)
    return all([values[ridx][cidx] < i[0] for i in neighbours])

lowest_points = []
def part1(values):
    for ridx, row in enumerate(values):
        for cidx, col in enumerate(row):
            if is_lowest_point(values, ridx, cidx):
                lowest_points.append((values[ridx][cidx], ridx, cidx))
    print(f"First part: {sum([i[0] + 1 for i in lowest_points])}")

def get_neighbours(values, ridx, cidx):
    neighbours = []
    if ridx > 0: neighbours.append((values[ridx - 1][cidx], ridx - 1, cidx))
    if ridx < len(values) - 1: neighbours.append((values[ridx + 1][cidx], ridx + 1, cidx))
    if cidx > 0: neighbours.append((values[ridx][cidx - 1], ridx, cidx - 1))
    if cidx < len(values[ridx]) - 1: neighbours.append((values[ridx][cidx + 1], ridx, cidx + 1))
    return neighbours

marked = set()
def bassin(values, ridx, cidx):
    neighbours = get_neighbours(values, ridx, cidx)
    if values[ridx][cidx] == 9 or (ridx, cidx) in marked: return 0
    marked.add((ridx, cidx))
    return 1 + sum([bassin(values, i[1], i[2]) for i in neighbours])


def part2(values):
    bassins_size = []
    for low in lowest_points:
        bassins_size.append(bassin(values, low[1], low[2]))
    print(f"Second part: {prod(sorted(bassins_size)[-3:])}")

def main():
    # values = get_input(INPUT_FILE_SMALL)
    values = get_input(INPUT_FILE)
    part1(values) # First part: 532
    part2(values) # Second part: 1110780

if __name__ == '__main__':
    main()