INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

import string
import re
from copy import deepcopy

def gen_movements(movements_input: str):
    return [[int(j) for j in re.findall(r'[0-9]+', line)] for line in movements_input.splitlines()]

def gen_stacks(stacks_input: str):
    stack_matrix = [i.replace('    ', '[]').replace(' ', '').replace(']', ' ').replace('[', '').rstrip().split(' ') for i in stacks_input.splitlines()]
    column_ids = list(stack_matrix.pop().pop())
    stack_list = [[] for _ in column_ids]
    for row in reversed(stack_matrix):
        for idx, column in enumerate(row):
            if column != '': stack_list[idx].append(column)
    return stack_list

def get_input(file):
    with open(file) as f:
        stacks, movements = f.read().split('\n\n')
        return gen_stacks(stacks), gen_movements(movements)

def get_final_end_of_stacks(stacks_: list[str], movements: list[int], tool_method):
    stacks = deepcopy(stacks_)
    for iter_count, start, end in movements:
        tool_method(stacks, iter_count, start, end)
    return get_top_stack_values(stacks)

def crate_mover_9000(stacks, iter_count, start, end):
    for _ in range(iter_count):
        stacks[end -1].append(stacks[start - 1].pop())

def crate_mover_9001(stacks, iter_count, start, end):
    stacks[end - 1] += stacks[start - 1][-iter_count:]
    stacks[start - 1] = stacks[start - 1][:-iter_count]

def get_top_stack_values(stacks):
    end_str = ''
    for stack in stacks:
        end_str += stack[-1]
    return end_str

def part1(values):
    print(f"First part: {get_final_end_of_stacks(*values, crate_mover_9000)}")

def part2(values):
    print(f"Second part: {get_final_end_of_stacks(*values, crate_mover_9001)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: FRDSQRRCD
    part2(values) # Second part: HRFTQVWNN

if __name__ == "__main__":
    main()