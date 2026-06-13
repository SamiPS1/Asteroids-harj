import sys

import pygame
from asteroids import Asteroid
from player import Player
from shot import Shot
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
import asteroidfield

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    setattr(Player, "containers", (updatable, drawable))
    setattr(Asteroid, "containers", (asteroids, updatable, drawable))
    setattr(asteroidfield.AsteroidField, "containers", (updatable,))
    setattr(Shot, "containers", (shots, updatable, drawable))
    player = Player(x, y)
    asteroid_field = asteroidfield.AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    if asteroid.radius > ASTEROID_MIN_RADIUS:
                        log_event("asteroid_split")
                    else:
                        log_event("asteroid_destroyed")

                    asteroid.split()
                    shot.kill()
                    break


        for drawable_obj in drawable:
            drawable_obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
        
if __name__ == "__main__":
    main()
    
