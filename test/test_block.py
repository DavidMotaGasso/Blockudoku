import unittest, os, sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import blockudoku as bd

class TestBlock(unittest.TestCase):

    def setUp(self):
        self.block = bd.Block(((True, False), (True, False), (True, True)), (3,2))

    def test_get_score(self):
        self.assertEqual(self.block.get_score(), 4)

    def test_rows(self):
        self.assertEqual(self.block.num_rows(), 3)

    def test_cols(self):
        self.assertEqual(self.block.num_cols(), 2)

if __name__ == '__main__':
    unittest.main()
