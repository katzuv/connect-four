from itertools import cycle

from board import Board, ColumnOutOfBoundsError, FullColumnError


def main():
    """
    Main function running the game.

    :except: ColumnOutOfBoundsError, FullColumnError, Exception
    :return: when the game has ended
    """
    board = Board()

    for player in cycle(['X', 'O']):
        print board
        while True:
            try:
                column = column_input(player)
                if board.move(column, player):
                    print board
                    print_win(player)
                    return
                break
            except ColumnOutOfBoundsError as error:
                print 'Column {} is not in board'.format(error.column + 1)
            except FullColumnError as error:
                print 'Column {} is full'.format(error.column + 1)
            except Exception as error:
                print error

        if board.is_full():
            print board
            print_game_over()
            return


def print_win(player):
    """
    Print the winner's sign.

    :param player: the winner
    :type player: str
    """
    print 'Player {} won! :)'.format(player)


def print_game_over():
    """
    Print that the board is full and the game is over.
    """
    print 'Board is full, tie.'


def column_input(player):
    """
    Input a column number from player.

    :param player: player to ask the input for
    :type player: str
    :return: column number player inputted
    :rtype: int
    """
    return int(raw_input('Player {}, enter a column number between 1 and {}: '.format(player, Board.COLUMNS))) - 1


if __name__ == '__main__':
    main()
