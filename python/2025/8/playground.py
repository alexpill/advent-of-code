from collections import Counter
import enum
from functools import reduce
from math import sqrt
from operator import add


INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size  # Rank helps in balancing the tree

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def same_set(self, x, y):
        return self.find(x) == self.find(y)


def has_cycle(edges, n):
    uf = UnionFind(n)
    for u, v in edges:
        if uf.same_set(u, v):
            return True  # Cycle detected
        uf.union(u, v)
    return False


def count_components(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return len(set(uf.find(i) for i in range(n)))


def get_input(file):
    with open(file) as f:
        return [tuple(int(g) for g in s.split(",")) for s in f.read().splitlines()]


def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def kruskal_mst(points):
    edges = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = dist(points[i], points[j])
            edges.append((distance, i, j))

    edges.sort()

    uf = UnionFind(len(points))
    total_distance = 0
    last_edge = None

    for distance, i, j in edges:
        if not uf.same_set(i, j):
            uf.union(i, j)
            total_distance += distance
            last_edge = (distance, i, j)

            if total_distance == len(points) - 1:
                break

    return last_edge


def part1(values, small):
    distances = {}

    for a in values:
        for b in values:
            if a == b:
                continue
            distances[dist(a, b)] = [a, b]

    mins = sorted(distances.keys())
    point_to_index = {point: i for i, point in enumerate(values)}
    uf = UnionFind(len(values))

    for i, distance in enumerate(mins):
        if small and i == 10 or i == 1000:
            break
        point_a, point_b = distances[distance]
        idx_a = point_to_index[point_a]
        idx_b = point_to_index[point_b]
        uf.union(idx_a, idx_b)

    root_counts = Counter(uf.find(i) for i in range(len(values)))
    top_3_sizes = [count for root, count in root_counts.most_common(3)]

    print(f"First part: {reduce(lambda a, b: a * b, top_3_sizes)}")


def part2(values):
    # Utilise Kruskal pour trouver l'arbre couvrant minimal
    last_edge = kruskal_mst(values)

    # La dernière arête ajoutée avant d'avoir l'arbre couvrant complet
    distance, i, j = last_edge
    print(f"Second part: {values[i][0] * values[j][0]}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values, small=False)  # First part: 175440
    part2(values)  # Second part: 3200955921


if __name__ == "__main__":
    main()
