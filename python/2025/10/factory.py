from functools import reduce
from itertools import combinations
from scipy.optimize import linprog


INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"


def bool_arr_to_bits(arr):
    return sum(v << i for i, v in enumerate(arr[::-1]))

class Machine:
    def __init__(self, lights, buttons, voltage) -> None:
        self.l = lights
        self.b = buttons
        self.v = voltage

    def to_bits(self):
        l_bits = bool_arr_to_bits(self.l)
        b_bits = []
        for b in self.b:
            arr = []
            for i in range(len(self.l)):
                arr.append(i in b)
            b_bits.append(bool_arr_to_bits(arr))
        return l_bits, b_bits

    def __repr__(self):
        return f"{"".join(['#' if f else '.' for f in self.l])} {self.b} {self.v}"


def get_input(file: str) -> list[Machine]:
    machines: list[Machine] = []
    with open(file) as f:
        for line in f.read().splitlines():
            light, *button, voltage = line.split(" ")
            light = [i == "#" for i in light[1:-1]]
            button = [[int(s) for s in b[1:-1].split(",")] for b in button]
            voltage = list(eval(voltage[1:-1]))
            machines.append(Machine(light, button, voltage))
    return machines


def part1(values: list[Machine]):
    bests = []
    for val in values:
        l, b = val.to_bits()
        found = False
        i = 0
        while not found:
            for c in combinations(b, i):
                permut = reduce(lambda a, b: a ^ b, c, 0b0)
                if permut == l:
                    bests.append(i)
                    found = True
                    break
            if found:
                break
            i += 1
    print(f"First part: {sum(bests)}")


def part2(values):
    # linear prog: https://en.wikipedia.org/wiki/Linear_programming
    total_presses = 0
    for machine in values:
        numbers = range(len(machine.v))
        c = [1 for _ in machine.b]
        A = [[i in button for button in machine.b] for i in numbers]
        total_presses += linprog(c, A_eq=A, b_eq=machine.v, integrality=1).fun
    print(f"Second part: {int(total_presses)}")


def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values)  # First part: 488
    part2(values)  # Second part:


if __name__ == "__main__":
    main()
