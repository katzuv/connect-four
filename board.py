class Board(object):
    def __init__(self):
        self.__rows = [[' ' for _ in xrange(7)] for _ in xrange(6)]

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.__rows)

    def is_full(self):
        return all(' ' not in row for row in self.__rows)

    def move(self, column, player):
        '''
        :return: Whether player won the game after this move.
        '''
        row = self.__insert(column, player)
        return self.__is_winner(player, row, column)

    def __insert(self, column, player):
        self.__raise_if_column_is_full(column)
        raise NotImplementedError()

    def __raise_if_column_is_full(self, column):
        raise NotImplementedError()

    def __is_winner(self, player, row, column):
        raise NotImplementedError()


class FullColumnError(Exception):
    def __init__(self, column):
        super(FullColumnError, self).__init__('Column {} is full'.format(column))
