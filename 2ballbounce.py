import math
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
screen_center = [WIDTH // 2,  HEIGHT // 2]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 ball bounce")


circle_radius = 200
circle_outline_width = 5


GRAVITY = 0.8

ball_radius = 15
ball_outline_width = 5
ball_pos = screen_center.copy()
ball_color = pygame.Color(255, 0, 0)
ball_velocity = [5, -5]
ball_acceleration =  [0, GRAVITY]

ball2_radius = 15
ball2_outline_width = 5
ball2_pos = [screen_center[0] + 5, screen_center[1] + 5]
ball2_color = pygame.Color(0, 255, 255)
ball2_velocity = [5, -5]
ball2_acceleration =  [0, GRAVITY]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ball_velocity[0] += ball_acceleration[0]
    ball_velocity[1] += ball_acceleration[1]
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    ball2_velocity[0] += ball2_acceleration[0]
    ball2_velocity[1] += ball2_acceleration[1]
    ball2_pos[0] += ball2_velocity[0]
    ball2_pos[1] += ball2_velocity[1]

    dx =  ball_pos[0] - screen_center[0]
    dy =  ball_pos[1] - screen_center[1]
    distance = math.sqrt(dx**2 + dy**2)

    dx2 =  ball2_pos[0] - screen_center[0]
    dy2 =  ball2_pos[1] - screen_center[1]
    distance2 = math.sqrt(dx2**2 + dy2**2) 

    if distance >=  circle_radius - ball_radius:
        normal = [dx / distance, dy /  distance]
        dot_product = ball_velocity[0] *  normal[0] + ball_velocity[1] * normal[1]
        reflection = [ball_velocity[0] - 2 *  dot_product * normal[0], ball_velocity[1] - 2 * dot_product * normal[1]]
        ball_velocity = [reflection[0], reflection[1]]
        ball_pos[0] = screen_center[0] + (circle_radius - ball_radius) * normal [0]
        ball_pos[1] = screen_center[1] + (circle_radius - ball_radius) * normal [1]
        circle_radius -= 2 #Disminuye el tamano con cada rebote
        ball_velocity[1] *= 1.03 #Aumenta la velocidad con cada rebote

    if distance2 >=  circle_radius - ball2_radius:
        normal2 = [dx2 / distance2, dy2 /  distance2]
        dot_product2 = ball2_velocity[0] *  normal2[0] + ball2_velocity[1] * normal2[1]
        reflection2 = [ball2_velocity[0] - 2 *  dot_product2 * normal2[0], ball2_velocity[1] - 2 * dot_product2 * normal2[1]]
        ball2_velocity = [reflection2[0], reflection2[1]]
        ball2_pos[0] = screen_center[0] + (circle_radius - ball2_radius) * normal2 [0]
        ball2_pos[1] = screen_center[1] + (circle_radius - ball2_radius) * normal2 [1]
        circle_radius += 2 #Aumenta el tamano con cada rebote
        ball2_velocity[1] *= 1.03 #Aumenta la velocidad con cada rebote

    screen.fill((0, 0, 0))
    
    pygame.draw.circle(screen, (255, 255, 255), (screen_center[0], screen_center[1]), circle_radius, circle_outline_width)
    pygame.draw.circle(screen, ball_color, (ball_pos[0], ball_pos[1]), ball_radius)
    pygame.draw.circle(screen, ball2_color, (ball2_pos[0], ball2_pos[1]), ball2_radius)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

