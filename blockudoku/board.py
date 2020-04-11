import numpy as np

class Board:
    def __init__(self):
        self.board = np.full((9, 9), False)

    def allow_block(self, r, c, block):  # r,c -> row and column of the upper left cell
        # len_r, len_c -> lengths of the row and column that include the block
        # block_state -> True/False distribution of the block

        len_r = block.block.shape[0]
        len_c = block.block.shape[1]
        allow = 1  # To be continued xd It should be improved with a while

        for i in range(len_r):
            for j in range(len_c):
                if block.block.item((i, j)) == True and self.board.item((i + r, j + c)) == True:
                    allow = 0

        #if allow == 1:
          #  for i in len_r:
            #    for j in len_c:
            #        self.board.item((i + r, j + c)) = block.block.item((i, j))

        return allow