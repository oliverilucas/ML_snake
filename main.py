import pygame, sys, numpy as np
from pygame.locals import *

pygame.init()

#Parámetros de grilla
blockSize = 10 
MARGIN = 1
height = 30 
width = 60

#Parámetros de juego
grid = []
HEAD = (15, 30)
BODY = [(HEAD[0], HEAD[1]-1), (HEAD[0], HEAD[1]-2), (HEAD[0], HEAD[1]-3), (HEAD[0], HEAD[1]-4), (HEAD[0], HEAD[1]-5)]
direction = 'right'

#Colores
WHITE = pygame.Color(255,255,255)
LIGH_WHITE = pygame.Color(239,239,239)
BLACK = pygame.Color(0,0,0)
GREEN = pygame.Color(155,102,75)

def defGrid():
    global grid
    grid = []
    for _ in range (0,height):
        rowlist = []
        for _ in range (0,width):
            rowlist.append(0)
        grid.append(rowlist)
    grid = np.array(grid)

    #Parámetros de pantalla
    WINDOW_HEIGHT = (blockSize + MARGIN) * height + MARGIN #alto
    WINDOW_WIDTH = (blockSize + MARGIN) * width + MARGIN #ancho
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    return SCREEN

def drawGrid():
    for row in range(height):
        for column in range(width):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(SCREEN,
                             color,
                             [(MARGIN + blockSize) * column + MARGIN,
                              (MARGIN + blockSize) * row + MARGIN,
                              blockSize,
                              blockSize])

def drawSnake():
    global grid
    grid[HEAD[0], HEAD[1]] = 1
    for element in BODY:
        grid[element[0]][element[1]] = 1

def naturalMove(HEAD, BODY):
    varBODY = []
    varBODY.append(HEAD)
    for element in BODY[0:(len(BODY)-1)]:
        varBODY.append(element)
    return HEAD, varBODY

   


SCREEN = defGrid()

# -------------- Main Program Loop -------------- 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                direction = 'left'
                HEAD, BODY = naturalMove(HEAD, BODY)
                HEAD = (HEAD[0], HEAD[1]-1)
            elif event.key ==K_RIGHT:
                direction = 'right'
                HEAD, BODY = naturalMove(HEAD, BODY)
                HEAD = (HEAD[0], HEAD[1]+1)  
            elif event.key ==K_UP:
                direction = 'up'
                HEAD, BODY = naturalMove(HEAD, BODY)
                HEAD = (HEAD[0]-1, HEAD[1])
            elif event.key ==K_DOWN:
                direction = 'down'
                HEAD, BODY = naturalMove(HEAD, BODY)
                HEAD = (HEAD[0]+1, HEAD[1])
    
    SCREEN.fill(BLACK)
    defGrid()
    drawSnake()
    drawGrid()

    pygame.display.update()
