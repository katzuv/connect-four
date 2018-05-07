from board import Board

board = Board()
#                          1    2    3    4    5    6    7
board._Board__rows = [[' ', ' ', ' ', ' ', ' ', 'X', ' '],  # 1
                      [' ', ' ', ' ', ' ', ' ', 'X', ' '],  # 2
                      [' ', ' ', ' ', ' ', ' ', 'X', ' '],  # 3
                      [' ', ' ', ' ', ' ', 'X', 'X', ' '],  # 4
                      [' ', 'X', 'X', 'X', 'X', ' ', ' '],  # 5
                      [' ', ' ', 'X', ' ', ' ', ' ', ' ']]  # 6

# assert board._Board__is_winner_in_sequence(Board, ['X', 'X', 'X', 'X'], 3, 'X')
print board._Board__is_winner(6, 3, 'X')
# assert board._Board__is_winner_in_column(4, 6, 'X')
# assert board._Board__is_winner_in_column(5, 6, 'X')
