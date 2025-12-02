from copy import deepcopy
from functools import cache
from math import floor, log10

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return f.read().split()


def process(values, iterations):  # Brute force, working for part1 not 2
    # better to use recursion and count the number of iterations instead of the array s
    result = deepcopy(values)
    for _ in range(iterations):
        new_result = []
        for value in result:
            if value == "0":
                new_result.append("1")
            elif len(value) % 2 == 0:
                new_result.append(str(int(value[: len(value) // 2])))
                new_result.append(str(int(value[len(value) // 2 :])))
            else:
                new_result.append(str(int(value) * 2024))
        result = new_result
    return result


@cache
def stone_count(value, iter_cnt):
    if iter_cnt == 0:
        return 1  # only one iteration more
    if value == 0:
        return stone_count(1, iter_cnt - 1)
    # thanks to 4HbQ in reddit for math trick
    number_len = floor(log10(value)) + 1
    if number_len % 2 != 0:
        return stone_count(value * 2024, iter_cnt - 1)
    power = 10 ** (number_len // 2)
    return stone_count(value // power, iter_cnt - 1) + stone_count(
        value % power, iter_cnt - 1
    )

def process2(values, iterations):
    result = 0
    for value in values:
        result += stone_count(int(value), iterations)
    return result

def part1(values):
    print(f"First part: {process2(values, 25)}")

def part2(values):
    print(f"Second part: {process2(values, 75)}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 228668
    part2(values)  # Second part: 270673834779359


if __name__ == "__main__":
    main()
