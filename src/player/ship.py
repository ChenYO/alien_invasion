import pygame

class Ship():

	def __init__(self, ai_setting, screen):

		self.ai_setting = ai_setting

		#取得遊戲畫面資料
		self.screen = screen

		#載入太空船圖檔
		self.image = pygame.image.load("../images/ship.bmp")
		#設定圖檔的區塊範圍
		self.rect = self.image.get_rect()
		#設定畫面的區塊範圍
		self.screen_rect = screen.get_rect()

		#設定太空船初始的位置
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#self.rect.centerx = self.screen_rect.centerx
		#self.rect.centery = self.screen_rect.centery


		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		#移動Flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_setting.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_setting.ship_speed_factor

		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.centery -= self.ai_setting.ship_speed_factor

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_setting.ship_speed_factor

		self.rect.centerx = self.centerx
		self.rect.centery = self.centery

	def blitme(self):
		#畫製太空船
		self.screen.blit(self.image, self.rect)