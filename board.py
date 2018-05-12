class Board(object):
    """Class that represents a Connect Four board."""
    ROWS = 6
    COLUMNS = 7
    EMPTY = ' '
    TARGET = 4

    def __init__(self):
        """Initialize a Connect Four board."""
        self.__rows = [[self.EMPTY for _ in xrange(self.COLUMNS)] for _ in xrange(self.ROWS)]

    def __str__(self):
        """
        :return: a string describing the current board
        :rtype: str
        """
        return '\n'.join(' '.join(row) for row in self.__rows)

    def is_full(self):
        """
        :return: whether the board is full.
        :rtype: bool
        """
        return all(self.EMPTY not in row for row in self.__rows)

    def move(self, column, player):
        """
        Make one move in the game and return whether player won the game.

        :param column: column the player inputted
        :type column: int
        :param player: current player
        :type player: str
        :return: whether player won the game
        :rtype: bool
        """
        row = self.__insert(column, player)
        return self.__is_winner(row, column, player)

    def __insert(self, column, player):
        """
        Insert a player's token into the board.

        :param column: column number the player entered
        :type column: int
        :param player: current player
        :type player: str
        :return: row the token fell into
        :rtype: int
        """
        self.__raise_if_out_of_bounds(column)
        self.__raise_if_column_is_full(column)
        for i, row in reversed(list(enumerate(self.__rows))):
            if row[column] != self.EMPTY:
                continue
            row[column] = player
            return i

    def __is_winner(self, row, column, player):
        """
        :param row: row player inserted his last token into
        :type row: int
        :param column: column player inserted his last token into
        :type column: int
        :param player: current player
        :type player: str
        :return: whether player won the game
        :rtype: bool
        """
        return self.__is_winner_in_row(row, column, player) \
            or self.__is_winner_in_column(row, column, player) \
            or self.__is_winner_in_descending_diagonal(row, column, player) \
            or self.__is_winner_in_ascending_diagonal(row, column, player)

    def __is_winner_in_row(self, row, column, player):
        """
        :param row: row player inserted his last token into
        :type row: int
        :param column: column player inserted his last token into
        :type column: int
        :param player: current player
        :type player: str
        :return: whether player won the game by creating a sequence of four tokens in a row
        :rtype: bool
        """
        return self.__is_winner_in_sequence(self.__rows[row], column, player)

    def __is_winner_in_column(self, row, column, player):
        """
        :param row: row player inserted his last token into
        :type row: int
        :param column: column player inserted his last token into
        :type column: int
        :param player: current player
        :type player: str
        :return: whether player won the game by creating a sequence of four tokens in a column
        :rtype: bool
        """
        return self.__is_winner_in_sequence([r[column] for r in self.__rows], row, player)

    def __is_winner_in_descending_diagonal(self, row, column, player):
        """
        :param row: row player inserted his last token into
        :type row: int
        :param column: column player inserted his last token into
        :type column: int
        :param player: current player
        :type player: str
        :return: whether player won the game by creating a sequence of four tokens in a descending diagonal
        :rtype: bool
        """
        if row >= column:
            difference = row - column
            return self.__is_winner_in_sequence(
                [self.__rows[i][i - difference]
                 for i in xrange(difference, min(self.ROWS, difference + self.COLUMNS))],
                column, player)

        difference = column - row
        return self.__is_winner_in_sequence(
            [self.__rows[i - difference][i] for i in xrange(difference, min(difference + self.ROWS, self.COLUMNS))],
            row, player)

    def __is_winner_in_ascending_diagonal(self, row, column, player):
        """
        :param row: row player inserted his last token into
        :type row: int
        :param column: column player inserted his last token into
        :type column: int
        :param player: current player
        :type player: str
        :return: whether player won the game by creating a sequence of four tokens in a ascending diagonal
        :rtype: bool
        """
        addition = row + column
        if addition < self.ROWS:
            return self.__is_winner_in_sequence([self.__rows[addition - i][i] for i in xrange(addition + 1)], column,
                                                player)
        return self.__is_winner_in_sequence(
            [self.__rows[addition - i][i] for i in xrange(addition - (self.ROWS - 1), min(addition + 1, self.COLUMNS))],
            column - addition + (self.ROWS - 1), player)

    @classmethod
    def __is_winner_in_sequence(cls, sequence, index, player):
        """
        :param sequence: sequence of tokens
        :type sequence: list
        :param index: index of the latest token in the list
        :param player:  current player
        :type player: str
        :return: whether player won the game by creating a sequence of four tokens
        :rtype: bool
        """
        target_slice = [player] * cls.TARGET
        return any(sequence[start:start + cls.TARGET] == target_slice
                   for start in xrange(max(0, index - (cls.TARGET - 1)), index + 1))

    @classmethod
    def __raise_if_out_of_bounds(cls, column):
        """
        Raise a ColumnOutOfBoundsError exception if the inputted column is out of board boundaries.

        :param column: column number inputted
        :type column: int
        :raise: ColumnOutOfBoundsError
        """
        if not 0 <= column < cls.COLUMNS:
            raise ColumnOutOfBoundsError(column)

    def __raise_if_column_is_full(self, column):
        """
        Raise a FullCommonError exception if the inputted column is already full.
        :param column: column number inputted
        :type column: int
        :raise: FullColumnError
        """
        if self.__rows[0][column] != self.EMPTY:
            raise FullColumnError(column)


class ColumnOutOfBoundsError(IndexError):
    """
    Exception for handling columns numbers inputted for columns that are out of board boundaries.
    """

    def __init__(self, column):
        """
        Initialize a ColumnOutOfBoundsError exception.

        :param column: column inputted for checking if it is out of board boundaries
        :type column: int
        """
        super(ColumnOutOfBoundsError, self).__init__()
        self.column = column


class FullColumnError(Exception):
    """
    Exception for handling columns numbers for columns that are already full.
    """

    def __init__(self, column):
        """
       Initialize a FullColumnError exception.

       :param column: column inputted for checking if it is already full
       :type column: int
       """
        super(FullColumnError, self).__init__()
        self.column = column
