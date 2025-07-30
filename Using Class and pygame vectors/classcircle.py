####UNFINISHED BUGGED BAD LOGIC


import math
import pygame
from pygame import Vector2


width = 800
height = 800


pygame.init()
screen = pygame.display.set_mode((width, height))  
clock = pygame.time.Clock()  

class Circle:
    def __init__(self):
        self.position_circle = Vector2(width / 2, height / 2)
        self.color_circle = (255, 255, 255) 
        self.radius_circle = 250  
        self.width_circle = 5

    def draw_circle(self):
        pygame.draw.circle(screen, self.color_circle, (int(self.position_circle.x), int(self.position_circle.y)), self.radius_circle, self.width_circle)

class Ball:
    def __init__(self):
        self.position = Vector2(width / 2, height / 2)  
        self.color = (255, 0, 0)  
        self.gravity = Vector2(0, 1)  
        self.velocity = Vector2(10, -10)  
        self.radius = 20  

    def update(self):
        self.velocity += self.gravity  
        self.position += self.velocity  

    def check_collision(self):
    
        distance = math.sqrt((self.position.x - circle_instance.position_circle.x)**2 + 
                             (self.position.y - circle_instance.position_circle.y)**2)
        
        if distance >= (circle_instance.radius_circle + self.radius):
            normal = (self.position - circle_instance.position_circle).normalize() 
            
            dotproduct = self.velocity.dot(normal) 
            reflection = self.velocity - 2 * dotproduct * normal  
            self.velocity = reflection  

            overlap = (circle_instance.radius_circle + self.radius) - distance
            self.position += normal * overlap  

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)


ball = Ball()  
circle_instance = Circle()  

while True:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            pygame.quit()  
            exit()  
    
    screen.fill((0, 0, 0))  
    ball.update() 
    ball.check_collision()  
    ball.draw() 
    circle_instance.draw_circle()  

    pygame.display.flip()  
    clock.tick(60)  

