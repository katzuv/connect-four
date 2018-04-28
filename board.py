class Board(object):
    def __init__(self):
        self.__rows = [[' ' for _ in xrange(7)] for _ in xrange(6)]

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.__rows)

    def is_full(self):
        raise NotImplementedError()

    def move(self, column, player):
        '''
        :return: Whether player won the game after this move.
        '''
        raise NotImplementedError()


class FullColumnError(Exception):
    def __init__(self, column):
        super(FullColumnError, self).__init__('Column {} is full'.format(column))
