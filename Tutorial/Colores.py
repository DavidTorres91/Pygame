import pygame, sys
from pygame.locals import *

pygame.init()


color = (0,140,60)
colorDos = pygame.Color(255,120,9)

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Colores")
   

ventana.fill(color)

while True:

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()