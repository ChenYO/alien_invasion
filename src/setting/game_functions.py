import sys
import pygame
from player.bullet import Bullet

#偵測按下的事件
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()



#發射子彈
def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

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
def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)					
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
				

#更新畫面
def update_screen(ai_settings, screen, ship, alien, bullets):
	screen.fill(ai_settings.bg_color)

	#繪製子彈
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	alien.blitme()
	pygame.display.flip()

#更新子彈畫面
def update_bullets(bullets):
	for bullet in bullets.copy():
		#向右發射
		#if bullet.rect.x >= screen.get_rect().right:
		#刪除子彈，以免浪費記憶體效能
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)