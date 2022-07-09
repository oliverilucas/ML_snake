from piezas import piezaI, piezaJ, piezaL, piezaO, piezaS, piezaT, piezaZ
import pygame, sys, numpy as np
from pygame.locals import *

pygame.init()

#Parámetros de juego
grid_game = []
blockSize = 30 
MARGIN = 2

#Crea la grilla
for _ in range (0,20):
    rowlist = []
    for _ in range (0,10):
        rowlist.append(0)
    grid_game.append(rowlist)

#Parámetros de pantalla
WINDOW_HEIGHT = (blockSize + MARGIN) * 20 + MARGIN #alto
WINDOW_WIDTH = (blockSize + MARGIN) * 10 + MARGIN #ancho
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

#Colores
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)
GREEN = pygame.Color(155,102,75)

piezaL(grid_game)

#Mueve la pantalla en una fila.
def downGrid():
    grid_game.insert(0, [0] * 10)
    grid_game.pop(20)

def leftGrid():
    grid_game.insert(0, [0] * 10)
    grid_game.pop(20)


def drawGrid():
    for row in range(20):
        for column in range(10):
            color = WHITE
            if grid_game[row][column] == 1:
                color = GREEN
            pygame.draw.rect(SCREEN,
                             color,
                             [(MARGIN + blockSize) * column + MARGIN,
                              (MARGIN + blockSize) * row + MARGIN,
                              blockSize,
                              blockSize])


# -------------- Main Program Loop -------------- 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                pass
            elif event.key ==K_RIGHT:
                pass
            elif event.key ==K_UP:
                pass
            elif event.key ==K_DOWN:
                downGrid()
    
    SCREEN.fill(BLACK)
    drawGrid()

    pygame.display.update()


