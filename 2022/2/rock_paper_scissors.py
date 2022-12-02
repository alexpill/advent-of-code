INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

ORD_THRESHOLD = 23

def get_input(file):
    with open(file) as f:
        return [ i.split(" ") for i in f.read().splitlines()]

def total_score(values):
    total = 0
    for oponent, me in values:
        shape_point = ord(me) - ord('X') + 1
        round_outcome = (ord(me) - ord(oponent) - ORD_THRESHOLD - 1) % 3
        round_point = (round_outcome) * 3
        total += shape_point + round_point
    return total

def exact_total_score(values):
    total = 0
    for oponent, me in values:
        round_outcome = (ord(me) - ord('X'))
        shape_point =  ((ord(oponent) - ord('A')) + round_outcome - 1)
        shape_point = shape_point % 3 + 1
        round_point = round_outcome * 3
        total += shape_point + round_point
        print(shape_point, round_point, round_point + shape_point)
    return total

def part1(values):
    print(f"First part: {total_score(values)}")

def part2(values):
    print(f"Second part: {exact_total_score(values)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 14163
    part2(values) # Second part: 12091

if __name__ == "__main__":
    main()