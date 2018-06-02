import sys
import pygame
from player.bullet import Bullet
from enemy.alien import Alien
from time import sleep

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
	elif event.key == pygame.K_f:
		ai_settings.bullet_width = 600
	elif event.key == pygame.K_g:
		ai_settings.bullet_width = 3
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
def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)					
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
				

#偵測是否按下play按鍵
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	#偵測是否按在按鈕上
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

	if button_clicked and not stats.game_active:
		ai_settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True

		aliens.empty()
		bullets.empty()

		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()


#更新畫面
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
	screen.fill(ai_settings.bg_color)

	#繪製子彈
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen)
	sb.show_score()
	if not stats.game_active:
		play_button.draw_button()

	pygame.display.flip()

#更新子彈畫面
def update_bullets(ai_settings,screen, stats, sb, ship, aliens, bullets):
	for bullet in bullets.copy():
		#向右發射
		#if bullet.rect.x >= screen.get_rect().right:
		#刪除子彈，以免浪費記憶體效能
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
	

#偵測子彈與外星人的碰撞
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()

	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens)

#計算要放幾行艦隊
def get_number_rows(ai_settings, ship_hight, alien_height):
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_hight)
	number_rows = int(available_space_y / (2 * alien_height))

	return number_rows

#計算一行要放幾隻外星人
def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))

	return number_aliens_x

#產生外星人
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	alien.rect.x = alien.x
	aliens.add(alien)

#建立外星人艦隊
def create_fleet(ai_settings, screen, ship, aliens):
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

#偵測外星人是否撞到牆壁
def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break;

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

#更新外星人動作
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
		check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

#偵測太空船撞擊事件
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	if stats.ships_left > 0:
		stats.ships_left -= 1
		aliens.empty()
		bullets.empty()

		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
		break


