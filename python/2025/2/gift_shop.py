INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return [tuple(int(split) for split in s.split('-')) for s in f.read().replace('\n', '').split(',')]

def part1(values):
    invalid_id_sum = 0
    for start, stop in values:
        for val in range(start, stop + 1):
            str_val = str(val)
            str_len = len(str_val) // 2
            if str_val[:str_len] == str_val[str_len:]:
                invalid_id_sum += val
    print(f"First part: {invalid_id_sum}")

def part2(values):
    invalid_id_sum = 0
    for start, stop in values:
        for val in range(start, stop + 1):
            str_val = str(val)
            stop = 1
            # print("--- val:", val)
            while stop <= len(str_val) / 2:
                if str_val.count(str_val[:stop]) == len(str_val) / stop:
                    invalid_id_sum += val
                    break
                stop += 1
    print(f"Second part: {invalid_id_sum}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 18700015741
    part2(values)  # Second part: 20077272987

if __name__ == "__main__":
    main()

# Elegant solution found on Reddit (credit to 4HbQ):
# It uses regex to find digit group
# for lo, hi in findall(r"(\d+)-(\d+)", *open("in.txt")):
#     for i in range(int(lo), int(hi) + 1):
#         if match(r"^(\d+)\1$", str(i)):
#             a += i
#         if match(r"^(\d+)\1+$", str(i)):
#             b += i
