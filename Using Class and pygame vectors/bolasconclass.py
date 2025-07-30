import math
import pygame
from pygame import Vector2

width = 700
height = 700
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.position = Vector2(width / 2, height / 2)
        self.color = (255, 0, 0) 
        self.gravity = Vector2(0, 0.1) 
        self.velocity = Vector2(5, -5) 
        self.radius = 20 

    def update(self):
        self.velocity += self.gravity 
        self.position += self.velocity

        if self.position.x - self.radius < 0 or self.position.x + self.radius > width:
            self.velocity.x *= -1  
        if self.position.y - self.radius < 0 or self.position.y + self.radius > height:
            self.velocity.y *= -1  

    def draw(self):
        
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)


ball = Ball()  

while True:  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            pygame.quit()  
            exit()  

    screen.fill((53, 53, 88))  
    ball.update()  
    ball.draw()  

    pygame.display.flip()  
    clock.tick(60)  

