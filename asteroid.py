import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHAPE_COLOR

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, SHAPE_COLOR, self.position, self.radius, LINE_WIDTH)
    
    def update(self,dt):
        self.position += self.velocity * dt