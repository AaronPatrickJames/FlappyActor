import pygame
from settings import *
from random import choice, randint

class BG(pygame.sprite.Sprite):

	def __init__(self,groups, scale_factor):
		#What ever group I create will be created here on init
		super().__init__(groups)

		#background
		bg_image = pygame.image.load("../Graphics/Environment/Background.png").convert()

		full_Height = bg_image.get_height() * scale_factor
		full_Width = bg_image.get_width() * scale_factor

		#duplicate becuase of stutter at end of slide
		full_sized_image = pygame.transform.scale(bg_image,(full_Width,full_Height))

		self.image = pygame.Surface((full_Width * 2,full_Height))
		self.image.blit(full_sized_image,(0,0))
		self.image.blit(full_sized_image,(full_Width,0))
		self.rect = self.image.get_rect(topleft = (0,0))
		self.pos = pygame.math.Vector2(self.rect.topleft)


	def update(self,dt):
		self.pos.x -= 300 * dt
		if self.rect.centerx <= 0:
			self.pos.x = 0
		self.rect.x = round(self.pos.x)

class Ground(pygame.sprite.Sprite):

	def __init__(self,groups, scale_factor):
		#What ever group I create will be created here on init
		super().__init__(groups)

		#background
		ground_surf = pygame.image.load("../Graphics/Environment/ground.png").convert_alpha()
		self.image = pygame.transform.scale(ground_surf,pygame.math.Vector2(ground_surf.get_size()) * scale_factor)
		self.rect = self.image.get_rect(topleft = (0, 0))
		self.pos = pygame.math.Vector2(self.rect.topleft)

	def update(self,dt):
		self.pos.x -= 360 * dt
		if self.rect.centerx <= 0:
			self.pos.x = 0
		self.rect.x = round(self.pos.x)

class Avatar(pygame.sprite.Sprite):

	def __init__(self,groups, scale_factor):
		#What ever group I create will be created here on init
		super().__init__(groups)

		#image
		surf = pygame.image.load("../Graphics/Actor/Bib.png").convert_alpha()
		self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size())* scale_factor)

		#rect
		self.rect = self.image.get_rect(midleft = (WINDOW_WIDTH / 20, WINDOW_HEIGHT / 2))
		self.pos = pygame.math.Vector2(self.rect.topleft)

		#movement
		self.gravity = 1000
		self.direction = 0


	#remember to use a log gravity, not a liniar
	def apply_gravity(self, dt):
		self.direction += self.gravity * dt
		self.pos.y += self.direction * dt
		self.rect.y = round(self.pos.y)


	def jump(self):
		self.direction = -500
		pygame.mixer.Sound("../Sound/Flap.mp3").play()


	def update(self, dt):
			self.apply_gravity(dt)

			
class Obstical(pygame.sprite.Sprite):

	def __init__(self,groups, scale_factor):
		#What ever group I create will be created here on init
		super().__init__(groups)

		orientation = choice(("up", "down"))
		surf = pygame.image.load("../Graphics/Obsticals/Pipe.png").convert_alpha()
		self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
		self.image = pygame.transform.scale(self.image, (100, 600))
		spawnDepth = WINDOW_WIDTH + self.image.get_width()

		if orientation == "up":
			y = WINDOW_HEIGHT + randint(-1,500)
			self.rect = self.image.get_rect(midbottom =(spawnDepth,y))
			
		else:
			y = 0 + randint(-500, 1)
			self.image = pygame.transform.flip(self.image, False ,True)
			self.rect = self.image.get_rect(midtop = (spawnDepth,y))
			

		self.pos = pygame.math.Vector2(self.rect.topleft)

	def update(self, dt):
		self.pos.x -= 400 * dt 
		self.rect.x = round(self.pos.x)
		if self.rect.right <= -100:
			self.kill()


