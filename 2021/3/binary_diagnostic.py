INPUT_FILE = "binary_diagnostic_input.txt"

BIT_COUNT = 12

def read_values(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]

def one_value_bit_count(values, bit_count=BIT_COUNT):
    bit_per_index = [0] * bit_count
    for value in values:
        for i in range(bit_count):
            if value[i] == "1":
                bit_per_index[i] += 1
    return bit_per_index

is_most_common = lambda x, y: x >= len(y) / 2

def part1(values):
    gamma_rate = ""
    one_bit_count = one_value_bit_count(values)
    for bit in one_bit_count:
        gamma_rate += "1" if is_most_common(bit, values) else "0"
    epsilon_rate = ~int(gamma_rate, 2) & 0xFFF
    power_consumption = int(gamma_rate, 2) * epsilon_rate
    print(f"First part: {power_consumption}")

def filtering(values, is_least_common=False):
    new_val = values.copy()
    current_index = 0
    while len(new_val) > 1:
        bit_cnt = one_value_bit_count(new_val)[current_index]
        cond = not is_most_common(bit_cnt, new_val) if is_least_common else is_most_common(bit_cnt, new_val)
        filter_func = lambda x: x[current_index] == ("1" if cond else "0")
        new_val = list(filter(filter_func, new_val))
        current_index += 1
    return new_val[0]

def part2(values):
    oxygen_generator_rating = int(filtering(values), 2)
    co2_scrubber_rating = int(filtering(values, True), 2)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(f"Second part: {life_support_rating}")

def main():
    values = read_values(INPUT_FILE)
    part1(values) # First part: 3847100
    part2(values) # Second part: 4105235

if __name__ == '__main__':
    main()