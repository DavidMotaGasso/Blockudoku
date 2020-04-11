import unittest, os, sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import blockudoku as bd

class TestBlockFactory(unittest.TestCase):

    def test_block_1(self):
        block = bd.BlockFactory.BLOCK_1
        self.assertEqual(block.block.shape, (1, 1))
        self.assertEqual(block.get_score(), 1)
        self.assertTrue(block.block.item(0, 0))


if __name__ == '__main__':
    unittest.main()
