from queue import SimpleQueue
from collections import defaultdict
from copy import deepcopy

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        G = { i + j * 1j: c for j, line in enumerate(f.read().splitlines()) for i, c in enumerate(line) }
        return G


def flood_fill(G, start):
    area = set()
    q = SimpleQueue()
    q.put(start)
    while not q.empty():
        pos = q.get()
        if G.get(pos) == G.get(start):
            area.add(pos)
            for d in [1, -1, 1j, -1j]:
                if pos + d in G and pos + d not in area:
                    q.put(pos + d)
    return area

def get_bounds(area, G):
    bounds = set()
    # P = {(p,d) for d in (+1,-1,+1j,-1j) for p in area if p+d not in area}
    # other_P = P - {(p+d*1j,d) for p,d in P}
    for i in area:
        for d in [1, -1, 1j, -1j]:
            if i + d not in area:
                bounds.add((i, d))
    other_bounds = set()
    for pos, dir_ in bounds:
        other_bounds.add((pos+dir_*1j, dir_))
    return len(bounds), len(bounds - other_bounds)

def part1(values):
    sets = {p: {p} for p in values}
    for key in values:
        for d in [1, -1, 1j, -1j]:
            if key + d in values and values[key] == values[key + d]:
                sets[key] |= sets[key + d]
                for s in sets[key]:
                    sets[s] = sets[key]
    sets = { tuple(s) for s in sets.values()}
    result = sum([len(s) * get_bounds(s, values)[0] for s in sets])
    print(f"First part: {result}")

def part2(values):
    sets = {p: {p} for p in values}
    for key in values:
        for d in [1, -1, 1j, -1j]:
            if key + d in values and values[key] == values[key + d]:
                sets[key] |= sets[key + d]
                for s in sets[key]:
                    sets[s] = sets[key]
    sets = { tuple(s) for s in sets.values()}
    result = sum([len(s) * get_bounds(s, values)[1] for s in sets])
    print(f"Second part: {result}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 1473408
    part2(values)  # Second part: 886364

if __name__ == "__main__":
    main()
