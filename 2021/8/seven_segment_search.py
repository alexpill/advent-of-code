INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"
INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"

one_len = 2
four_len = 4
seven_len = 3
eight_len = 7

def get_input(filename):
    with open(filename, 'r') as f:
        raw_values = [i.strip().split("|") for i in f.readlines()]
        values = [{"sig_pattern": i[0].strip().split(), "out_digit": i[1].strip().split()} for i in raw_values]
        return values

def part1(values):
    one_four_seven_heights_cnt = 0
    for val in values:
        for digit_out in val["out_digit"]:
            d_len = len(digit_out)
            if d_len == one_len or d_len == four_len or d_len == seven_len or d_len == eight_len:
                one_four_seven_heights_cnt += 1
    print(f"First part: {one_four_seven_heights_cnt}")

# Inspired by https://www.reddit.com/r/adventofcode/comments/rbj87a/comment/hnoyy04/?utm_source=share&utm_medium=web2x&context=3
def part2(values):
    s = 0
    for val in values:
        segment_by_size = {len(s) : set(s) for s in val["sig_pattern"]}
        inter = lambda x, y: len(x & segment_by_size[y])
        out_num = ""
        for out_dig in map(set, val["out_digit"]):
            if len(out_dig) == one_len: out_num += "1"
            elif len(out_dig) == seven_len: out_num += "7"
            elif len(out_dig) == four_len: out_num += "4"
            elif len(out_dig) == eight_len: out_num += "8"
            elif len(out_dig) == 5 and inter(out_dig, 4) == 2: out_num += "2"
            elif len(out_dig) == 5 and inter(out_dig, 4) == 3 and inter(out_dig, 2) == 1: out_num += "5"
            elif len(out_dig) == 5 and inter(out_dig, 4) == 3 and inter(out_dig, 2) == 2: out_num += "3"
            elif len(out_dig) == 6 and inter(out_dig, 4) == 4: out_num += "9"
            elif len(out_dig) == 6 and inter(out_dig, 4) == 3 and inter(out_dig, 2) == 1: out_num += "6"
            elif len(out_dig) == 6 and inter(out_dig, 4) == 3 and inter(out_dig, 2) == 2: out_num += "0"
        s += int(out_num)
    print(f"Second part: {s}")
    pass

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 495
    part2(values) # Second part: 1055164

if __name__ == "__main__":
    main()