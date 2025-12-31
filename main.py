import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Init groups
    Player.containers = (updatable, drawable)
    
    # Player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)
    
    
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        screen.fill("black")
        
        for shape in drawable:
            shape.draw(screen)
        
                
        pygame.display.flip()
        # end of iteration
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
