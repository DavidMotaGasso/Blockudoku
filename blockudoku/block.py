import numpy as np

class Block:
    def __init__(self, block_tuple, shape):
        self.block = np.array(block_tuple)
        self.block = self.block.reshape(shape)

    def get_score(self):
        return np.count_nonzero(self.block)
