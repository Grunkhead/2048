from block import Block
from random import randint

class Board():
    
    def __init__(self, boardSize):
        
        self.generate_board_layout(boardSize)

    # Generate the multidimensional board layout with 2 random Block objects in it.
    def generate_board_layout(self, boardSize):
        
        self.get_board([[

            map(self.generate_random_block(), range(0, 2))
            
            ]*boardSize for i in range(boardSize)])


    # TODO block generating mechanism.
    def generate_random_block(self):
        
        row    = randint(0, self.boardSize)
        column = randint(0, self.boardSize)

        block = Block(row, column, 2)

        self.get_empty_cordinates(self.get_board)
        self.add_block_to_board(block, self.get_board)

        return block

    def add_block_to_board(block, board):

        # TODO implementation of adding a Block object to the board -
        # using the row and column cordinates in the Block instance.

    # Will fill in the empty spots.
    def get_empty_cordinates(board):

        empty_cordinates = def checkBoard(board):

            for row in board:
                for column in row:
                    if not column:
                        column = True

            return board

    
    # Setters
    def set_board(self, board):
        self.board = board

    # Getters
    def get_board(self):
        return self.get_board()

