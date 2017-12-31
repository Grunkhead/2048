from classes.block import Block
from random import randint

class Board():
    
    def __init__(self, boardSize):

        # Minus 1 because of counting from zero.
        self.boardSize = boardSize - 1

        self.set_board(self.generate_board_layout(boardSize))

        # Generate random first pair of random blocks.
        [self.generate_random_block(self.board, self.boardSize) for x in range(2)]


    # Generate the multidimensional board layout with 2 random Block objects in it.
    def generate_board_layout(self, boardSize):
          
            return [[None]*boardSize for i in range(boardSize)]

    def add_numbers_to_eachother(row, slideTowards):

        iterator = len(row) - 1
        nextNum  = 0

        while iterator > 0:
            
            currNum = list[iterator]
            nextNum = list[iterator - 1]
                
            if nextNum == currNum:
                list[iterator] = nextNum + currNum
                del list[iterator - 1]
                list.insert(0, 0)

            iterator -= 1

        return row
        

    # TODO block generating mechanism.
    def generate_random_block(self, board, boardSize):

        # Generate cordinates.        
        row    = randint(0, boardSize)
        column = randint(0, boardSize)

        # Set 2 as default value.
        block = Block(row, column, 2)
        
        row = board[block.get_row()]

        colValue = row[block.get_column()]

        # If spot is empty, spawn generated Block object.
        if colValue == None:
            row[block.get_column()] = block
            return True

        # If not empty, retry combination.
        # TODO this could be more efficient.
        self.generate_random_block(board, boardSize)
        return False

    # def add_block_to_board(block, board):

        # TODO implementation of adding a Block object to the board -
        # using the row and column cordinates in the Block instance.
    
    # Setters
    def set_board(self, board):
        self.board = board

    # Getters
    def get_board(self):
        return self.board
