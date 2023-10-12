import pygame, sys, time
from settings import *
from Sprites import BG, Ground, Avatar, Obstical

class Game:
    def __init__(self):

        #Setup Frame
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

        #Sprite Groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        #scale factor
        bg_height = pygame.image.load("../Graphics/Environment/Background.png").get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height

        #Sprites
        BG(self.all_sprites, self.scale_factor)
        Ground(self.all_sprites, self.scale_factor)
        NewFactor = self.scale_factor / 15


        self.avatar = Avatar(self.all_sprites, NewFactor)

        

        #timer
        self.obstical_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstical_timer, 1600)
        self.ObsticalFactor = self.scale_factor / 8

    def collisions(self):

        if pygame.sprite.spritecollide(self.avatar,self.collision_sprites,False, pygame.sprite.collide_mask):
            print("Gonna Crash")
            pygame.quit()
            sys.exit()

        if self.avatar.pos.y >= WINDOW_HEIGHT:
            print("You Fell")
            pygame.quit()
            sys.exit()

        if self.avatar.pos.y <= 0:
            print("THE ROOF!")
            pygame.quit()
            sys.exit()


    def run(self):
        pygame.mixer.Sound("../Sound/gamestarted.mp3").play()
        last_time = time.time()
        pygame.mixer.Sound("../Sound/music.mp3").play(-1)

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

                #check for jump on click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.avatar.jump()

                if event.type == self.obstical_timer:
                    Obstical([self.all_sprites, self.collision_sprites], self.ObsticalFactor)


            #Game Locic
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.collisions()
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()
            self.clock.tick(FRAMERATE)



if __name__ == "__main__":
    game = Game()
    game.run()
