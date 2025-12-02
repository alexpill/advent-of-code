INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

from collections import deque

id_ = 0
def get_id():
    global id_
    id_ += 1
    return id_

class Node:
    def __init__(self, value, is_start = False, is_end = False):
        self.id = get_id()
        self.value = value
        self.is_start = is_start
        self.is_end = is_end

    def __repr__(self) -> str:
        return f"({self.id},'{self.value}')"
    def __eq__(self, __o: object) -> bool:
        if type(__o) != Node: return False
        return self.id == __o.id
    def __hash__(self) -> int:
        return hash(self.id)

    def can_access(self, __o: 'Node', step=1):
        o_value = __o.value if not __o.is_end else 'z'
        s_value = self.value if not self.is_start else 'a'
        return ord(o_value) - ord(s_value) <= step

def values_to_node(values):
    matrix: list[list[Node]] = []
    for line in values:
        matrix_line: list[Node] = []
        for col in line:
            is_start = col == 'S'
            is_end = col == 'E'
            matrix_line.append(Node(col, is_start, is_end))
        matrix.append(matrix_line)
    return matrix

def get_adjacents(matrix: list[list[Node]], x: int, y: int) -> list[Node]:
    adjacents: list[Node] = []
    if x > 0: adjacents.append(matrix[x - 1][y])
    if x < len(matrix) - 1: adjacents.append(matrix[x + 1][y])
    if y > 0: adjacents.append(matrix[x][y - 1])
    if y < len(matrix[x]) - 1: adjacents.append(matrix[x][y + 1])
    return adjacents

def create_graph(values):
    matrix = values_to_node(values)
    start, end = None, None
    graph = dict()
    for r_id, row in enumerate(matrix):
        for c_id, col in enumerate(row):
            if col.is_start: start = col
            if col.is_end: end = col
            adjacents = get_adjacents(matrix, r_id, c_id)
            neighbours = [i for i in adjacents if col.can_access(i)]
            graph[col] = neighbours
    return graph, start, end

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def breadth_first_search(graph, start, end):
    queue = deque([[start, 0]])
    visited = set([start])
    while queue:
        node, distance = queue.popleft()
        if node == end:
            return distance
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append([neighbour, distance + 1])
                visited.add(neighbour)
    return -1

def part1(values):
    graph, start, end = create_graph(values)
    print(f"First part: {breadth_first_search(graph, start, end)}")

def get_min_distance_from_min_points(values):
    graph, _, end = create_graph(values)
    starts = [i for i in graph if i.value == 'a' or i.is_start]
    distances = list(filter(lambda x: x != -1, [breadth_first_search(graph, i, end) for i in starts]))
    return min(distances)

def part2(values):
    print(f"Second part: {get_min_distance_from_min_points(values)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 504
    part2(values) # Second part: 500

if __name__ == "__main__":
    main()