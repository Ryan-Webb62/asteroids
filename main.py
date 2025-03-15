import pygame
from constants import *

def main():
  print(f"""Starting Asteroids!\n
Screen width: {SCREEN_WIDTH}\n
Screen height: {SCREEN_HEIGHT}\n""")

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill((0, 0, 0))
    pygame.display.flip()



if __name__ == "__main__":
  main()