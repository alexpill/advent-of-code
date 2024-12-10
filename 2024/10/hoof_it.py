from queue import SimpleQueue, LifoQueue
from copy import deepcopy

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        G = {
            i + j * 1j: int(c)
            for j, l in enumerate(f.read().splitlines())
            for i, c in enumerate(l)
        }
        return G


def part1(values):
    starts = [k for k, v in values.items() if v == 0]
    scores = []
    for start in starts:
        result = 0
        queue = SimpleQueue() # better to use DFS instead of BFS next time
        queue.put(start)
        visited = set()
        while not queue.empty():
            current = queue.get()
            for i in [1, -1, 1j, -1j]:
                new = current + i
                new_value = values.get(new)
                if (
                    new in values
                    and new not in visited
                    and new_value == values[current] + 1
                ):
                    if new_value == 9:
                        result += 1
                    queue.put(new)
                    visited.add(new)
        scores.append(result)
    print(f"First part: {sum(scores)}")


def part2(values):
    starts = [k for k, v in values.items() if v == 0]
    scores = []
    for start in starts:
        result = 0
        queue = LifoQueue() # DFS without visited set
        queue.put(start)
        # visited = set()
        while not queue.empty():
            current = queue.get()
            # if current not in visited:
            #     visited.add(current)
            for i in [1, -1, 1j, -1j]:
                new = current + i
                new_value = values.get(new)
                # if new in values and new not in visited and new_value == values[current] + 1:
                if new in values and new_value == values[current] + 1:
                    if new_value == 9:
                        result += 1
                    queue.put(new)
        scores.append(result)
    print(f"Second part: {sum(scores)}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 459
    part2(values)  # Second part: 1034


if __name__ == "__main__":
    main()
