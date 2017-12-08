class Block():

    def __init__(self, value):
        
        self.set_value(value)

    def set_value(self, value):
        
        self.value = value

    def set_image(self, imagePath):
        
        self.image = load(imagePath)
        


    

        