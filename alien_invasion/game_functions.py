import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, play_button, ship, aliens, 
 bullets,sb):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sb.dump_file()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ai_settings, screen, stats,  ship, aliens, bullets,sb)
		elif event.type == pygame.MOUSEBUTTONDOWN:#检测单击按钮事件
			check_mousebuttondown(ai_settings, screen, stats, play_button,ship,
	aliens, bullets,sb)
def check_mousebuttondown(ai_settings, screen, stats, play_button,ship,
	aliens, bullets,sb):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	check_play_button(ai_settings, screen, stats, play_button,
	ship, aliens, bullets,sb, mouse_x, mouse_y)
	check_history_button(stats, play_button,sb, mouse_x, mouse_y)
	check_reset_button(stats, play_button,sb, mouse_x, mouse_y)
	check_return_button(stats, play_button, mouse_x, mouse_y)
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
def check_keyup_events(event,ai_settings, screen, stats,  ship, aliens, bullets,sb):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
	elif event.key == pygame.K_ESCAPE:
		sb.dump_file()
		sys.exit()
	elif event.key == pygame.K_p:
		start_game(ai_settings, screen, stats,  ship, aliens, bullets,sb)
def start_game(ai_settings, screen, stats,  ship, aliens, bullets,sb):
	# 重置游戏设置
	ai_settings.initialize_dynamic_settings()
	# 隐藏光标
	pygame.mouse.set_visible(False)
	# 重置游戏统计信息
	stats.reset_stats()
	stats.game_active = True
	# 重置记分牌图像
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_ships()
	# 清空外星人列表和子弹列表
	aliens.empty()
	bullets.empty()
	# 创建一群新的外星人，并让飞船居中
	create_alien(ai_settings,screen,aliens,stats)
	ship.center_ship()
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets,sb, mouse_x, mouse_y):
	"""在玩家单击Play按钮时开始新游戏"""
	button_clicked = play_button.play_rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active and not stats.history_button:
		start_game(ai_settings, screen, stats,  ship, aliens, bullets,sb)

def check_history_button(stats, play_button,sb,mouse_x, mouse_y):
	button_clicked = play_button.history_rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		stats.history_button = True
		sb.load_file()
def check_return_button(stats, play_button, mouse_x, mouse_y):
	button_clicked = play_button.return_rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active and stats.history_button:
		stats.history_button = False
def check_reset_button(stats, play_button,sb, mouse_x, mouse_y):
	button_clicked = play_button.reset_rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active and stats.history_button:
		sb.clearly_ranking()
		#sb.load_file()
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""检查是否有外星人到达了屏幕底端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			aliens.remove(alien)
			break
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""更新整群外星人的位置"""
	aliens.update()
	# 检测外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
	# 检查是否有外星人到达屏幕底端
	check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""响应被外星人撞到的飞船"""
	if stats.ships_left > 0:
		# 将ships_left减1
		stats.ships_left -= 1
		# 更新记分牌
		sb.prep_ships()
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)#显示鼠标光标
	# 清空外星人列表和子弹列表
	aliens.empty()
	bullets.empty()
	# 创建一群新的外星人，并将飞船放到屏幕底端中央
	create_alien(ai_settings,screen,aliens,stats)
	ship.center_ship()
	# 暂停
	sleep(0.5)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
 play_button):
	screen.fill(ai_settings.bg_color)#这个方法只接受一个实参：一种颜色
	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#让飞船出现在屏幕
	ship.blitme()
	aliens.draw(screen)
	#alien.blitme()
	# 显示得分
	if stats.history_button:#如果历史按钮活动状态
		play_button.draw_score_ranking()
		sb.history_score()
	sb.show_score()
	# 如果游戏处于非活动状态，就绘制Play按钮
	if not stats.game_active and not stats.history_button:
		play_button.draw_button()
	# 让最近绘制的屏幕可见
	pygame.display.flip() #不断更新屏幕，以显示元素的新位置

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		"""如果还没有到达限制，就发射一颗子弹"""
		# 创建一颗子弹，并将其加入到编组bullets中
		new_bullet = Bullet(ai_settings,screen, ship)
		bullets.add(new_bullet)

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""更新子弹的位置，并删除已消失的子弹"""
	# 更新子弹的位置
	bullets.update()
	# 删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
	aliens, bullets)

def start_new_level(stats,sb,ai_settings,  ship,screen, aliens):
	if stats.beat_alien*ai_settings.speedup_scale+stats.score_alien<=stats.score:
		# 如果到达等级条件，就提高一个等级
		#bullets.empty()
		stats.beat_alien += stats.beat_alien*ai_settings.speedup_scale#增加提高等级条件
		ai_settings.increase_speed()
		# 提高等级
		stats.level += 1
		sb.prep_level()
#		create_fleet(ai_settings,  ship,screen, aliens)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
	aliens, bullets):
	"""响应子弹和外星人的碰撞"""
	# 删除发生碰撞的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	#if collisions:
	for aliens in collisions.values():
		stats.score += ai_settings.alien_points * len(aliens)
		sb.prep_score()
		check_high_score(stats, sb)
	start_new_level(stats,sb,ai_settings,  ship,screen, aliens)

def check_high_score(stats, sb):
	"""检查是否诞生了新的最高得分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

def create_alien(ai_settings,screen,aliens,stats):
	"""创建一个外星人并将其放在当前行"""
	alien = Alien(ai_settings,screen)
	if len(aliens) < 3+int(stats.level/2):
		aliens.add(alien)
