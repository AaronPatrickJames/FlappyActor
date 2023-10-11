import pygame
from settings import *

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

