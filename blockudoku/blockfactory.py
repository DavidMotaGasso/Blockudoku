# Generates the blocks with different shapes and orientations
from .block import Block

class BlockFactory:

    # 1x1
    # X
    BLOCK_1 = Block((True), (1,1))

    # 2x1
    # XX
    BLOCK_2A = Block((True, True), (2,1))

    # 1x2
    # X
    # X
    BLOCK_2B = Block(((True), (True)), (1,2))

    # 2x2
    # XX
    # XX
    BLOCK_3 = Block(((True, True), (True, True)), (2,2))

    # 2x2
    # X0
    # XX
    BLOCK_4A = Block(((True, False), (True, True)), (2,2))

    # 2x2
    # XX
    # X0
    BLOCK_4B = Block(((True, True), (True, False)), (2,2))

    # 2x2
    # XX
    # 0X
    BLOCK_4C = Block(((True, True), (False, True)), (2,2))

    # 2x2
    # 0X
    # XX
    BLOCK_4D = Block(((False, True), (True, True)), (2,2))

    BLOCK_COLLECTION = (BLOCK_1, BLOCK_2A, BLOCK_2B, BLOCK_3,
                        BLOCK_4A, BLOCK_4B, BLOCK_4C, BLOCK_4D)