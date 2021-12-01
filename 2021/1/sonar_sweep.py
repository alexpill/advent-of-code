
INPUT_FILE = './sonar_sweep_part_1_input.txt'

def extract_data(input_file):
    with open(INPUT_FILE, 'r') as f:
        return f.read().splitlines()

def get_increase_count(values):
    counter = 0
    previous_value = values[0]
    for value in values[1:]:
        if int(value) > int(previous_value):
            counter += 1
        previous_value = value
    return counter

def three_value_sliding_window_sum(values):
    agglomaerated_values = []
    for i in range(len(values) - 2):
        agglomaerated_values.append(int(values[i]) + int(values[i + 1]) + int(values[i + 2]))
    return agglomaerated_values

def part1(depth_values):
    print(get_increase_count(depth_values))

def part2(depth_values):
    agglomaerated_values = three_value_sliding_window_sum(depth_values)
    print(get_increase_count(agglomaerated_values))

def main():
    depth_values = extract_data(INPUT_FILE)
    part1(depth_values)
    part2(depth_values)

if __name__ == '__main__':
    main()