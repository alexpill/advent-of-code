import numpy as np

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        values = []
        for group in f.read().split("\n\n"):
            lines = group.splitlines()
            lines = [l.split(":")[1] for l in lines]
            lines = [[i.strip() for i in l.split(",")] for l in lines]
            a, b, p = lines
            a = [int(i.split("+")[1]) for i in a]
            b = [int(i.split("+")[1]) for i in b]
            p = [int(i.split("=")[1]) for i in p]
            values.append(((a[0], b[0], p[0]), (a[1], b[1], p[1])))
        return values


# def extended_euclidean_algorithm(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         g, x1, y1 = extended_euclidean_algorithm(b % a, a)
#         x = y1 - (b // a) * x1
#         y = x1
#         return g, x, y


def process(values, threshold=0):
    button_matrix = []
    prize_matrix = []
    for A, B in values:
        xa, ya, pa = A
        xb, yb, pb = B
        button_matrix.append([[xa, ya], [xb, yb]])
        prize_matrix.append([[pa + threshold], [pb + threshold]])
    solved = np.linalg.solve(button_matrix, prize_matrix)
    rounded = np.round(solved)
    result_as_int = rounded.astype(int)
    result = 0
    for idx, value in enumerate(result_as_int):
        A, B = value
        X_confirm = A * button_matrix[idx][0][0] + B * button_matrix[idx][0][1]
        Y_confirm = A * button_matrix[idx][1][0] + B * button_matrix[idx][1][1]
        if X_confirm == prize_matrix[idx][0] and Y_confirm == prize_matrix[idx][1]:
            result += A * 3 + B
    return result[0]


def part1(values):
    result = process(values)
    print(f"First part: {result}")


def part2(values):
    result = process(values, 1e13)
    print(f"Second part: {result}")


def main():
    # values = get_input(INPUT_FILE)
    values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 31761
    part2(values)  # Second part: 90798500745591


if __name__ == "__main__":
    main()

# Solution from Reddit with cramers rule of order 2
# with open(INPUT_FILE_SMALL) as f:
#     lines = [line.rstrip() for line in f]


# def solve(part: int):
#     tokens = 0
#     add = 10000000000000 if part == 2 else 0
#     for line in lines:
#         if line.startswith("Button"):
#             l = line.split(" ")
#             a = l[1].split(":")[0]
#             if a == "A":
#                 x1 = int(l[2][2:-1])
#                 y1 = int(l[3][2:])
#             else:
#                 x2 = int(l[2][2:-1])
#                 y2 = int(l[3][2:])

#         elif line.startswith("Prize"):
#             l = line.split(" ")
#             c = int(l[1][2:-1]) + add
#             d = int(l[2][2:]) + add
#             a = (c * y2 - d * x2) / (x1 * y2 - y1 * x2)
#             b = (d * x1 - c * y1) / (x1 * y2 - y1 * x2)
#             if a == int(a) and b == int(b):
#                 tokens += int(3 * a + b)
#     print(tokens)
# solve(1)
# solve(2)

# Pretty solution from Reddit with linear regression
# M = (
#     np.fromregex(INPUT_FILE_SMALL, r"\d+", [("", int)] * 6)
#     .view(int)
#     .reshape(-1, 3, 2)
#     .swapaxes(1, 2)
# )

# for p in 0, 1e13:
#     S = M[..., :2]
#     P = M[..., 2:] + p
#     R = np.linalg.solve(S, P).round().astype(int)
#     print(*R.squeeze() @ [3, 1] @ (S @ R == P).all(1))
