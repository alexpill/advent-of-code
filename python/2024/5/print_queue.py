from collections import defaultdict
from functools import cmp_to_key

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        first, second = f.read().split("\n\n")
        return first.splitlines(), second.splitlines()


def process_values(is_after_raw, update_raw):
    is_after = defaultdict(set)
    for line in is_after_raw:
        after, key = line.split("|")
        is_after[int(after)].add(int(key))
    return is_after, [[int(j) for j in x.split(",")] for x in update_raw]


def resolve_values(is_after, updates):
    valid = []
    invalid = []
    for update in updates:
        processed = set()
        for page in update:
            if is_after[page] & processed:
                invalid.append(update)
                break
            processed.add(page)
        else:
            valid.append(update)
    return valid, invalid


def part1(values):
    is_after, updates = values
    is_after, updates = process_values(is_after, updates)
    valid, _ = resolve_values(is_after, updates)
    print(f"First part: {sum([x[len(x) // 2] for x in valid])}")


def part2(values):
    is_after, updates = values
    is_after, updates = process_values(is_after, updates)
    _, invalid = resolve_values(is_after, updates)
    result = 0
    for update in invalid:
        new_valid = []
        processed = set()
        for page in update:
            if is_after[page] & processed:
                intersection_list = list(is_after[page] & processed)
                insert_index = min([new_valid.index(x) for x in intersection_list])
                new_valid.insert(insert_index, page)
            else:
                new_valid.append(page)
            processed.add(page)
        result += new_valid[len(new_valid) // 2]
    print(f"Second part: {result}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 5452
    part2(values)  # Second part:


if __name__ == "__main__":
    main()

# And as always a pretty solution from reddit using cmp_to_key
# from functools import cmp_to_key

# rules, pages = open(INPUT_FILE_SMALL).read().split("\n\n")
# cmp = cmp_to_key(lambda x, y: -(x + "|" + y in rules))

# a = [0, 0]
# for p in pages.split():
#     p = p.split(",")
#     s = sorted(p, key=cmp)
#     a[p != s] += int(s[len(s) // 2])

# print(*a)
