import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (player_shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:
            if player.collision(obj):
                sys.exit("Game over!")

        for obj in asteroids:
            for shot in player_shots:
                if shot.collision(obj):
                    shot.kill()
                    obj.kill()
            

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60)) / 1000

if __name__ == "__main__":
    main()
