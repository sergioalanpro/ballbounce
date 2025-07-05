import math
import pygame
import random
import sys

#Inicializa Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 800
screen_center = [WIDTH // 2,  HEIGHT // 2]
screen = pygame.display.set_mode((WIDTH, HEIGHT))#Crear la ventana
pygame.display.set_caption("Ballbounce")

#Circulo parametros
circle_radius = 200
circle_outline_width = 5
circle_color = pygame.Color(255, 255, 255)

#Gravedad
GRAVITY = 1

#Bola parametros
ball_radius = 15
ball_outline_width = 5
ball_pos = screen_center.copy()
ball_color = pygame.Color(255, 0, 0)
ball_velocity = [10, -10]
ball_acceleration =  [0, GRAVITY]



#Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Actualizar posicion de la bola
    ball_velocity[0] += ball_acceleration[0]
    ball_velocity[1] += ball_acceleration[1]
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    #Calcular distancia
    dx =  ball_pos[0] - screen_center[0] #Diferencia de posicion X2-X1
    dy =   ball_pos[1] - screen_center[1] #Diferencia de posicion  Y2-Y1
    distance = math.sqrt(dx**2 + dy**2) #magnitud del vector o distancia entre 2 puntos

    #Checar colision
    if distance >=  circle_radius - ball_radius:
        normal = [dx / distance, dy /  distance]
        dot_product = ball_velocity[0] *  normal[0] + ball_velocity[1] * normal[1]
        reflection = [ball_velocity[0] - 2 *  dot_product * normal[0], ball_velocity[1] - 2 * dot_product * normal[1]]
        ball_velocity = [reflection[0], reflection[1]]
        ball_pos[0] = screen_center[0] + (circle_radius - ball_radius) * normal [0]
        ball_pos[1] = screen_center[1] + (circle_radius - ball_radius) * normal [1]


    #Limpia la pantalla
    screen.fill((0, 0, 0))
    
    #Dibujar circulo
    pygame.draw.circle(screen, circle_color, (screen_center[0], screen_center[1]), circle_radius, circle_outline_width)

    #Dibujar bola
    pygame.draw.circle(screen, ball_color, (ball_pos[0], ball_pos[1]), ball_radius)
    
    #Actualiza el display
    pygame.display.flip()

    #Fps
    pygame.time.Clock().tick(60)