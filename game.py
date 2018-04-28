from itertools import cycle

from board import Board, FullColumnError


def main():
    board = Board()

    for player in cycle(['X', 'O']):
        print board
        while True:
            try:
                column = column_input(player)
                if board.move(column, player):
                    print_win(player)
                    return
                break
            except (ValueError, FullColumnError) as error:
                print error

        if board.is_full():
            print_game_over()
            return


def print_win(player):
    print 'Player {} won! :)'.format(player)


def print_game_over():
    print 'Board is full, tie.'


def column_input(player):
    return int(raw_input('Player {}, enter a column number between 1 and 7: '.format(player))) - 1


if __name__ == '__main__':
    main()
