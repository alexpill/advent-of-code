INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

class MyRange:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    def isFullyContaining(self, other):
        return self.start <= other.start and self.end >= other.end

    def isOverlapping(self, other):
        return max(self.start, other.start) <= min(self.end, other.end)

    def __repr__(self) -> str:
        return f"{self.start}-{self.end}"
    def __str__(self):
        return f"{self.start}-{self.end}"

def get_input(file):
    with open(file) as f:
        return [[ MyRange(*j.split('-')) for j in i.split(',')] for i in f.read().splitlines()]



def get_fully_containing_count(values):
    count = 0
    for r1, r2 in values:
        if r1.isFullyContaining(r2) or r2.isFullyContaining(r1):
            count += 1
    return count

def get_overlapping_count(values):
    count = 0
    for r1, r2 in values:
        if r1.isOverlapping(r2):
            count += 1
    return count

def part1(values):
    print(f"First part: {get_fully_containing_count(values)}")

def part2(values):
    print(f"Second part: {get_overlapping_count(values)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 496
    part2(values) # Second part: 847

if __name__ == "__main__":
    main()