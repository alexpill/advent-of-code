INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

class Game:
    def __init__(self, index, sets):
        self.index = index
        self.sets = sets

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


def value_parser(values):
    game_split = [line.split(':')[1] for line in values]
    return [[[{'value':int(j.split()[0]), 'color': j.split()[1]} for j in i.split(',')] for i in line.split(';')] for line in game_split]

def get_impossible_games(games):
    for game_index, game in enumerate(games):
        for subset in game:
            should_break = False
            for cube in subset:
                if cube['color'] == 'red' and cube['value'] > MAX_RED or \
                   cube['color'] == 'green' and cube['value'] > MAX_GREEN or \
                   cube['color'] == 'blue' and cube['value'] > MAX_BLUE:
                    yield game_index + 1
                    should_break = True
                    break
            if should_break:
                break

def get_cube_power(games):
    for game in games:
        max_red = 0
        max_green = 0
        max_blue = 0
        for subset in game:
            for cube in subset:
                if cube['color'] == 'red' and cube['value'] > max_red:
                    max_red = cube['value']
                if cube['color'] == 'blue' and cube['value'] > max_blue:
                    max_blue = cube['value']
                if cube['color'] == 'green' and cube['value'] > max_green:
                    max_green = cube['value']
        yield max_green * max_red * max_blue

def part1(values):
    value_count = len(values)
    sum_of_indexes = value_count * (value_count + 1) // 2
    print(f"First part: {sum_of_indexes - sum([i for i in get_impossible_games(values)])}")

def part2(values):
    print(f"Second part: {sum(get_cube_power(values))}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    parsed_value = value_parser(values)
    part1(parsed_value) # First part: 1853
    part2(parsed_value) # Second part: 72706

if __name__ == "__main__":
    main()


## Incredible solution :
# from collections import Counter
# from functools import reduce
# from operator import mul, or_

# thres = Counter({"red":12, "green":13, "blue":14})

# tot_1 = 0
# tot_2 = 0
# with open("input.txt", "r") as f:
#     for game in f:
#         game_id, draws = game.strip().split(": ")
#         game_id = int(game_id.split(" ")[1])
#         draws = [[c.split(" ") for c in d.split(", ")] for d in draws.split("; ")]
#         draws = [Counter({c[1]:int(c[0]) for c in d}) for d in draws]
#         tot_1 += all(d<=thres for d in draws) * game_id
#         tot_2 += reduce(mul, reduce(or_, draws).values())

# print(1, tot_1)
# print(2, tot_2)