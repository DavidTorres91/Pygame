import pygame, sys
from pygame.locals import *

pygame.init()


ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Figuras Geometricas")


pygame.draw.polygon(ventana,(190,10,170),((140,0),(291,106),(237,277),(56,277),(0,106)))
pygame.draw.circle(ventana,(8,20,210),(80,120),50)
pygame.draw.rect(ventana,(130,70,70),(10,0,100,50))
pygame.draw.polygon(ventana,(90,180,70),((80,90),(50,100),(40,80),(60,135)))

while True:
    for evento in pygame.event.get():

        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
