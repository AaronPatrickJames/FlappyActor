import pygame, sys, time
from settings import *


class Game:
    def __init__(self):

        #Setup Frame
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

    def run(self):
        last_time = time.time()

        #game loop
        while True:

            #Delta Time
            #fixes frame rate differences
            dt = time.time() - last_time
            last_time = time.time()

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(FRAMERATE)



if __name__ == "__main__":
    game = Game()
    game.run()
