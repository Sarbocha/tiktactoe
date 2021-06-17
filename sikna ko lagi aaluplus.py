import numpy
import pygame, sys
import numpy as np

pygame.init()
display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Aalu Plus")
Row = 3
Column = 3

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

board = numpy.zeros((Row, Column))
display.fill(Blue)


def draw_lines():
    pygame.draw.line(display, Red, (0, 200), (600, 200), 10)
    pygame.draw.line(display, Red, (0, 400), (600, 400), 10)

    pygame.draw.line(display, Red, (200, 0), (200, 600), 10)
    pygame.draw.line(display, Red, (400, 0), (400, 600), 10)


def aaluplus():
    for row in range(Row):
        for col in range(Column):
            if board[row][col] == 1:
                pygame.draw.circle(display, Green, (int(col * 200 + 100), (row * 200 + 100)), 60, 15)
            elif board[row][col] == 2:
                pygame.draw.line(display, Green, (col * 200 + 55, row * 200 + 200 - 55),
                                 (col * 200 + 200 - 55, row * 200 + 55), 15)
                pygame.draw.line(display, Green, (col * 200 + 55, row * 200 + 55),
                                 (col * 200 + 200 - 55, row * 200 + 200 - 55), 15)


def gamewin(player):
    for col in range(Column):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            drawverticalline()
            return True

    for row in range(Row):
        if board[0][row] == player and board[1][row] == player and board[2][row] == player:
            drawhorizontalline()
            return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        drawascdiagonal()
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        drawdesdiagonal()
        return True

    return False


def drawverticalline(col, player):
    posX = col * 200 + 100
    pygame.draw.line(display, Red, (15, posX), (600 - 15, posX), 15)


def drawhorizontalline(row, player):
    posY = row * 200 + 100
    pygame.draw.line(display, Red, (posY, 15), (posY, 600 - 15), 15)


def drawascdiagonal(player):
    pygame.draw.line(display, Red, (15, 600 - 15), (600 - 15, 15), 15)


def drawdesdiagonal():
    pygame.draw.line(display, Red, (15, 15), (600 - 15, 600 - 15), 15)


def restart():
    display.fill(Blue)
    draw_lines()
    player = 1
    for col in range(Column):
        for row in range(Row):
            board[col][row] = 0


def mark_square(row, col, player):
    board[row][col] = player


def spaceavailable(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def isspaceempty():
    for row in range(Row):
        for col in range(Column):
            if board[row][col] == 0:
                return False
    return True


draw_lines()
player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x = event.pos[0]
            y = event.pos[1]

            clickedrow = int(y // 200)
            clickedcol = int(x // 200)

            if player == 1:
                mark_square(clickedrow, clickedcol, 1)
                gamewin(player)

                if gamewin(player):
                    game_over = True
                player = 2

            elif player == 2:
                mark_square(clickedrow, clickedcol, 2)
                gamewin(player)
                if gamewin(player):
                    game_over = True
                player = 1
            aaluplus()

    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_0:
            restart()
    pygame.display.update()


