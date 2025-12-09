from itertools import combinations, pairwise


INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return [tuple(int(a) for a in s.split(",")) for s in f.read().splitlines()]


def part1(values):
    values = sorted(values)
    max_area = 0
    for i, v in enumerate(values):
        for j in values[i:]:
            a, b = v
            c, d = j
            area = (abs(a - c) + 1) * (abs(b - d) + 1)
            max_area = max(max_area, area)
    print(f"First part: {max_area}")


def get_perimeter(values):
    perimeter = set()
    for i in range(len(values)):
        p1 = values[i]
        p2 = values[(i + 1) % len(values)]
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                perimeter.add((x1, y))
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                perimeter.add((x, y1))
    return perimeter


def part2(values):
    max_area = 0
    green = list(pairwise(values + [values[0]]))  # first element for cycling
    for (x1, y1), (x2, y2) in combinations(values, 2):
        area = (abs(y1 - y2) + 1) * (abs(x1 - x2) + 1)
        if area > max_area:
            for (x3, y3), (x4, y4) in green:
                if ( # aabb to test intersection between line and rect
                    min(x3, x4) < max(x1, x2)
                    and max(x3, x4) > min(x1, x2)
                    and min(y3, y4) < max(y1, y2)
                    and max(y3, y4) > min(y1, y2)
                ):
                    break
            else:
                max_area = area

    print(f"Second part: {max_area}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part:
    part2(values)  # Second part:


if __name__ == "__main__":
    main()

# ..............
# .......#XXX#..
# .......XXXXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# .........XXX..
# .........#X#..
# ..............
