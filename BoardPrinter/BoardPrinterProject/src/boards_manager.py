# place your BoardsManager class in this file

from BoardPrinterProject.src.board import Board


class board_manager(object):

    def __init__(self, input_num, switch_board, quit_program):
        self.input_num = input_num
        self.switch_board = switch_board
        self.quit_program = quit_program
        self.list_of_boards = []
        self.board = []
        self.current_printing = ''

    def input_num(self) -> None:
        name = str(input('Enter the name of your board:'))
        self.list_of_boards.append(name)
        row_num = int(input('Enter the number of rows for your board:'))
        column_num = int(input('Enter the number of columns for your board:'))
        character = str(input('Enter the blank character to be used on your board:'))
        # create board
        print(name)
        board_1 = Board(row_num, column_num, character)
        self.board.append(board_1)
        # actions for remaining board
        print(
            'Select your action from the list below.\n1. Fill Spot\n2. Erase Spot\n3. Switch Board\n4. Create Board\n5. Quit')
        print('\n')  # empty line

        change_action_num = int(input('Enter the number of the action you would like to do:'))

    def switch_board(self) -> None:
        print(f'{index}{name}' for index, name in enumerate(self.list_of_boards))
        index_num = input(int('Enter the number of the board you want to switch to:'))
        for index_num in range(len(self.list_of_boards)):
            self.current_printing = self.board[index_num]
def main():
    f1 = board_managerd(3, 4, "@")
    print(f1.create_board())
    print(f1.add_spot('!', '1,0'))
    print(f1.add_spot('!', '2,1'))
    print(f1.erase_spot('2,1'))


if __name__ == '__main__':
    main()