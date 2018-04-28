class Board(object):
    def __init__(self):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

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
