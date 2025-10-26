import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Set containers for Player class
    Player.containers = (updatable, drawable)
    
    # Instantiate the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update all updatable objects
        updatable.update(dt)
        
        # Fill the screen with black
        screen.fill("black")
        
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        # Flip the display
        pygame.display.flip()
        
        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()