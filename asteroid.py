import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            self.split_into_new()

    def split_into_new(self):
        random_angle = random.uniform(20, 50)
        velocity_a = self.velocity.rotate(random_angle)
        velocity_b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = velocity_a * 1.2
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = velocity_b * 1.2
