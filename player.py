import pygame
import circleshape
import constants
from shot import Shot

class Player(circleshape.CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (self.radius / 1.5)

        position = pygame.Vector2(self.position.x, self.position.y)
        a = pygame.Vector2(position.x + forward.x * self.radius, position.y + forward.y * self.radius)
        b = pygame.Vector2(position.x - forward.x * self.radius - right.x, position.y - forward.y * self.radius - right.y)
        c = pygame.Vector2(position.x - forward.x * self.radius + right.x, position.y - forward.y * self.radius + right.y)

        return [(a.x, a.y), (b.x, b.y), (c.x, c.y)]
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown = max(0, self.shot_cooldown - dt)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown > 0:
            return

        self.shot_cooldown = constants.PLAYER_SHOOT_COOLDOWN_SECONDS

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * constants.PLAYER_SHOT_SPEED
        shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS, velocity)

