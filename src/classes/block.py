from pygame import load

class Block:

    image  = None
    number = None

    def __init__(self, number):
        self.number = number

    def setImage(self, imagePath):
        self.image = load(imagePath)

    

        