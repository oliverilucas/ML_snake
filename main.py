import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()

#Parámetros de pantalla
WINDOW_HEIGHT = 375 #alto
WINDOW_WIDTH = 225 #ancho
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")
grilla = []

np.zeros((15,9))
#Colores
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)

velocidad = 50

def drawGrid():
    blockSize = 25 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def setGrid():
    for x in range(0, 9):
        for y in range(0,15):
            grilla[x][y] = 0



while True:
    SCREEN.fill(BLACK)
    drawGrid()
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
                pass     
    pygame.display.update()

