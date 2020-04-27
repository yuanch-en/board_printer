# Place your Board class in this file

from typing import List

class Board(object):

    def __init__(self, board_size_rows, board_size_cols, board_blank):
        self.board_size_rows = board_size_rows
        self.board_size_cols = board_size_cols
        self.board_blank = board_blank
        self.current_board = ''

    def create_board(self) -> str:
        # board_size_rows = int(input('Enter the number of rows for your board: '))
        # board_size_cols = int(input('Enter the number of columns for your board: '))
        # board_blank = input('Enter the blank character to be used on your board: ')

        new_board = []
        first_row = [' ']  # leave the first space

        for k in range(self.board_size_cols):
            first_row.append(str(k))
        first_row_str = ' '.join(first_row)
        new_board.append(first_row_str)  # make the first row of numbers

        for i in range(self.board_size_rows):
            row = [str(i)]  # the index number before each row
            for k in range(self.board_size_cols):
                row.append(self.board_blank)
            new_board.append(' '.join(row))  # join the row
            self.current_board = '\n'.join(new_board)  # join the board with new lines
        return self.current_board  # is a string

    def add_spot(self, new_chr, position) -> str:
        """

        :param new_chr:
        :param position:
        :return:

        """
        current_list = self.current_board.split('\n')  # turn the string into a list of rows
        position_list = position.split(',')  # take the position as row and col
        index_row = int(position_list[0])
        index_col = int(position_list[1])  # str to int
        row = current_list[index_row + 1]
        row_list = list(row)  # find the row and seperate the characters into a new list
        row_list[index_col*2 + 2] = new_chr  # change the character
        current_list[index_row + 1] = ''.join(row_list)
        self.current_board = '\n'.join(current_list)  # join the lists back together
        return self.current_board

    def erase_spot(self, position):
        """

        :param position:
        :return:
        """

        current_list = self.current_board.split('\n')  # turn the string into a list of rows
        position_list = position.split(',')  # take the position as row and col
        index_row = int(position_list[0])
        index_col = int(position_list[1])  # str to int
        row = current_list[index_row + 1]
        row_list = list(row)  # find the row and seperate the characters into a new list
        row_list[index_col*2 + 2] = self.board_blank  # change the character
        current_list[index_row + 1] = ''.join(row_list)
        self.current_board = '\n'.join(current_list)  # join the lists back together
        return self.current_board

    def __str__(self):
        return f'self.current_board'


def main():
    f1 = Board(3, 4, "@")
    print(f1.create_board())
    print(f1.add_spot('!', '1,0'))
    print(f1.add_spot('!', '2,1'))
    print(f1.erase_spot('2,1'))


if __name__ == '__main__':
    main()
