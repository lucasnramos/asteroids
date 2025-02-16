import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius)
    
    def update(self, dt):
        self.x += self.velocity * dt
        self.y += self.velocity * dt