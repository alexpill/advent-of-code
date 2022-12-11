INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"
# INPUT_FILE_SMALL_VARIANT = f"{__file__.replace('.py', '_input_small_variant.txt')}"

import os

def get_input(file):
    with open(file) as f:
        return [ [i.split()[0], int(i.split()[1])] for i in f.read().splitlines()]

def display_grid(size_x, size_y, head_pos, all_pos, pause=True, clear_start=True, clear_end=False, x_offset = 0, y_offset = 0):
    if clear_start: os.system('clear')
    print(f"head: x={head_pos[0]}, y={head_pos[1]}")
    for y in range(-y_offset, size_y - y_offset):
        for x in range(-x_offset, size_x - x_offset):
            if (x , (size_y - 2 * y_offset) - 1 - y) == head_pos:
                print('H', end="")
                continue
            for idx, pos in enumerate(all_pos):
                if (x, (size_y - 2 * y_offset) - 1 - y) == pos:
                    print(str(idx + 1) if idx != len(all_pos) - 1 else 'T', end="")
                    break
            else:
                print('.', end="")
        print()
    if pause: input()
    if clear_end: os.system('clear')

def pretty_display(positions, size_x, size_y, x_offset=0, y_offset=0):
    for head, *tail in positions:
        display_grid(size_x, size_y, head, tail, x_offset=x_offset, y_offset=y_offset)

def compute_new_head_position(last_head, direction):
    x_step = 0 if direction == 'U' or direction == 'D' else 1 if direction == 'R' else -1
    y_step = 0 if direction == 'L' or direction == 'R' else -1 if direction == 'D' else 1
    last_head_x, last_head_y = last_head
    return (last_head_x + x_step, last_head_y + y_step)

def compute_new_position(last_pos, new_prev):
    x_diff = new_prev[0] - last_pos[0]
    y_diff = new_prev[1] - last_pos[1]
    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return (last_pos[0], last_pos[1])
    x_offset = 1 if x_diff > 0 else -1 if x_diff < 0 else 0
    y_offset = 1 if y_diff > 0 else -1 if y_diff < 0 else 0
    return (last_pos[0] + x_offset, last_pos[1] + y_offset)

def step_in_direction(positions, direction, rope_length):
    new_head = compute_new_head_position(positions[-1][0], direction)
    all_new_pos = tuple([new_head])
    for i in range(rope_length):
        new_pos = compute_new_position(positions[-1][i + 1], all_new_pos[-1])
        all_new_pos += tuple([new_pos])
    positions.append(all_new_pos)
    return all_new_pos[-1]

def get_visited_position_count(values, rope_length):
    positions = [[(0, 0), *[(0, 0) for _ in range(rope_length)]]]
    unique_tail_positions = set()
    for direction, count in values:
        for _ in range(count):
            new_pos = step_in_direction(positions, direction, rope_length)
            unique_tail_positions.add(new_pos)
    # pretty_display(positions, 6, 5) # For small example
    # pretty_display(positions, 26, 17, 11, 5) # For small example variant
    return len(unique_tail_positions)

def part1(values):
    print(f"First part: {get_visited_position_count(values, 1)}")

def part2(values):
    print(f"Second part: {get_visited_position_count(values, 9)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    # values = get_input(INPUT_FILE_SMALL_VARIANT)
    part1(values) # First part: 5858
    part2(values) # Second part:

if __name__ == "__main__":
    main()