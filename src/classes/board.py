from classes.block import Block # Windows classes.block | Linux block
from random import randint

class Board():
    
    def __init__(self, boardSize):
        self.set_board(self.generate_board_layout(boardSize))


    # Generate the multidimensional board layout with 2 random Block objects in it.
    def generate_board_layout(self, boardSize):
          
            return [[Block]*boardSize for i in range(boardSize)]


    # TODO block generating mechanism.
    def generate_random_block(self):
        
        row    = randint(0, self.boardSize)
        column = randint(0, self.boardSize)

        block = Block(row, column, 2)

        # self.get_empty_cordinates(self.get_board)
        # self.add_block_to_board(block, self.get_board)

        return block

    # def add_block_to_board(block, board):

        # TODO implementation of adding a Block object to the board -
        # using the row and column cordinates in the Block instance.

    # Will fill in the empty spots.
    def get_empty_cordinates(board):

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
        return self.board

# Test functionality
# board = Board(4)
# print(board.generate_board_layout(4))
