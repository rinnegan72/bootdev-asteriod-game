from asteroid import Asteroid
import asteroidfield
import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroidfield import AsteroidField


def main():
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version:{VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield_instance = AsteroidField()
    while True:
        log_state()
        updatable.update(dt)
        for drawables in drawable:
            drawables.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # print(dt)


if __name__ == "__main__":
    main()
