INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

from functools import cmp_to_key

def get_input(file):
    with open(file) as f:
        pair_of_packet_raw = [i for i in f.read().splitlines()]
        return list(map(eval, filter(lambda x: x != '', pair_of_packet_raw)))

def pair_list_compare(pair: list[list]):
    left_iter = iter(pair[0])
    right_iter = iter(pair[1])
    curr_l = next(left_iter, None)
    curr_r = next(right_iter, None)
    while curr_l is not None and curr_r is not None:
        diff = pair_compare([curr_l, curr_r])
        if diff != 0:
            return -1 if diff < 0 else 1
        curr_l = next(left_iter, None)
        curr_r = next(right_iter, None)
    if curr_l is None and curr_r is None:
        return 0
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
    for i in range(0, len(values), 2):
        compare = pair_compare([values[i], values[i+1]])
        if compare < 0:
            count += i//2 + 1
    return count

def divider_packets(values):
    first_val, second_val = [[2]], [[6]]
    values = values + [first_val, second_val]
    sorted_values = sorted(values, key=cmp_to_key(lambda a, b: pair_compare([a, b])))
    return (sorted_values.index(first_val) + 1) * (sorted_values.index(second_val) + 1)

def part1(values):
    print(f"First part: {right_order_pairs_indices_sum(values)}")

def part2(values):
    print(f"Second part: {divider_packets(values)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 5717
    part2(values)  # Second part: 25935

if __name__ == "__main__":
    main()
