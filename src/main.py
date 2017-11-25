import pygame

def initConfig():

    size   = width, height = 400, 450
    screen = pygame.display.set_mode(size)


def main():

    print("Starting..")

    initConfig()

    # Loop so screen won't disappear.
    input()

# Start the program.
main()