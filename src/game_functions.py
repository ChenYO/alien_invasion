import sys
import pygame

#偵測按下的事件
def check_keydown_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True

#偵測放開的事件
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

#偵測事件
def check_events(ship):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ship)					
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)
				

#更新畫面
def update_screen(ai_settings, screen, ship):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	pygame.display.flip()