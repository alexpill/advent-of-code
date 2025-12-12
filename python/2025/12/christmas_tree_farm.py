INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        elements = f.read().split("\n\n")

        regions = elements[6:]
        regions = regions[0].splitlines()
        parsed_regions = []
        for region in regions:
            sizes, conds = region.split(":")
            x, y = [int(i) for i in sizes.split("x")]
            conds = [int(i) for i in conds.strip().split(" ")]
            parsed_regions.append(((x, y), conds))

        return parsed_regions


def solve_region(width, height, quantities):
    blocks_available = (width // 3) * (height // 3)
    pieces_needed = sum(quantities)
    return blocks_available >= pieces_needed


def part1(values):
    count = 0
    for (width, height), quantities in values:
        if solve_region(width, height, quantities):
            count += 1
    print(f"First part: {count}")


def part2(values):
    print(f"Second part:")


def main():
    values = get_input(INPUT_FILE)
    part1(values)  # First part: 567
    part2(values)  # Second part:


if __name__ == "__main__":
    main()


# Solution from Reddit (credit 4HbQ as always):
# Key insight: all shapes fit in 3x3 blocks, so just count available blocks
# import re; answer = 0
# for l in list(open('in.txt'))[30:]:
#     w,h, *n = map(int, re.findall(r'\d+', l))
#     answer += w//3 * h//3 >= sum(n)
# print(answer)
