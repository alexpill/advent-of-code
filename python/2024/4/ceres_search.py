from collections import defaultdict

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


def check_unit(x, y, values, unitRef):
    if x < 0 or y < 0 or y >= len(values) or x >= len(values[0]):
        return False
    return values[y][x] == unitRef


def check_neighbors(values, x, y, ref):
    found = [0] * 8
    for i in range(1, len(ref)):
        if check_unit(x + i, y, values, ref[i]):
            found[0] += 1
        if check_unit(x - i, y, values, ref[i]):
            found[1] += 1
        if check_unit(x, y + i, values, ref[i]):
            found[2] += 1
        if check_unit(x, y - i, values, ref[i]):
            found[3] += 1
        if check_unit(x + i, y + i, values, ref[i]):
            found[4] += 1
        if check_unit(x - i, y - i, values, ref[i]):
            found[5] += 1
        if check_unit(x - i, y + i, values, ref[i]):
            found[6] += 1
        if check_unit(x + i, y - i, values, ref[i]):
            found[7] += 1

    return len(list(filter(lambda x: x == len(ref) - 1, found)))


def part1(values):
    values = [[i for i in x] for x in values]
    count = 0
    ref = "XMAS"
    for y in range(0, len(values)):
        for x in range(0, len(values)):
            if values[y][x] == ref[0]:
                count += check_neighbors(values, x, y, ref)
    print(f"First part: {count}")


def check_neighbors2(values, x, y, ref):
    found = [0] * 4
    for i in range(-int(len(ref) / 2), int(len(ref) / 2) + 1):
        if check_unit(x + i, y + i, values, ref[i + int(len(ref) / 2)]):
            found[0] += 1
        if check_unit(x - i, y - i, values, ref[i + int(len(ref) / 2)]):
            found[1] += 1
        if check_unit(x + i, y - i, values, ref[i + int(len(ref) / 2)]):
            found[2] += 1
        if check_unit(x - i, y + i, values, ref[i + int(len(ref) / 2)]):
            found[3] += 1
    return len(list(filter(lambda x: x == len(ref), found))) >= 2


def part2(values):
    values = [[i for i in x] for x in values]
    count = 0
    ref = "MAS"
    for y in range(0, len(values)):
        for x in range(0, len(values)):
            if values[y][x] == ref[int(len(ref) / 2)]:
                count += check_neighbors2(values, x, y, ref)
    print(f"Second part: {count}")


def main():
    # values = get_input(INPUT_FILE)
    values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 2654
    part2(values)  # Second part: 1990


if __name__ == "__main__":
    main()

# Reddit response
# from collections import defaultdict

# G = defaultdict(str) | {
#     (i, j): c for i, r in enumerate(open(0)) for j, c in enumerate(r)
# }
# g = list(G.keys())
# D = -1, 0, 1

# T = (list("XMAS"),)
# print(
#     sum(
#         [G[i + di * n, j + dj * n] for n in range(4)] in T
#         for di in D
#         for dj in D
#         for i, j in g
#     )
# )

# T = list("MAS"), list("SAM")
# print(
#     sum(
#         [G[i + d, j + d] for d in D] in T and [G[i + d, j - d] for d in D] in T
#         for i, j in g
#     )
# )
