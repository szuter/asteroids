import sys
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

   
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)
    
    asteroid_field = AsteroidField()
    
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        
        for obj in asteroids:
            for shot in shots:
                if obj.collision(shot):
                    obj.kill()
                    shot.kill()
                    
            if player.collision(obj):
                print("Game over!")
                sys.exit()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
