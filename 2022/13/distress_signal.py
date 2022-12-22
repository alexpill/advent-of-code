INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        pair_of_packet_raw = [i for i in f.read().split('\n\n')]
        return [[eval(j) for j in i.splitlines()] for i in pair_of_packet_raw]

def pair_list_compare(pair: list[list]):
    left_iter = iter(pair[0])
    right_iter = iter(pair[1])
    curr_l = next(left_iter, None)
    curr_r = next(right_iter, None)
    while curr_l and curr_r:
        diff = pair_compare([curr_l, curr_r])
        if diff != 0:
            return -1 if diff < 0 else 1
        curr_l = next(left_iter, None)
        curr_r = next(right_iter, None)
    return -1 if curr_l is None else 1

def pair_compare(pair: list):
    left = pair[0]
    right = pair[1]
    if type(left) is int and type(right) is int:
        return left - right
    if type(left) is int:
        left = [left]
    if type(right) is int:
        right = [right]
    return pair_list_compare([left, right])

def right_order_pairs_indices_sum(values):
    count = 0
    for idx, pair in enumerate(values):
        if pair_compare(pair) < 0:
            count += idx + 1
    return count

def part1(values):
    print(f"First part: {right_order_pairs_indices_sum(values)}")

def part2(values):
    print(f"Second part:")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part:
    part2(values)  # Second part:

if __name__ == "__main__":
    main()
