import math
import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 800
screen_center = [WIDTH // 2, HEIGHT // 2]
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("2 ball collision")

# Parámetros del círculo
circle_radius = 200
circle_outline_width = 5

# Gravedad
GRAVITY = 0.5

# Parámetros de la bola 1
ball_radius = 15
ball_outline_width = 5
ball_pos = screen_center.copy()
ball_color = pygame.Color(255, 0, 0)
ball_velocity = [5, -5]
ball_acceleration = [0, GRAVITY]

# Parámetros de la bola 2
ball2_radius = 15
ball2_outline_width = 5
ball2_pos = [screen_center[0] + 5, screen_center[1] + 5]
ball2_color = pygame.Color(0, 255, 255)
ball2_velocity = [5, -5]
ball2_acceleration = [0, GRAVITY]

# Función de colisión entre las bolas
def check_collision(ball1_pos, ball2_pos, ball1_velocity, ball2_velocity, ball_radius):
    # Calcula la diferencia entre las posiciones de las dos bolas
    dx = ball2_pos[0] - ball1_pos[0]
    dy = ball2_pos[1] - ball1_pos[1]
    distance = math.sqrt(dx**2 + dy**2)

    # Verificar si las bolas están colisionando (distancia menor o igual a la suma de los radios)
    if distance <= 2 * ball_radius:
        # Normalizar el vector de colisión
        normal = [dx / distance, dy / distance]

        # Separar las bolas para evitar solapamiento
        overlap = 2 * ball_radius - distance
        ball1_pos[0] -= normal[0] * overlap / 2
        ball1_pos[1] -= normal[1] * overlap / 2
        ball2_pos[0] += normal[0] * overlap / 2
        ball2_pos[1] += normal[1] * overlap / 2

        # Obtener la velocidad relativa entre las bolas
        relative_velocity = [ball2_velocity[0] - ball1_velocity[0], ball2_velocity[1] - ball1_velocity[1]]
        
        dot_product = relative_velocity[0] * normal[0] + relative_velocity[1] * normal[1]


        # Intercambiar velocidades en la dirección normal
        ball1_velocity[0] += dot_product * normal[0]
        ball1_velocity[1] += dot_product * normal[1]

        ball2_velocity[0] -= dot_product * normal[0]
        ball2_velocity[1] -= dot_product * normal[1]

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar posición de la bola 1
    ball_velocity[0] += ball_acceleration[0]
    ball_velocity[1] += ball_acceleration[1]
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Actualizar posición de la bola 2
    ball2_velocity[0] += ball2_acceleration[0]
    ball2_velocity[1] += ball2_acceleration[1]
    ball2_pos[0] += ball2_velocity[0]
    ball2_pos[1] += ball2_velocity[1]

    # Verificar colisión entre las bolas
    check_collision(ball_pos, ball2_pos, ball_velocity, ball2_velocity, ball_radius)

    # Calcular distancia bola 1
    dx = ball_pos[0] - screen_center[0]  # Diferencia de posición X2-X1
    dy = ball_pos[1] - screen_center[1]  # Diferencia de posición Y2-Y1
    distance = math.sqrt(dx**2 + dy**2)  # Magnitud del vector o distancia entre 2 puntos

    # Calcular distancia bola 2
    dx2 = ball2_pos[0] - screen_center[0]  # Diferencia de posición X2-X1
    dy2 = ball2_pos[1] - screen_center[1]  # Diferencia de posición Y2-Y1
    distance2 = math.sqrt(dx2**2 + dy2**2)  # Magnitud del vector o distancia entre 2 puntos

    # Checar colisión con el círculo
    if distance >= circle_radius - ball_radius:
        normal = [dx / distance, dy / distance]
        dot_product = ball_velocity[0] * normal[0] + ball_velocity[1] * normal[1]
        ball_velocity = [
            ball_velocity[0] - 2 * dot_product * normal[0],
            ball_velocity[1] - 2 * dot_product * normal[1],
        ]
        ball_pos[0] = screen_center[0] + (circle_radius - ball_radius) * normal[0]
        ball_pos[1] = screen_center[1] + (circle_radius - ball_radius) * normal[1]
        #circle_radius -= 2
        #ball_velocity[1] *= 1.02

    if distance2 >= circle_radius - ball2_radius:
        normal2 = [dx2 / distance2, dy2 / distance2]
        dot_product2 = ball2_velocity[0] * normal2[0] + ball2_velocity[1] * normal2[1]
        ball2_velocity = [
            ball2_velocity[0] - 2 * dot_product2 * normal2[0],
            ball2_velocity[1] - 2 * dot_product2 * normal2[1],
        ]
        ball2_pos[0] = screen_center[0] + (circle_radius - ball2_radius) * normal2[0]
        ball2_pos[1] = screen_center[1] + (circle_radius - ball2_radius) * normal2[1]
        #circle_radius += 2
        #ball_velocity[1] *= 1.02

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el círculo
    pygame.draw.circle(screen, (255, 255, 255), (screen_center[0], screen_center[1]), circle_radius, circle_outline_width)

    # Dibujar la bola 1
    pygame.draw.circle(screen, ball_color, (ball_pos[0], ball_pos[1]), ball_radius)

    # Dibujar la bola 2
    pygame.draw.circle(screen, ball2_color, (ball2_pos[0], ball2_pos[1]), ball2_radius)

    # Actualizar el display
    pygame.display.flip()

    # FPS
    pygame.time.Clock().tick(60)

