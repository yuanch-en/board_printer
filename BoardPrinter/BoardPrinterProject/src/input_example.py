from typing import List


# some example functions that use input
# to demonstrate how to test them in
# test/test_input_examples

def name_board() -> str:
    a = str(input('Enter the first number: '))
    return a


def multi_line_gatherer() -> List:
    num_lines = int(input('How many lines will you enter: '))
    lines = []
    for i in range(num_lines):
        line = input(f'Enter line {i}: ')
        lines.append(line)
    return lines
