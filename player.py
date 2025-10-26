import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float = PLAYER_RADIUS):
        # Initialize parent with the radius value
        super().__init__(x, y, radius)
        # Use a Vector2 for position so vector arithmetic works correctly
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.rotation: float = 0.0
        self.radius: float = float(radius)

    def triangle(self):
        # forward is a unit vector pointing in the ship's local "up" direction
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # right is perpendicular to forward and scaled by radius
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (self.radius / 1.5)
        a = self.position + (forward * self.radius)
        b = self.position - (forward * self.radius) - right
        c = self.position - (forward * self.radius) + right
        return [a, b, c]

    def draw(self, screen):
        # Convert Vector2 points to (x, y) tuples for pygame.draw.polygon
        points = [(p.x, p.y) for p in self.triangle()]
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)

    def update(self, dt):
        # Placeholder for movement/rotation updates using delta time (dt)
        pass