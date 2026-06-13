import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...] | None
    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: float

    def __init__(self, x, y, radius):
        # we will be using this later
        containers = getattr(self, "containers", None)
        if containers is not None:
            super().__init__(containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = float(radius)

    def draw(self, screen):
        # must override in subclasses
        raise NotImplementedError("CircleShape.draw must be implemented by subclasses")

    def update(self, dt):
        # must override
        pass
    
    def collides_with(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius