import random

import pygame
import circleshape
import constants
from constants import LINE_WIDTH
from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            log_event("asteroid_destroyed")
            self.kill()
            return []

        log_event("asteroid_split")
        self.kill()

        new_radius = self.radius / 2
        angle1 = random.uniform(0, 360)
        angle2 = angle1 + 180

        velocity1 = pygame.Vector2(0, 1).rotate(angle1) * random.randint(40, 100)
        velocity2 = pygame.Vector2(0, 1).rotate(angle2) * random.randint(40, 100)

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2

        return [asteroid1, asteroid2]