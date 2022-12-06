INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def is_start_packet(packet, packet_size = 4):
    return len(set(packet)) == packet_size

def get_packet_start_index(datastream, packet_size = 4):
    sliding_window = list(datastream[:packet_size])
    if is_start_packet(sliding_window, packet_size): return packet_size
    for i in range(len(datastream) - packet_size):
        sliding_window.pop(0)
        sliding_window.append(datastream[i + packet_size])
        if is_start_packet(sliding_window, packet_size): return packet_size + i + 1
    return -1

def char_processing_count(datastreams, packet_size = 4):
    count = 0
    for datastream in datastreams:
        index = get_packet_start_index(datastream, packet_size)
        print(index)
        count += index
    return count

def part1(values):
    print(f"First part: {char_processing_count(values)}")

def part2(values):
    print(f"Second part: {char_processing_count(values, 14)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 1623
    part2(values) # Second part: 3744

if __name__ == "__main__":
    main()