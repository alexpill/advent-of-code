from collections import defaultdict

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        G = {i + j * 1j: c for i, r in enumerate(f) for j, c in enumerate(r.strip())}
        return G


def pretty_print(values):
    for x in range(12):
        for y in range(12):
            print(values[x + y * 1j], end="")
        print()


def part1(values):
    antennas_types = defaultdict(list)
    visited = set()
    for p in values:
        if values[p] != ".":
            antennas_types[values[p]].append(p)
    result = 0
    for t in antennas_types:
        antennas = antennas_types[t]
        for a in antennas:
            for b in filter(lambda x: x != a, antennas):
                antenna_diff = b - a
                coef = 1
                while a + coef * antenna_diff in values:
                    antinodes = a + coef * antenna_diff
                    if antinodes in values and antinodes not in visited:
                        result += 1
                        if values[antinodes] == ".":
                            values[antinodes] = "#"
                        visited.add(antinodes)
                    coef += 1
    pretty_print(values)
    print(f"First part: {result}")


def part2(values):
    print(f"Second part:")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 396 -> only with coef 2
    part2(values)  # Second part: 1200


if __name__ == "__main__":
    main()
