from collections import defaultdict
from copy import deepcopy

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return [[char for char in row] for row in f.read().splitlines()]


def find_guard(values):
    for i in range(len(values)):
        for j in range(len(values[i])):
            if values[i][j] in ["^", "v", "<", ">"]:
                return values[i][j], (i, j)
    return None

add = lambda x, y: tuple(map(sum, zip(x, y)))
in_bounds = lambda values, x, y: 0 <= x < len(values) and 0 <= y < len(values[0])

def process(values):
    g_dir, g_pos = find_guard(values)
    dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    keys = list(dirs.keys())
    visited = defaultdict(set)

    while in_bounds(values, *g_pos) and g_dir not in visited[g_pos]:
        visited[g_pos].add(g_dir)
        next_pos = add(g_pos, dirs[g_dir])
        if in_bounds(values, *next_pos) and values[next_pos[0]][next_pos[1]] == "#":
            g_dir = keys[(keys.index(g_dir) + 1) % len(dirs)]
        else:
            g_pos = next_pos

    return visited, g_pos in visited and g_dir in visited[g_pos] # reading the visited[g_pos] adds the last position


def part(values):
    visited, _ = process(values)
    loop_cnt = 0
    for x, y in list(visited.keys())[1:]:
        h_values = deepcopy(values)
        h_values[x][y] = "#"
        _, loop = process(h_values)
        loop_cnt += loop

    print(f"First part: { len(visited) }")
    print(f"Second part: { loop_cnt }")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part(values)  # First part: 4580
    # Second part: 1480


if __name__ == "__main__":
    main()

# Best solution found on Reddit
# G = {
#     i + j * 1j: c
#     for i, r in enumerate(open(INPUT_FILE))
#     for j, c in enumerate(r.strip())
# }

# start = min(p for p in G if G[p] == "^")

# def walk(G):
#     pos, dir, seen = start, -1, set()
#     while pos in G and (pos, dir) not in seen:
#         seen |= {(pos, dir)}
#         if G.get(pos + dir) == "#":
#             dir *= -1j
#         else:
#             pos += dir
#     return {p for p, _ in seen}, (pos, dir) in seen


# path = walk(G)[0]
# print(len(path), sum(walk(G | {o: "#"})[1] for o in path))
