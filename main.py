import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    # Create sprite groups for updating and drawing game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable, asteroids)
    
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        log_state()
        
         # Handle window close events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        # Clear the screen and draw all drawable sprites
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        player.draw(screen)
        pygame.display.flip()
        
        # Refresh the display and cap the frame rate at 60 FPS
        dt = clock.tick(60) / 1000
        player.update(dt)
        
        
if __name__ == "__main__":
    main()
