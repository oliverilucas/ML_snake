import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("Tutorial Cuatro")

#Colores
color_blanco = pygame.Color(255,255,255)
color_negro = pygame.Color(0,0,0)

pygame.draw.circle(ventana, color_negro, (15,15), 10, 5)

imagen = pygame.image.load("img/main.png")
pos_x = 200
pos_y = 200
velocidad = 50

while True:
    ventana.fill(color_blanco)
    ventana.blit(imagen, (pos_x, pos_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                pos_x -= velocidad
            elif event.key ==K_RIGHT:
                pos_x += velocidad
            elif event.key ==K_UP:
                pos_y -= velocidad
            elif event.key ==K_DOWN:
                pos_y += velocidad       

    pygame.display.update()

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)