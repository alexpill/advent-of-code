INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return [ [int(j) for j in i.split()] for i in f.read().split('\n\n') ]

def get_row_sum(arr):
    return [ sum(i) for i in arr]

def part1(values):
    print(f"First part: {max(get_row_sum(values))}")

def get_top_three_sum(arr: list[int]):
    arr.sort(reverse=True)
    return sum(arr[0:3])

def part2(values):
    print(f"Second part: {get_top_three_sum(get_row_sum(values))}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 68787
    part2(values) # Second part: 198041

if __name__ == "__main__":
    main()