class Board(object):
    ROWS = 6
    COLUMNS = 7
    EMPTY = ' '
    TARGET = 4

    def __init__(self):
        self.__rows = [[self.EMPTY for _ in xrange(self.COLUMNS)] for _ in xrange(self.ROWS)]

    def __str__(self):
        return '\n'.join('\033[1m' + str(i) + '\033[0;0m' + ' ' + ' '.join(row) for i, row in enumerate(self.__rows, start=1)) + '\n' + \
        '\033[1m' + '  1 2 3 4 5 6 7' + '\033[0;0m'

    def is_full(self):
        return all(self.EMPTY not in row for row in self.__rows)

    def move(self, column, player):
        '''
        :return: Whether player won the game after this move.
        '''
        row = self.__insert(column, player)
        return self.__is_winner(player, row, column)

    def __insert(self, column, player):
        self.__raise_if_out_of_bounds(column)
        self.__raise_if_column_is_full(column)
        for i, row in enumerate(reversed(self.__rows)):
            if row[column] != self.EMPTY:
                continue
            row[column] = player
            return i

    def __is_winner(self, player, row, column):
        return self.__is_winner_in_row(player, row, column) \
               or self.__is_winner_in_column(player, row, column) \
               or self.__is_winner_in_descending_diagonal(player, row, column) \
               or self.__is_winner_in_ascending_diagonal(player, row, column)

    def __is_winner_in_row(self, player, row, column):
        return self.__is_winner_in_sequence(player, self.__rows[row], column)

    def __is_winner_in_column(self, player, row, column):
        return self.__is_winner_in_sequence(player, [r[column] for r in self.__rows], row)

    def __is_winner_in_descending_diagonal(self, player, row, column):
        if row >= column:
            difference = row - column
            return self.__is_winner_in_sequence(
                player,
                [self.__rows[i][i - difference]
                 for i in xrange(difference, min(self.ROWS, difference + self.COLUMNS))],
                column)
        difference = column - row
        return self.__is_winner_in_sequence(
            player,
            [self.__rows[i - difference][i] for i in xrange(difference, min(difference + self.ROWS, self.COLUMNS))],
            row)

    def __is_winner_in_ascending_diagonal(self, player, row, column):
        sum = row + column
        if sum < self.ROWS:
            return self.__is_winner_in_sequence(player, [self.__rows[sum - i][i] for i in xrange(sum + 1)], column)
        return self.__is_winner_in_sequence(
            player,
            [self.__rows[sum - i][i] for i in xrange(sum - (self.ROWS - 1), min(sum + 1, self.COLUMNS))],
            column - sum + (self.ROWS - 1))

    @classmethod
    def __is_winner_in_sequence(cls, player, sequence, index):
        target_slice = [player] * cls.TARGET
        return any(sequence[start:start + cls.TARGET] == target_slice
                   for start in xrange(max(0, index - (cls.TARGET - 1)), index + 1))

    @classmethod
    def __raise_if_out_of_bounds(cls, column):
        if not 0 <= column < cls.COLUMNS:
            raise ColumnOutOfBoundsError(column)

    def __raise_if_column_is_full(self, column):
        if self.__rows[0][column] != self.EMPTY:
            raise FullColumnError(column)

    def __is_winner(self, player, row, column):
        raise NotImplementedError()

class ColumnOutOfBoundsError(IndexError):
    def __init__(self, column):
        super(ColumnOutOfBoundsError, self).__init__()
        self.column = column

class FullColumnError(Exception):
    def __init__(self, column):
        super(FullColumnError, self).__init__()
        self.column = column
