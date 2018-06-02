import sys
import pygame
import setting.game_functions as gf
from pygame.sprite import Group
from setting.setting import Setting
from setting.game_stats import GameStats
from player.ship import Ship
from enemy.alien import Alien
from setting.button import Button
from setting.scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings = Setting()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	play_button = Button(ai_settings, screen, "Play")

	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)
	while True:		
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			bullets.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()

