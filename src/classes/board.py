class Board:

    def __init__(self, size):
        
        self.generate_board_layout(size)


    def generate_board_layout(self, size):
        
        self.set_board_layout([[new Block]*size for i in range(size)])
        
    
    def set_board_layout(self, boardLayout):
        
        self.boardLayout = boardLayout



        
        


