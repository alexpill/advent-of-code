import re

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def part1(values):
    total = 0
    for value in values:
        total += sum([ int(i) * int(j) for i, j in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", value) ])
    print(f"First part: {total}")

def part2(values):
    total = 0
    doing = True
    for value in values:
        for a,b,dont,do in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(don\'t\(\))|(do\(\))", value):
            if dont != "":
                doing = False
            if do != "":
                doing = True
            if a != "" and b != "" and doing:
                total += int(a) * int(b)
    print(f"Second part: {total}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 188116424
    part2(values) # Second part: 104245808

if __name__ == "__main__":
    main()
