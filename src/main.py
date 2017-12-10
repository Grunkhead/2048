import pygame, sys
from classes.board import Board

pygame.init()

headerFont = pygame.font.SysFont(None, 100)
textFont = pygame.font.SysFont(None, 60)
orange = (243,145,55)
blue = (64, 188, 216)

def main():

    print("Starting..")

    running = True

    screen = pygame.display.set_mode((1080, 1080))
    screen.fill((255, 0, 0))

    display_UI(screen)
    board = Board(4)

    while running:
        pygame.display.update()

        display_board(screen, board)

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
    container = pygame.Surface((1080, 810))
    container.fill(orange)
    screen.blit(container, (0, 180))

    rectangle = pygame.Surface((250, 180))
    rectangle.fill(blue)
    board = board.get_board()

    i = 180
    for row in board:
        j = 0
        for block in row:
            screen.blit(rectangle, (15 + j, 15 + i))            
            screen.blit(textFont.render(str(block), True, orange), (15 + j, 15 + i))
            j = j + 265
        i = i + 195


# def display_score(screen, score):



# def display_highscore(screen, score):


# Start the program.
main()