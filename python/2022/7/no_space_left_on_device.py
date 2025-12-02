INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"
# INPUT_FILE_SMALL = f"{__file__.replace('.py', '_input_small.txt')}"

class Symbols:
    ROOT = '/'
    COMMAND = '$'
    PARENT = '..'

class Node:
    def __init__(self, name, parent, size = -1):
        self.name = name
        self.is_dir = True if size == -1 else False
        self.size = size
        self.total_size = 0 if self.is_dir else size
        self.children = []
        self.parent = parent
    def __repr__(self):
        return f"{self.name}\t{self.size}\t{self.total_size}\t{self.parent}\t{self.children}"

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()

def update_path(current_path, dir_):
    match dir_:
        case Symbols.PARENT:
            current_path.pop()
        case Symbols.ROOT:
            current_path = ['/']
        case _:
            current_path.append(dir_)

def get_command(line):
    _, command, *args = line.split()
    return command, args

def get_file_node(line, path):
    size_or_dir, file = line.split()
    parent = '/' + '/'.join(path[1:])
    filename = (parent if parent != '/' else '') + '/' + file
    return Node(filename, parent) if size_or_dir == 'dir' else Node(filename, parent, int(size_or_dir))

def propagate_size(files, node: Node, size):
    if node.parent == '/':
        files['/'].total_size += size
        return
    files[node.parent].total_size += size
    propagate_size(files, files[node.parent], size)

def add_file(files, file_node: Node):
    files[file_node.name] = file_node
    files[file_node.parent].children.append(file_node.name)
    if not file_node.is_dir:
        propagate_size(files, file_node, file_node.size)

def process_command(command, args, current_path):
    match command:
        case 'ls':
            return True
        case 'cd':
            update_path(current_path, args[0])
            return False
        case _:
            raise ValueError(f"Unknown command: {command}")

def get_file_tree(values: list[str]):
    current_path = ['/']
    files = { "/": Node('/', '')}
    list_mode = False
    for line in values:
        if line.startswith(Symbols.COMMAND):
            command, args = get_command(line)
            list_mode = process_command(command, args, current_path)
        elif list_mode:
            node = get_file_node(line, current_path)
            add_file(files, node)
    return files

def get_bellow_100k_total_size(values):
    files = get_file_tree(values)
    total = 0
    for file in files:
        file_node = files[file]
        if file_node.total_size < 100000 and file_node.is_dir: total += files[file].total_size
    return total

def get_to_remove_dir_size(values):
    needed = 30000000
    files = get_file_tree(values)
    remaining_space = 70000000 - files[Symbols.ROOT].total_size
    candidate = 99999999999999999999
    for file in files:
        file_node = files[file]
        if not file_node.is_dir:
            continue
        if remaining_space + file_node.total_size >= needed and file_node.total_size < candidate:
            candidate = file_node.total_size
    return candidate

def part1(values):
    print(f"First part: {get_bellow_100k_total_size(values)}")

def part2(values):
    print(f"Second part: {get_to_remove_dir_size(values)}")

def main():
    values = get_input(INPUT_FILE)
    # values = get_input(INPUT_FILE_SMALL)
    part1(values) # First part: 1886043
    part2(values) # Second part: 3842121

if __name__ == "__main__":
    main()