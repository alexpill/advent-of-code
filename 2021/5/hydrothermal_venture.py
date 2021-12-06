INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"
INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __repr__(self):
        return f"{self.p1} -> {self.p2}"
    def min_x(self):
        return min(self.p1.x, self.p2.x)
    def min_y(self):
        return min(self.p1.y, self.p2.y)
    def max_x(self):
        return max(self.p1.x, self.p2.x)
    def max_y(self):
        return max(self.p1.y, self.p2.y)

class Matrix:
    def __init__(self, values, size=None):
        self.inner_lines = values
        self.size_x, self.size_y = size if size else get_matrix_size(values)
        self._arr = [['.' for x in range(self.size_x)] for y in range(self.size_y)]
    def __repr__(self):
        return f"{self.size_x}x{self.size_y} matrix"
    def print(self):
        for row in self._arr:
            print(''.join(row))
    def fill(self, vertical_only=True):
        for line in self.inner_lines:
            self.fill_line(line, vertical_only)
    def fill_line(self, line, vertical_only=True):
        line_is_diagonal = line.p1.x != line.p2.x and line.p1.y != line.p2.y
        if vertical_only and line_is_diagonal:
            return
        elif line_is_diagonal:
            self.fill_diagonal(line)
        else:
            self.fill_vertical(line)

    def compute_values(self, curr_value):
        return str(int(curr_value) + 1) if curr_value != '.' else '1'

    def fill_vertical(self, line):
        for x in range(line.min_x(), line.max_x() + 1):
            for y in range(line.min_y(), line.max_y() + 1):
                self._arr[y][x] = self.compute_values(self._arr[y][x])

    def fill_diagonal(self, line):
        y = line.p1.y
        x = line.p1.x
        while abs(y - line.p2.y) > 0 and abs(x - line.p2.x) > 0:
            self._arr[y][x] = self.compute_values(self._arr[y][x])
            y += 1 if y <= line.p2.y else -1
            x += 1 if x <= line.p2.x else -1
        self._arr[y][x] = self.compute_values(self._arr[y][x])

    def count_values_above(self, value):
        count = 0
        for row in self._arr:
            for char in row:
                if char != '.':
                    if int(char) >= value:
                        count += 1
        return count

def get_input(file=INPUT_FILE):
    with open(file) as f:
        for line in f:
            p1_raw, p2_raw = line.strip().split('->')
            x1, y1 = p1_raw.strip().split(',')
            x2, y2 = p2_raw.strip().split(',')
            p1 = Point(int(x1), int(y1))
            p2 = Point(int(x2), int(y2))
            yield Line(p1, p2)

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def get_matrix_size(values):
    return (max(map(lambda x: x.max_x(), values)) + 1,
            max(map(lambda x: x.max_y(), values)) + 1)

def part1(values):
    matrix = Matrix(values)
    print(matrix)
    matrix.fill()
    dangerous_areas_count = matrix.count_values_above(2)
    print(f"First part: {dangerous_areas_count}")

def part2(values):
    matrix = Matrix(values)
    print(matrix)
    matrix.fill(vertical_only=False)
    dangerous_areas_count = matrix.count_values_above(2)
    print(f"Second part: {dangerous_areas_count}")

def main():
    values_small = list(get_input(INPUT_FILE_SMALL))
    values = list(get_input(INPUT_FILE))
    part1(values) # First part: 5092
    part2(values) # Second part: 20484

if __name__ == "__main__":
    main()