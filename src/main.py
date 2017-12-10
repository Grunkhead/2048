import pygame, sys
from classes.board import Board

pygame.init()

headerFont = pygame.font.SysFont(None, 100)
textFont = pygame.font.SysFont(None, 60)
orange = (243,145,55)

def main():

    print("Starting..")

    running = True

    screen = pygame.display.set_mode((1080, 1080))
    screen.fill((255, 0, 0))

    displayUI(screen)
    board = Board(4)

    while running:
        pygame.display.update()

        displayBoard(board)

        for event in pygame.event.get():
            
            # Enable to kill the application.
            if event.type == pygame.QUIT:
                running = False

    sys.exit()


def display_UI(screen):
    title = headerFont.render("2048", True, orange)
    score = textFont.render("Score", True, orange)
    highscore = textFont.render("Highscore", True, orange)
    screen.blit(title, (15, 55))
    screen.blit(score, (465, 55))
    screen.blit(highscore, (800, 55))


def display_board(screen, board):
    container = Surface((1080, 810))
    container.fill(orane)
    screen.blit(container, (180, 0))


# def display_score(screen, score):



# def display_highscore(screen, score):


# Start the program.
main()