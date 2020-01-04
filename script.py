import random

LEFT_SIDE = [52,4,6,5]
RIGHT_SIDE = 40

def get_symbols(left_side, right_side):
    solved = False
    SYMBOLS = ['+', '-', '/', '*']
    while not solved:
        goal_solution = left_side[0]
        symbols = SYMBOLS
        random.shuffle(symbols)
        symbols = symbols[0:3]
        for i, symbol in enumerate(symbols):
            if symbol == '+':
                goal_solution += left_side[i + 1]
            elif symbol == '-':
                goal_solution -= left_side[i + 1]
            elif symbol == '/':
                goal_solution /= left_side[i + 1]
            elif symbol == '*':
                goal_solution *= left_side[i + 1]
        if goal_solution == right_side:
            solved = True
    print symbols

get_symbols(LEFT_SIDE, RIGHT_SIDE)
