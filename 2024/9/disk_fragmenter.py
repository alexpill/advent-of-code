from functools import reduce
from collections import defaultdict

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return [int(x) for x in f.read().splitlines()[0]]


def get_data(values):
    data = ["."] * sum(values)
    data_table = defaultdict(tuple)
    cursor = 0
    idx = 0
    for i, value in enumerate(values):
        if i % 2 == 0:
            for j in range(value):
                data[(cursor + j)] = idx
            data_table[idx] = (cursor, cursor + value)
            idx += 1
        cursor += value
    return data, data_table


def part1(values):
    data, _ = get_data(values)
    ri = len(data) - 1
    dot_count = data.count(".")
    for i in range(len(data)):
        while data[ri] == ".":
            ri -= 1
        if len(data) - 1 - ri == dot_count:
            break
        if data[i] == ".":
            data[i] = data[ri]
            data[ri] = "."
            ri -= 1
            # [print(x, end='') for x in data]
            # print()

    result = reduce(
        lambda x, y: x + y[0] * y[1] if y[1] != "." else x,
        [x for x in enumerate(data)],
        0,
    )
    print(f"First part: {result}")


def part2(values):
    data, table = get_data(values)
    for key, value in reversed(table.items()):
        f_len = value[1] - value[0]
        for i in range(value[0]):
            if data[i] == "." and all(map(lambda x: x == ".", data[i : i + f_len])):
                for j in range(f_len):
                    data[i + j] = key
                    data[table[key][0] + j] = "."
                break

    result = reduce(
        lambda x, y: x + y[0] * y[1] if y[1] != "." else x,
        [x for x in enumerate(data)],
        0,
    )

    print(f"Second part: {result}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 6463499258318
    part2(values)  # Second part: 6493634986625


if __name__ == "__main__":
    main()
