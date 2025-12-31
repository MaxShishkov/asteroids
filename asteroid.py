import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, SHAPE_COLOR, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, SHAPE_COLOR, self.position, self.radius, LINE_WIDTH)
    
    def update(self,dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        rotated_vector_one = self.velocity.rotate(new_angle)
        rotated_vector_two = self.velocity.rotate(-new_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        ast1.set_velocity(rotated_vector_one * 1.2)
        ast2.set_velocity(rotated_vector_two * 1.2)