import pygame
from constants import *
from circleshape import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen.fill((0,0,0))
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000

if __name__ == "__main__":
    main()

