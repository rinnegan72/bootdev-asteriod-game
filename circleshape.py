import pygame
from constants import LINE_WIDTH


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # must override
        self.position += self.velocity * dt

    def collides_with(self, other):
        center_distance = self.position.distance_to(other.position)
        combined_radius = self.radius + other.radius
        if center_distance < combined_radius:
            return True
        else:
            return False
