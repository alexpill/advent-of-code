INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"

def get_input(filename):
    with open(filename, 'r') as f:
        return [int(i) for i in f.read().strip().split(",")]

def part1(values):
    min_fuel_cost = None
    for i in range(max(values) + 1):
        fuel_cost = sum([abs(val - i) for val in values])
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
    print(f"First part: {min_fuel_cost}")

def part2(values):
    min_fuel_cost = None
    for i in range(max(values) + 1):
        # sum of all natural numbers : (N * (N + 1)) / 2
        fuel_cost = sum([(abs(val - i) * (abs(val - i) + 1)) // 2 for val in values])
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
    print(f"Second part: {min_fuel_cost}")

def main():
    values = get_input(INPUT_FILE)
    part1(values) # First part: 355150
    part2(values) # Second part: 98368490

if __name__ == "__main__":
    main()