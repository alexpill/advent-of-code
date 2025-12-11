from collections import deque

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"
INPUT_FILE_SMALL_PART_2 = f"{__file__.replace('.py', '_input_small_part2.txt')}"


def get_input(file):
    with open(file) as f:
        nodes = dict()
        for line in f.read().splitlines():
            node, neighbours = line.split(":")
            neighbours = neighbours.strip().split(" ")
            nodes[node] = neighbours
        return nodes


def dfs(graph, node):
    count = 0
    visited = set()
    stack = deque()
    stack.append(node)
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for n in graph[node]:
                if n == "out":
                    count += 1
                    visited = set()
                    break
                elif n not in visited:
                    stack.append(n)
    return count

def dfs_with_cond(graph, start, end):
    from functools import cache
    @cache
    def dp(node, visited_dac, visited_fft):
        if node == end:
            return 1 if visited_dac and visited_fft else 0
        count = 0
        for neighbor in graph.get(node, []):
            new_dac = visited_dac or (neighbor == 'dac')
            new_fft = visited_fft or (neighbor == 'fft')
            count += dp(neighbor, new_dac, new_fft)
        return count
    return dp(start, False, False)

def part1(values):
    count = dfs(values, "you")
    print(f"First part: {count}")


def part2(values):
    count = dfs_with_cond(values, 'svr', 'out')
    print(f"Second part: {count}")


def main():
    values= get_input(INPUT_FILE)
    values1 = get_input(INPUT_FILE_SMALL)
    values2 = get_input(INPUT_FILE_SMALL_PART_2)
    part1(values1)  # First part: 497
    part2(values)  # Second part:


if __name__ == "__main__":
    main()

# As always: solution from Reddit (credit to 4HbQ):
# Note: seems like it was a good choice to use cache
# from functools import cache

# G = {k[:-1]: v for k, *v in map(str.split, open("in.txt"))}

# @cache
# def count(here, dac, fft):
#     match here:
#         case "out":
#             return dac and fft
#         case "dac":
#             dac = True
#         case "fft":
#             fft = True

#     return sum(count(next, dac, fft) for next in G[here])


# print(count("you", 1, 1), count("svr", 0, 0))
