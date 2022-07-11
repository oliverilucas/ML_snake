import pygame, sys, numpy as np, random, math
from pygame.locals import *

pygame.init()

#Parámetros de grilla
blockSize = 10 
MARGIN = 0
height = 30
width = 60

#Parámetros de juego
FPS = 25
fpsClock = pygame.time.Clock()
grid = []
HEAD = ((math.trunc(height/2), math.trunc(width/2)))
BODY = [(HEAD[0], HEAD[1]-1), (HEAD[0], HEAD[1]-2), (HEAD[0], HEAD[1]-3), (HEAD[0], HEAD[1]-4), (HEAD[0], HEAD[1]-5)]
TAIL = ()
FOOD = ()
direction = 'right'
food_status = 1
score = 0

#Colores
WHITE = pygame.Color(255,255,255)
RED = pygame.Color(255,0,0)
BLACK = pygame.Color(0,0,0)
BROWN = pygame.Color(155,102,75)
LIGHT_WHITE = pygame.Color(245,232,255)

def defGrid():
    global grid
    grid = []
    for _ in range (0,height):
        rowlist = []
        for _ in range (0,width):
            rowlist.append(0)
        grid.append(rowlist)
    grid = np.array(grid)

def screen():
    WINDOW_HEIGHT = (blockSize + MARGIN) * height + MARGIN + 25 #alto
    WINDOW_WIDTH = (blockSize + MARGIN) * width + MARGIN #ancho
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    return SCREEN

def drawGrid():
    for row in range(height):
        for column in range(width):
            color = WHITE
            if grid[row][column] == 1:
                color = BROWN
            if grid[row][column] == 2:
                color = RED
            pygame.draw.rect(SCREEN,
                             color,
                             [(MARGIN + blockSize) * column + MARGIN,
                              (MARGIN + blockSize) * row + MARGIN,
                              blockSize,
                              blockSize])

#Escribe a snake dentro del grid
def drawSnake():
    try:
        global grid
        grid[HEAD[0], HEAD[1]] = 1
        for element in BODY:
            grid[element[0]][element[1]] = 1
    except:
        pass

def bodyMove(HEAD, BODY):
    global TAIL
    TAIL = BODY[len(BODY)-1]
    varBODY = []
    varBODY.append(HEAD)
    for element in BODY[0:(len(BODY)-1)]:
        varBODY.append(element)
    return HEAD, varBODY

def food():
    global food_status
    global FOOD
    global score
    if food_status == 1:
        while True:
            FOOD = (random.randint(0, height-1), random.randint(0, width-1))
            if grid[FOOD[0]][FOOD[1]] == 0:
                grid[FOOD[0], FOOD[1]] = 2
                food_status = 0
                break
    else:
        grid[FOOD[0], FOOD[1]] = 2
    if HEAD == FOOD:
        food_status = 1
        BODY.append(TAIL)
        score += 1
        food()

def scoreboard():
    global score
    font = pygame.font.SysFont(None,30)
    img = font.render('Score: {0}'.format(score), True, RED)
    SCREEN.blit(img, (3, ((blockSize + MARGIN) * height + MARGIN)+3))
        
def boundaries():
    for elements in BODY:
        if HEAD == elements:
            quit()
    if HEAD[0] >= height or HEAD[0] < 0 or HEAD[1] >= width or HEAD[1] < 0:
        quit()

def loopMove():
    global HEAD
    global BODY
    HEAD, BODY = bodyMove(HEAD, BODY)
    if direction == 'left':
        HEAD = (HEAD[0], HEAD[1]-1)
    elif direction == 'right':
        HEAD = (HEAD[0], HEAD[1]+1)
    elif direction == 'up':
        HEAD = (HEAD[0]-1, HEAD[1])
    elif direction == 'down':
        HEAD = (HEAD[0]+1, HEAD[1])

def quit():
    pygame.quit()
    sys.exit()

# -------------- Main Program Loop -------------- 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT and not direction == 'right' and not direction == 'left':
                direction = 'left'
            elif event.key ==K_RIGHT and not direction == 'left' and not direction == 'right':
                direction = 'right'
            elif event.key ==K_UP and not direction == 'down' and not direction == 'up':
                direction = 'up'
            elif event.key ==K_DOWN and not direction == 'up' and not direction == 'down':
                direction = 'down'

    defGrid()
    SCREEN = screen()
    SCREEN.fill(BLACK)
    loopMove()
    drawSnake()
    boundaries()
    food()
    scoreboard()
    drawGrid()

    pygame.display.update()
    fpsClock.tick(FPS)
