INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

def get_input(file):
    with open(file) as f:
        return [list(map(lambda x: int(x),list(i))) for i in f.read().splitlines()]

def is_edge_tree(trees, x, y):
    return x == 0 or x == len(trees) - 1 or y == 0 or  y == len(trees[0]) - 1

def is_visible(tree, left, right, top, bottom):
    return tree > max(left) or tree > max(right) or tree > max(top) or tree > max(bottom)

def get_cardinal_tree(values, x, y) -> list[list[int], list[int], list[int], list[int]]:
    left, right = values[x][:y], values[x][y+1:]
    top = [row[y] for row in values[:x]]
    bottom = [row[y] for row in values[x+1:]]
    return left, right, top, bottom

def process_tree(values, x, y):
    if is_edge_tree(values, x, y):
        return 1
    left, right, top, bottom = get_cardinal_tree(values, x, y)
    if is_visible(values[x][y], left, right, top, bottom):
        return 1
    return 0

def visible_tree_count(values):
    count = 0
    for x in range(len(values)):
        for y in range(len(values[x])):
            count += process_tree(values, x, y)
    return count

def score_of_list(list_, tree, reverse=False):
    if tree > max(list_):
        return len(list_)
    if reverse:
        return list_[::-1].index(next(filter(lambda x: x >= tree, list_[::-1]))) + 1
    else:
        return list_.index(next(filter(lambda x: x >= tree, list_))) + 1

def process_tree_score(values, x, y):
    score = 1
    tree = values[x][y]
    if is_edge_tree(values, x, y):
        return 0
    left, right, top, bottom = get_cardinal_tree(values, x, y)
    score *= score_of_list(left, tree, True)
    score *= score_of_list(top, tree, True)
    score *= score_of_list(right, tree)
    score *= score_of_list(bottom, tree)
    return score

def highest_scenic_score(values):
    score = 0
    for x in range(len(values)):
        for y in range(len(values[x])):
            score = max(score, process_tree_score(values, x, y))
    return score

def part1(values):
    print(f"First part: {visible_tree_count(values)}")

def part2(values):
    print(f"Second part: {highest_scenic_score(values)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 1809
    part2(values) # Second part: 479400

if __name__ == "__main__":
    main()