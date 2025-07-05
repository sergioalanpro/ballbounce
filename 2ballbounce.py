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
pygame.display.set_caption("2 ball bounce")

#Circulo parametros
circle_radius = 200
circle_outline_width = 5

#Gravedad
GRAVITY = 0.8

#Bola parametros
ball_radius = 15
ball_outline_width = 5
ball_pos = screen_center.copy()
ball_color = pygame.Color(255, 0, 0)
ball_velocity = [5, -5]
ball_acceleration =  [0, GRAVITY]

#Bola 2 parametros
ball2_radius = 15
ball2_outline_width = 5
ball2_pos = [screen_center[0] + 5, screen_center[1] + 5]
ball2_color = pygame.Color(0, 255, 255)
ball2_velocity = [5, -5]
ball2_acceleration =  [0, GRAVITY]

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

    #Actualizar posicion de la bola 2
    ball2_velocity[0] += ball2_acceleration[0]
    ball2_velocity[1] += ball2_acceleration[1]
    ball2_pos[0] += ball2_velocity[0]
    ball2_pos[1] += ball2_velocity[1]

    #Calcular distancia bola 1
    dx =  ball_pos[0] - screen_center[0] #Diferencia de posicion X2-X1
    dy =  ball_pos[1] - screen_center[1] #Diferencia de posicion  Y2-Y1
    distance = math.sqrt(dx**2 + dy**2) #magnitud del vector o distancia entre 2 puntos

    #Calcular distancia bola 2
    dx2 =  ball2_pos[0] - screen_center[0] #Diferencia de posicion X2-X1
    dy2 =  ball2_pos[1] - screen_center[1] #Diferencia de posicion  Y2-Y1
    distance2 = math.sqrt(dx2**2 + dy2**2) #magnitud del vector o distancia entre 2 puntos

    #Checar colision
    if distance >=  circle_radius - ball_radius:
        #Bola 1 parametros
        normal = [dx / distance, dy /  distance]
        dot_product = ball_velocity[0] *  normal[0] + ball_velocity[1] * normal[1]
        reflection = [ball_velocity[0] - 2 *  dot_product * normal[0], ball_velocity[1] - 2 * dot_product * normal[1]]
        ball_velocity = [reflection[0], reflection[1]]
        ball_pos[0] = screen_center[0] + (circle_radius - ball_radius) * normal [0]
        ball_pos[1] = screen_center[1] + (circle_radius - ball_radius) * normal [1]
        circle_radius -= 2 #Disminuye el tamano con cada rebote
        ball_velocity[1] *= 1.03 #Aumenta la velocidad con cada rebote

    if distance2 >=  circle_radius - ball2_radius:
        #Bola 2 parametros
        normal2 = [dx2 / distance2, dy2 /  distance2]
        dot_product2 = ball2_velocity[0] *  normal2[0] + ball2_velocity[1] * normal2[1]
        reflection2 = [ball2_velocity[0] - 2 *  dot_product2 * normal2[0], ball2_velocity[1] - 2 * dot_product2 * normal2[1]]
        ball2_velocity = [reflection2[0], reflection2[1]]
        ball2_pos[0] = screen_center[0] + (circle_radius - ball2_radius) * normal2 [0]
        ball2_pos[1] = screen_center[1] + (circle_radius - ball2_radius) * normal2 [1]
        circle_radius += 2 #Aumenta el tamano con cada rebote
        ball2_velocity[1] *= 1.03 #Aumenta la velocidad con cada rebote

    

    #Limpia la pantalla
    screen.fill((0, 0, 0))

    #Dibujar circulo
    pygame.draw.circle(screen, (255, 255, 255), (screen_center[0], screen_center[1]), circle_radius, circle_outline_width)
     
    #Dibujar bola
    pygame.draw.circle(screen, ball_color, (ball_pos[0], ball_pos[1]), ball_radius)

    #Dibujar bola 2
    pygame.draw.circle(screen, ball2_color, (ball2_pos[0], ball2_pos[1]), ball2_radius)

    #Actualiza el display
    pygame.display.flip()

    #Fps
    pygame.time.Clock().tick(60)

