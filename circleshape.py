import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # declare containers here so static analyzers know this attribute exists
  

    def __init__(self, x, y, radius):
        # we will be using this later
        if getattr(self, "containers", None) is not None:
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass