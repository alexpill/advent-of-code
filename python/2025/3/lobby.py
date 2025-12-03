from functools import reduce


INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def get_input(file):
    with open(file) as f:
        return [[int(a) for a in s] for s in f.read().splitlines()]


def part1(values):
    bank_maxs = []
    for bank in values:
        ten_idx = 0
        digit_idx = 1
        for idx in range(len(bank) - 1):
            if bank[idx] > bank[ten_idx]:
                ten_idx = idx
                digit_idx = idx + 1
                continue
            if bank[idx] > bank[digit_idx] and idx > digit_idx:
                digit_idx = idx
        if bank[-1] > bank[digit_idx]:
            digit_idx = len(bank) - 1
        bank_maxs.append(bank[ten_idx] * 10 + bank[digit_idx])
    print(f"First part: {sum(bank_maxs)}")


def part2(values, max_len=12):
    banks_maxs = []
    for bank in values:
        remaining = len(bank) - max_len
        bank_max = []
        for idx, val in enumerate(bank):
            if len(bank_max) == 0 or val <= bank_max[-1] or remaining == 0:
                if len(bank_max) < max_len:
                    bank_max.append(val)
                else:
                    remaining -= 1
                continue
            for i, v in enumerate(bank_max):
                if val > v and remaining >= len(bank_max) - i:
                    remaining -= len(bank_max) - i
                    bank_max = bank_max[:i]
                    break
            if len(bank_max) < max_len:
                bank_max.append(val)

        banks_maxs.append(reduce(lambda a, b: a * 10 + b, bank_max))
    print(f"Second part: {sum(banks_maxs)}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 17207
    part2(values)  # Second part:


if __name__ == "__main__":
    main()


# Very pretty solution from Reddit as always.
# Using reducing sliding window
# def f(line, start=0, answer=""):
#     for end in range(101 - n, 101):
#         best = max(line[start:end])
#         start = line.index(best, start) + 1
#         answer += best
#     return int(answer)


# for n in 2, 12:
#     print(sum(map(f, open("in.txt"))))
