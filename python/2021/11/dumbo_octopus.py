from copy import deepcopy

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

MAX_EN = 9
STEPS = 100

def get_input(file):
    with open(file) as f:
        return [[int(i) for i in j] for j in f.read().splitlines()]

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            if col == 0:
                print(bcolors.HEADER + str(col) + bcolors.ENDC, end="")
            else:
                print(bcolors.OKGREEN + str(col) + bcolors.ENDC, end="")
        print()

def get_neighbors(values, ridx, cidx):
    neighbors = []
    for r in range(ridx-1, ridx+2):
        for c in range(cidx-1, cidx+2):
            if r == ridx and c == cidx:
                continue
            if r < 0 or r >= len(values) or c < 0 or c >= len(values[0]):
                continue
            neighbors.append((values[r][c], r, c))
    return neighbors

def process_cell(values, ridx, cidx, marked):
    if (ridx, cidx) in marked:
        return 0
    elif values[ridx][cidx] != 9:
        values[ridx][cidx] += 1
        return 0
    else:
        values[ridx][cidx] = 0
        marked.append((ridx, cidx))
        neighbors = get_neighbors(values, ridx, cidx)
        return 1 + sum([process_cell(values, r, c, marked) for v, r, c in neighbors])

def part1(val):
    values = deepcopy(val)
    flash_count = 0
    for step in range(STEPS):
        marked = []
        for ridx, row in enumerate(values):
            for cidx, col in enumerate(row):
                flash_count += process_cell(values, ridx, cidx, marked)
        marked.clear()
        # print(f"Step {step}:")
        # print_matrix(values)
        # print()
    print(f"First part: {flash_count}")

def part2(val):
    values = deepcopy(val)
    sync_step = 1
    while True:
        marked = []
        for ridx, row in enumerate(values):
            for cidx, col in enumerate(row):
                process_cell(values, ridx, cidx, marked)
        marked.clear()
        # print(f"Step {sync_step}:")
        # print_matrix(values)
        # print()
        if all([i.count(0) == len(i) for i in values]):
            break
        else:
            sync_step += 1
    print(f"Second part: {sync_step}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 1601
    part2(values) # Second part: 368

if __name__ == "__main__":
    main()
