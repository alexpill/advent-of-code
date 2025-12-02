from copy import deepcopy

INPUT_FILE = f"{__file__.replace('.py', '_input.txt')}"

def read_input_data(file_name):
    with open(file_name, 'r') as f:
        boards = []
        called_numbers = [int(i.strip()) for i in f.readline().split(',')]
        other = f.read().split('\n\n')
        for o in other:
            b = {
                "values": [[[int(j), 0] for j in i.split()] for i in o.split('\n') if i],
                "won": 0
            }
            boards.append(b)
        return {'called': called_numbers, 'boards': boards}

def get_matrix_column(matrix, idx):
    return [row[idx] for row in matrix]

def is_winning_board(board, row_idx, column_idx):
    is_winning = lambda arr: all([i[1] == 1 for i in arr])
    if is_winning(board[row_idx]) or is_winning(get_matrix_column(board, column_idx)):
        return True
    return False

def process_board(board, called_number):
    for row_idx, row in enumerate(board):
        for column_idx, cell in enumerate(row):
            if cell[0] == called_number:
                cell[1] = 1
            if is_winning_board(board, row_idx, column_idx):
                return board
    return None

def process_bingo(called_numbers, boards):
    winning_boards = []
    for called_number in called_numbers:
        for board in boards:
            if board['won'] == 1: continue
            winner = process_board(board["values"], called_number)
            if winner is not None:
                winning_boards.append([called_number, deepcopy(winner)]) # to keep curr state
                board['won'] = 1
    return winning_boards
    
def do_sum_of_unmarked_cell(board):
    sum_of_unmarked_cells = sum([i[0] for row in board for i in row if i[1] == 0])
    return sum_of_unmarked_cells

def get_winning_boards(data):
    data = deepcopy(data)
    called_numbers = data['called']
    boards = data['boards']
    return process_bingo(called_numbers, boards)

def part1(data):
    called_number, winning_board = get_winning_boards(data)[0]
    sum_of_unmarked_cells = do_sum_of_unmarked_cell(winning_board)
    print(f"First part: {sum_of_unmarked_cells * called_number}")

def part2(data):
    called_number, winning_board = get_winning_boards(data)[-1]
    sum_of_unmarked_cells = do_sum_of_unmarked_cell(winning_board)
    print(f"Second part: {sum_of_unmarked_cells * called_number}")

def main():
    data = read_input_data(INPUT_FILE)
    part1(data) # First part: 65325
    part2(data) # Second part: 4624

if __name__ == '__main__':
    main()