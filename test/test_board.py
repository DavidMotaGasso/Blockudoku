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
        block1 = bd.BlockFactory.BLOCK_3
        allow = self.board.allow_block(0, 0, block1) # How to enter r and c
        self.assertTrue(allow)

if __name__ == '__main__':
    unittest.main()
