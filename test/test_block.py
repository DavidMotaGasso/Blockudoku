import unittest, os, sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import blockudoku as bd

class TestBlock(unittest.TestCase):

    def test_get_score(self):
        block1 = bd.Block(((True, False), (True, False), (True, True)))
        self.assertEqual(block1.get_score(), 4)

        block2 = bd.BlockFactory.BLOCK_2B
        self.assertEqual(block2.get_score(),2)


if __name__ == '__main__':
    unittest.main()
