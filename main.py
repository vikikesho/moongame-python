from board import Board
from game import Game

import numpy as np

if __name__ == "__main__":
    adjMat = np.array([[0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0],
                    [1, 0, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 1, 0, 0, 0, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0, 1, 0, 1, 0]])

    board = Board(adjMat)

    game = Game(board)

    game.runGame()