INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

import functools as ft
import math
from copy import deepcopy

class Monkey:
    def __init__(self, start_items, operation, divider, success_monkey, fail_monkey):
        self.items = start_items
        self.operation = operation
        self.divider = divider
        self.success_monkey = success_monkey
        self.fail_monkey = fail_monkey
        self.inspect_count = 0

    def __repr__(self) -> str:
        return f"{self.items} {self.operation(1)} {self.success_monkey} {self.fail_monkey}"

    def do_round(self, monkeys, product_of_divider=None):
        for item in self.items:
            self.inspect_count += 1
            worry_level = self.operation(item)
            if product_of_divider is None:
                worry_level //= 3
            else:
                worry_level %= product_of_divider # (a % kn) % n = a % n because a % n ∈[0,𝑛−1]
            if worry_level % self.divider == 0:
                monkeys[self.success_monkey].items.append(worry_level)
            else:
                monkeys[self.fail_monkey].items.append(worry_level)
        self.items = []

def parse_monkey(monkey_raw):
    instructions = monkey_raw.splitlines()
    start_items = [int(i) for i in instructions[1].split(':')[1].split(',')]
    operation = lambda old: eval(instructions[2].split(':')[1].split('=')[1]) # oopsie woopsie this is dirty
    divider = int(instructions[3].split('by')[1])
    success_monkey = int(instructions[4].split('monkey')[1])
    fail_monkey = int(instructions[5].split('monkey')[1])
    return Monkey(start_items, operation, divider, success_monkey, fail_monkey)

def get_input(file):
    monkeys = []
    with open(file) as f:
        for monkey_raw in f.read().split('\n\n'):
            monkeys.append(parse_monkey(monkey_raw))
    return monkeys

def get_monkey_business_level(monkeys_: list[Monkey], round_count, alternative=False):
    monkeys = deepcopy(monkeys_)
    product_of_dividers = math.prod([monkey.divider for monkey in monkeys]) if alternative else None
    for _ in range(round_count):
        for monkey in monkeys:
            monkey.do_round(monkeys, product_of_dividers)
    # could have used math.prod
    return ft.reduce(lambda a, b: a * b, sorted([i.inspect_count for i in monkeys], reverse=True)[0:2])

def part1(values):
    print(f"First part: {get_monkey_business_level(values, 20)}")

def part2(values):
    print(f"Second part: {get_monkey_business_level(values, 10000, alternative=True)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 121450
    part2(values) # Second part: 28244037010

if __name__ == "__main__":
    main()