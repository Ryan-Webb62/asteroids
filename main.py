import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  asteroids = pygame.sprite.Group()

  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable,drawable)
  AsteroidField.containers = (updatable)

  Player.containers = (updatable, drawable)

  Shot.containers = (shots, updatable, drawable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
  field = AsteroidField()

  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill(("black"))
    
    for sprite in updatable:
      sprite.update(dt)
    
    for sprite in drawable:
      sprite.draw(screen)
    
    for asteroid in asteroids:
      if asteroid.check_collision(player):
        print("Game Over")
        sys.exit()


    pygame.display.flip()
    
    # limit the frame rate to 60 frames per second
    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()