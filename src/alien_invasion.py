import sys
import pygame
from pygame.sprite import Group
from setting.setting import Setting
from player.ship import Ship
from enemy.alien import Alien
import setting.game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Setting()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)
	while True:		
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)		
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

