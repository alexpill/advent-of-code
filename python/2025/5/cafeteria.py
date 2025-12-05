INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        ranges, ingredients = f.read().split("\n\n")
        ranges = [[int(s) for s in f.split("-")] for f in ranges.splitlines()]
        ingredients = [int(f) for f in ingredients.splitlines()]
        return (ranges, ingredients)

def simplify_ranges(ranges):
    new_ranges = []
    for a in sorted(ranges):
        for i, b in enumerate(new_ranges):
            if a[0] >= b[0] and a[1] <= b[1]:
                new_ranges[i] = [b[0], b[1]]
                break
            elif a[0] <= b[0] and a[1] <= b[1] and a[1] >= b[0]:
                new_ranges[i] = [a[0], b[1]]
                break
            elif a[0] >= b[0] and a[1] >= b[1] and a[0] <= b[1]:
                new_ranges[i] = [b[0], a[1]]
                break
            elif a[0] <= b[0] and a[1] >= b[1]:
                new_ranges[i] = [a[0], a[1]]
                break
        else:
            new_ranges.append(a)
    return new_ranges


def part1(values):
    fresh_cnt = 0
    ranges, ingredients = values
    ranges = simplify_ranges(ranges)
    for ing in ingredients:
        for r in ranges:
            if ing in range(r[0], r[1] + 1):
                fresh_cnt += 1
    print(f"First part: {fresh_cnt}")


def part2(values):
    ranges = values[0]
    ranges = simplify_ranges(ranges)
    id_cnt = 0
    for r in ranges:
        id_cnt += len(range(r[0], r[1] + 1))
    print(f"Second part: {id_cnt}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 701
    part2(values)  # Second part: 352340558684863


if __name__ == "__main__":
    main()
