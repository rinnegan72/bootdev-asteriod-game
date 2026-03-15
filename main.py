import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version:{VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        player.update(dt)
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # print(dt)


if __name__ == "__main__":
    main()
