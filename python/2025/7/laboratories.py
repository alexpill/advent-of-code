INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


def part1(values):
    values = values[:]
    split = 0
    for i in range(1, len(values)):
        for j in range(len(values[i])):
            if values[i - 1][j] == "S":
                new = list(values[i])
                new[j] = "|"
                values[i] = "".join(new)
            elif values[i][j] == "^" and values[i - 1][j] == "|":
                new = list(values[i])
                new[j - 1] = "|"
                new[j + 1] = "|"
                values[i] = "".join(new)
                split += 1
            elif values[i - 1][j] == "|":
                new = list(values[i])
                new[j] = "|"
                values[i] = "".join(new)
    print(f"First part: {split}")


def get_char(c):
    if c == "S":
        return 1
    if c == ".":
        return 0
    if c == "^":
        return -1


def part2(values):
    values = values[:]
    split = 0

    for i in range(len(values)):
        values[i] = list(values[i])
        for j in range(len(values[i])):
            values[i][j] = get_char(values[i][j])

    for i in range(1, len(values)):
        old = list(values[i-1])
        new = list(values[i])
        for j in range(len(new)):
            val = 0
            if new[j] == -1:
                continue
            if j < len(new) - 1 and new[j+1] == -1:
                val += old[j+1]
            if j > 0 and new[j-1] == -1:
                val += old[j-1]
            if old[j] != -1:
                val += old[j]
            if val != 0:
                new[j] = val
        values[i] = new
    print(f"Second part: {sum(values[-1])}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 1592
    part2(values)  # Second part: 17921968177009


if __name__ == "__main__":
    main()

# Pretty version from Reddit (credit to 4HbQ)
# The use of a single array being updated is very pretty
# first, *rest = open(INPUT_FILE_SMALL)

# a = 0
# b = [c == "S" for c in first]

# for line in rest:
#     for i in range(len(line)):
#         if line[i] == "^":
#             a += bool(b[i])
#             b[i - 1] += b[i]
#             b[i + 1] += b[i]
#             b[i] = 0

# print(a, sum(b))