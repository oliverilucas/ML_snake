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
game_status = 1
score = 0

#Colores
WHITE = pygame.Color(255,255,255)
RED = pygame.Color(255,0,0)
BLACK = pygame.Color(0,0,0)
BROWN = pygame.Color(155,102,75)
LIGHT_WHITE = pygame.Color(245,232,255)


def defGrid():
    global grid
    global game_status
    grid = []
    game_status = 1
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
    SCREEN.fill(BLACK)
    return SCREEN

def drawGrid():
    if game_status == 1:
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

def createSnake():
    if game_status == 1:
        try:
            global grid
            grid[HEAD[0], HEAD[1]] = 1
            for element in BODY:
                grid[element[0]][element[1]] = 1
        except:
            pass

def bodyMove(HEAD, BODY):
    if game_status == 1:
        global TAIL
        TAIL = BODY[len(BODY)-1]
        varBODY = []
        varBODY.append(HEAD)
        for element in BODY[0:(len(BODY)-1)]:
            varBODY.append(element)
        return HEAD, varBODY

def setFood():
    if game_status == 1:
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
            setFood()

def drawScoreboard():
    global score
    font = pygame.font.SysFont(None,30)
    img = font.render('Score: {0}'.format(score), True, RED)
    SCREEN.blit(img, (3, ((blockSize + MARGIN) * height + MARGIN)+3))
        
def isColission():
    if game_status == 1:
        for elements in BODY:
            if HEAD == elements:
                gameOver()

def loopMove():
    if game_status == 1:
        global HEAD
        global BODY
        HEAD, BODY = bodyMove(HEAD, BODY)
        if direction == 'left':
            if HEAD[1] > 0:
                HEAD = (HEAD[0], HEAD[1]-1)
            else:
                gameOver()
        elif direction == 'right':
            if HEAD[1] < width - 1:
                HEAD = (HEAD[0], HEAD[1]+1)
            else:
                gameOver()
        elif direction == 'up':
            if HEAD[0] > 0:
                HEAD = (HEAD[0]-1, HEAD[1])
            else:
                gameOver()
        elif direction == 'down':
            if HEAD[0] < height - 1:
                HEAD = (HEAD[0]+1, HEAD[1])
            else:
                gameOver()

def gameOver():
    global grid
    global HEAD
    global BODY
    global TAIL
    global FOOD
    global direction
    global food_status
    global score
    global game_status
    grid = []
    HEAD = ((math.trunc(height/2), math.trunc(width/2)))
    BODY = [(HEAD[0], HEAD[1]-1), (HEAD[0], HEAD[1]-2), (HEAD[0], HEAD[1]-3), (HEAD[0], HEAD[1]-4), (HEAD[0], HEAD[1]-5)]
    TAIL = ()
    FOOD = ()
    direction = 'right'
    food_status = 1
    score = 0
    game_status = 0


# -------------- Main Program Loop -------------- 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT and not direction == 'right' and not direction == 'left':
                direction = 'left'
            elif event.key ==K_RIGHT and not direction == 'left' and not direction == 'right':
                direction = 'right'
            elif event.key ==K_UP and not direction == 'down' and not direction == 'up':
                direction = 'up'
            elif event.key ==K_DOWN and not direction == 'up' and not direction == 'down':
                direction = 'down'

    #1. Crea la matriz de juego
    defGrid()
    #2. Establece el tamaño y diseño de pantalla.
    SCREEN = screen()
    #3. Bucle de movimiento: mueve a snake.
    loopMove()
    #4. Crea a Snake
    createSnake()
    #5. Detecta si snake colisiona consigo mismo o con una pared.
    isColission()
    #6. Pone la comida en el mapa
    setFood()
    #7. Dibuja el Scoreboard
    drawScoreboard()
    #8. Dibuja la pantalla
    drawGrid()

    pygame.display.update()
    fpsClock.tick(FPS)
