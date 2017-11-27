import pygame, sys


def main():

    print("Starting..")

    running = True

    screen = pygame.display.set_mode((450, 400))
    screen.fill((255, 0, 0))
    

    while running:
        pygame.display.update()

        for event in pygame.event.get():
            
            # Enable to kill the application.
            if event.type == pygame.QUIT:
                running = False
        

# Start the program.
main()