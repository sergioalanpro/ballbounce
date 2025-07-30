##UNFINISHED

import math
import pygame
from pygame import Vector2
import random


width = 700
height = 700
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Circle:
    def __init__(self):
        self.position_circle = Vector2(width / 2, height / 2) 
        self.color_cirlce = (0, 255, 0) 
        self.radius_circle = 200  
        self.width_circle = 5
    def draw_circle(self):
        pygame.draw.circle(screen, self.color_cirlce, (int(self.position_circle.x), int(self.position_circle.y)), self.radius_circle, self.width_circle)



class Ball:
    def __init__(self):
        self.position = Vector2(width / 2, height / 2)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.gravity = Vector2(0, 0.5)
        self.velocity = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))  
        self.radius = 20

    def update(self):
        self.velocity += self.gravity
        self.position += self.velocity

    def check_colision(self, circle):
        distance = math.sqrt((self.position.x - circle.position_circle.x)**2 + 
                             (self.position.y - circle.position_circle.y)**2)
                    
        if distance >= circle.radius_circle - self.radius:
            self.velocity.x *= -1
            self.velocity.y *= -1
            return True  
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)



balls = [Ball()] 
circle_instance = Circle()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((53, 53, 88))

    new_balls = []  

    for ball in balls:
        ball.update()
        if ball.check_colision(circle_instance):
            new_balls.append(Ball())  
        ball.draw(screen)

    balls.extend(new_balls)  

    circle_instance.draw_circle()

    pygame.display.flip()
    clock.tick(60)

    if len(balls) > 5:
        balls = balls[:5]

