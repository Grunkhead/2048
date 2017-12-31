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
        row[block.get_column()] = block

        print(self.board)


        # self.get_empty_cordinates(self.get_board)
        # self.add_block_to_board(block, self.get_board)

        return block

    # def add_block_to_board(block, board):

        # TODO implementation of adding a Block object to the board -
        # using the row and column cordinates in the Block instance.

    # Will fill in the empty spots.
    def get_empty_cordinates(self):

        for row in self.board:
            for column in row:
                if column:
                    column = 0

        return self.board

    
    # Setters
    def set_board(self, board):
        self.board = board

    # Getters
    def get_board(self):
        return self.board

# Test functionality
# board = Board(4)
# print(board.generate_board_layout(4))
