import pygame, sys, numpy as np, random
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
FOOD = ()
direction = 'right'
food_status = 1

#Colores
WHITE = pygame.Color(255,255,255)
RED = pygame.Color(255,0,0)
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
            if grid[row][column] == 2:
                color = RED
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

def food():
    global food_status
    global FOOD
    if food_status == 1:
        FOOD = (random.randint(0, height-1), random.randint(0, width-1))
        grid[FOOD[0], FOOD[1]] = 2
        food_status = 0
    else:
        grid[FOOD[0], FOOD[1]] = 2



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
    
    SCREEN = defGrid()
    SCREEN.fill(BLACK)
    food()
    drawSnake()
    drawGrid()

    pygame.display.update()
