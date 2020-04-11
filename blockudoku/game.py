from .board import Board
from .blockfactory import BlockFactory

class Game:

    def __init__(self):
        self.board = Board()
        self.score = 0
        self.current_block = None #TODO assign random block
        self.is_game_over = False

    def put_current_block(self, row, column):
        #TODO
        return None
