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
    @classmethod
    def __raise_if_out_of_bounds(cls, column):
        if not 0 <= column < cls.COLUMNS:
            raise ColumnOutOfBoundsError(column)


    def __raise_if_column_is_full(self, column):
        if self.__rows[0][column] != self.EMPTY:
            raise FullColumnError(column)

class ColumnOutOfBoundsError(IndexError):
    def __init__(self, column):
        super(ColumnOutOfBoundsError, self).__init__()
        self.column = column


class FullColumnError(OverflowError):
    def __init__(self, column):
        super(FullColumnError, self).__init__()
        self.column = column
