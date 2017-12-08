from block import Block
from random import randint

class Board():
    
    def __init__(self, boardSize):
        
        self.generate_board_layout(boardSize) 

    # Generate the multidimensional board layout with 2 random Block objects in it.
    def generate_board_layout(self, boardSize):
        
        self.set_board_layout([[

            map(self.generate_random_block(), range(0, 2))
            
            ]*boardSize for i in range(boardSize)])

    # TODO block generating mechanism.
    def generate_random_block(self):
        
        row    = randint(0, self.boardSize)
        column = randint(0, self.boardSize)

        block = Block(row, column, value)

        # TODO implementation.

    # TODO check for empty spots in multidimensional array -
    # so you know where a random block could be placed.
    def spot_is_empty():
        
        # TODO implementation.

        return true

    
    def set_board_layout(self, boardLayout):
        
        self.boardLayout = boardLayout
        


