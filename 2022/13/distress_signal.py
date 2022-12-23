INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

from functools import cmp_to_key

def get_input(file):
    with open(file) as f:
        return [[*map(eval, i.split())] for i in f.read().split('\n\n')]

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
    match left, right:
        case int(), int():
            return left - right
        case int(), list():
            return pair_compare([[left], right])
        case list(), int():
            return pair_compare([left, [right]])
        case list(), list():
            return pair_list_compare([left, right])

def right_order_pairs_indices_sum(values):
    count = 0
    for i, pair in enumerate(values):
        compare = pair_compare(pair)
        if compare < 0:
            count += i + 1
    return count

def divider_packets(values):
    first_val, second_val = [[2]], [[6]]
    vals = [first_val, second_val]
    sorted_values = sorted(sum(values, vals), key=cmp_to_key(lambda a, b: pair_compare([a, b])))
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

# Another solution for comparison:
# def cmp(l, r):
#     match l, r:
#         case int(), int():  return (l>r) - (l<r)
#         case int(), list(): return cmp([l], r)
#         case list(), int(): return cmp(l, [r])
#         case list(), list():
#             for z in map(cmp, l, r):
#                 if z: return z
#             return cmp(len(l), len(r))