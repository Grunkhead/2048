class Block():

    def __init__(self, row, column, value):
        
        self.set_row(row)
        self.set_column(column)
        self.set_value(value)

    # Setters
    def set_row(self, row):
        self.row = row

    def set_column(self, column):
        self.column = column

    def set_value(self, value):
        self.value = value

    def set_image_path(self, imagePath):
        self.image = load(imagePath)

    # Getters
    def get_row():
        return self.row

    def get_column():
        return self.column

    def get_value():
        return self.value        


    

        