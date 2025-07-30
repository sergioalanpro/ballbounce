import math
import pygame
import random
import sys

#Inicializa Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))#Crear la ventana
pygame.display.set_caption("a ver que pedo")

#Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Limpia la pantalla
    screen.fill((53, 53, 88))
    
    #Actualiza el display
    pygame.display.flip()

    #Fps
    pygame.time.Clock().tick(60)