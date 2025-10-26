import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS,PLAYER_SPEED,PLAYER_TURN_SPEED


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
         pygame.draw.polygon(screen, "white", self.triangle(), 2)
    


    def rotate(self,dt):
        self.rotation +=PLAYER_TURN_SPEED*dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt