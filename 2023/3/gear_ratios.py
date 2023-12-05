import re
from functools import reduce
from operator import mul

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def add_border_to_matrix(raw_matrix):
    matrix = [['.' for i in range(len(raw_matrix[0]) + 2)]]
    matrix += [['.'] + line + ['.'] for line in raw_matrix]
    matrix += [['.' for i in range(len(raw_matrix[0]) + 2)]]
    return matrix


def get_part_numbers(raw_matrix):
    matrix = add_border_to_matrix(raw_matrix)
    part_numbers = []
    for rid, row in enumerate(matrix):
        for cid, column in enumerate(row):
            if column != '.' and re.match('\W{1}', column):
                visited = []
                for i in range(rid-1, rid+2):
                    for j in range(cid-1, cid+2):
                        if matrix[i][j].isdigit() and (i, j) not in visited:
                            string = ''
                            left_index = j
                            right_index = j+1
                            while matrix[i][left_index].isdigit():
                                string = matrix[i][left_index] + string
                                visited += [(i, left_index)]
                                left_index -= 1
                            while matrix[i][right_index].isdigit():
                                string += matrix[i][right_index]
                                visited += [(i, right_index)]
                                right_index += 1
                            part_numbers.append(int(string))
    return sum(part_numbers)

def get_gear_ratio(raw_matrix):
    matrix = add_border_to_matrix(raw_matrix)
    final_sum = 0
    for rid, row in enumerate(matrix):
        for cid, column in enumerate(row):
            found_number = []
            if re.match('\*{1}', column):
                visited = []
                for i in range(rid-1, rid+2):
                    for j in range(cid-1, cid+2):
                        if matrix[i][j].isdigit() and (i, j) not in visited:
                            string = ''
                            left_index = j
                            right_index = j+1
                            while matrix[i][left_index].isdigit():
                                string = matrix[i][left_index] + string
                                visited += [(i, left_index)]
                                left_index -= 1
                            while matrix[i][right_index].isdigit():
                                string += matrix[i][right_index]
                                visited += [(i, right_index)]
                                right_index += 1
                            found_number.append(int(string))
            if len(found_number) == 2:
                final_sum += reduce(mul, found_number)
    return final_sum

def part1(values):
    result = get_part_numbers([[j for j in line] for line in values])
    print(f"First part: {result}")

def part2(values):
    result = get_gear_ratio([[j for j in line] for line in values])
    print(f"Second part: {result}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 544433
    part2(values) # Second part: 76314915

if __name__ == "__main__":
    main()