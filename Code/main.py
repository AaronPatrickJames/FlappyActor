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
        self.active = True

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

        #Text
        self.font = pygame.font.Font("../Graphics/Font/Brushed.ttf", 30)
        self.score = 0
        self.start_offset = 0

        #menu
        self.menu_surf = pygame.image.load("../Graphics/UI/menu.png").convert_alpha()
        self.menu_rect = self.menu_surf .get_rect(center = (WINDOW_WIDTH /2, WINDOW_HEIGHT / 2))


    def collisions(self):

        if pygame.sprite.spritecollide(self.avatar,self.collision_sprites,False, pygame.sprite.collide_mask):
            print("Gonna Crash")
            self.active = False
            self.avatar.kill()
            pygame.mixer.Sound("../Sound/shortscreamdead.mp3").play()

        if self.avatar.pos.y >= WINDOW_HEIGHT - 20:
            print("You Fell")
            self.active = False
            self.avatar.kill()
            pygame.mixer.Sound("../Sound/shortscreamdead.mp3").play()

        if self.avatar.pos.y <= -100:
            print("THE ROOF!")
            self.active = False
            self.avatar.kill()
            pygame.mixer.Sound("../Sound/shortscreamdead.mp3").play()


    def display_score(self):
        if self.active: 
            self.score = (pygame.time.get_ticks() - self.start_offset)// 1600
            y = 50
        else:
            y = WINDOW_HEIGHT / 2 + self.menu_rect.height

        score_surf = self.font.render(str(self.score), True, "black" )
        score_rect = score_surf.get_rect(midtop = (WINDOW_WIDTH / 2, y))
        self.display_surface.blit(score_surf, score_rect)

    def run(self):
        pygame.mixer.Sound("../Sound/gamestarted.mp3").play()
        last_time = time.time()
        #pygame.mixer.Sound("../Sound/music.mp3").play(-1)

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
                    if self.active == True:
                        self.avatar.jump()
                    else:
                        self.avatar = Avatar(self.all_sprites, self.scale_factor / 15)
                        self.active = True
                        self.start_offset = pygame.time.get_ticks()
                        pygame.mixer.Sound("../Sound/gamestarted.mp3").play()
                    


                if self.active == True:
                    if event.type == self.obstical_timer:
                        Obstical([self.all_sprites, self.collision_sprites], self.ObsticalFactor)
                else:
                    pass


            #Game Locic
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.display_score()

            if self.active: 
                self.collisions()
            else:
                self.display_surface.blit(self.menu_surf, self.menu_rect)


            pygame.display.update()
            self.clock.tick(FRAMERATE)



if __name__ == "__main__":
    game = Game()
    game.run()
