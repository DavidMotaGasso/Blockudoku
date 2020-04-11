import unittest, os, sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import blockudoku as bd

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = bd.Board()

    def test_initialize_empty_board(self):
        self.assertEqual(np.count_nonzero(self.board.board), 0)
        self.assertEqual(self.board.board.shape, (9, 9))

    def test_allow_block(self):
        block = bd.BlockFactory.BLOCK_3
        allow = self.board.allow_block(0, 0, block) # How to enter r and c
        self.assertTrue(allow)

    def test_allow_block_out_of_bounds(self):
        block = bd.BlockFactory.BLOCK_3
        allow = self.board.allow_block(8, 0, block)  # How to enter r and c
        self.assertFalse(allow)

    # Out of bounds (down and right)
    # Overlap test (it should return false becuase there is already a cell)

if __name__ == '__main__':
    unittest.main()
