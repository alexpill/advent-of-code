import itertools
from operator import add, mul
from functools import reduce

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def process_input(values, operators = [add, mul]):
    total_calibrations = 0
    for line in values:
        lres, nums = line.split(":")
        lres, nums = int(lres), [int(x) for x in nums.split()]
        products = [i for i in itertools.product(operators, repeat=(len(nums) - 1))]
        for product in products:
            res = nums[0]
            for index, num in enumerate(nums[1:]):
                res = product[index](res, num)
            if res == lres:
                total_calibrations += lres
                break
    return total_calibrations

def concat(a, b):
    return int(str(a) + str(b))

def part1(values):
    print(f"First part: {process_input(values)}")

def part2(values):
    print(f"Second part: {process_input(values, [add, mul, concat])}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part:
    part2(values) # Second part:

if __name__ == "__main__":
    main()