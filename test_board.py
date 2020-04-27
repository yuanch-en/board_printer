import unittest
from unittest.mock import patch
import unittest
from unittest.mock import patch
from BoardPrinterProject.src import board


class TestBoard(unittest.TestCase):
    def test_create_board(self):
        user_input = board.Board(3, 4, '@')
        answer = user_input.create_board()
        self.assertEqual(answer, '  0 1 2 3\n0 @ @ @ @\n1 @ @ @ @\n2 @ @ @ @')

        user_input = board.Board(1, 1, '@')
        answer = user_input.create_board()
        self.assertEqual(answer, '  0\n0 @')

        user_input = board.Board(3, 2, '?')

        answer = user_input.create_board()
        self.assertEqual(answer, '  0 1\n0 ? ?\n1 ? ?\n2 ? ?')


    def test_add(self):
        # erase is the same
        user_input = board.Board(3, 2, '?')
        board1 = user_input.create_board()
        answer = user_input.add_spot('+', '1,0')
        self.assertEqual(answer, '  0 1\n0 ? ?\n1 + ?\n2 ? ?')
        answer2 = user_input.add_spot('+', '  2, 1 ')
        self.assertEqual(answer2, '  0 1\n0 ? ?\n1 + ?\n2 ? +')


        user_input2 = board.Board(3, 2, '?')
        board2 = user_input2.create_board()
        answer = user_input2.add_spot('+', '2, 0')
        self.assertEqual(answer, '  0 1\n0 ? ?\n1 ? ?\n2 + ?')

        user_input3 = board.Board(3, 2, '?')
        board3 = user_input3.create_board()
        answer = user_input3.add_spot('+', '  2, 0 ')
        self.assertEqual(answer, '  0 1\n0 ? ?\n1 ? ?\n2 + ?')







if __name__ == '__main__':
    unittest.main()
