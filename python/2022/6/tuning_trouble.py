INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read()

def get_packet_start_index(datastream, packet_size = 4):
    for i in range(len(datastream) - packet_size + 1):
        if (len(set(datastream[i : i + packet_size]))) == packet_size: return i + packet_size

def part1(values):
    print(f"First part: {get_packet_start_index(values)}")

def part2(values):
    print(f"Second part: {get_packet_start_index(values, 14)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 1623
    part2(values) # Second part: 3774

if __name__ == "__main__":
    main()