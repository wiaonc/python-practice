#import sys 
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

'''扩展游戏《外星人入侵》：想想如何扩展游戏《外星人入侵》。例如，可让外
星人也能够向飞船射击，或者添加盾牌，让飞船躲到它后面，使得只有从两边射来的子
弹才能摧毁飞船。另外，还可以使用像 pygame.mixer 这样的模块来添加音效，如爆炸
声和射击声。'''
def run_game(): 
 # 初始化游戏并创建一个屏幕对象
	pygame.init()#初始化背景设置
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")#设置窗口名
	# 创建存储游戏统计信息的实例，并创建记分牌
	stats = GameStats(ai_settings)
	# 创建Play按钮
	play_button = Button(ai_settings, screen,stats)
	# 创建一艘飞船、一个子弹编组和一个外星人编组
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	sb = Scoreboard(ai_settings, screen, stats,play_button)
	# 创建外星人群
	#gf.create_fleet(ai_settings,ship,screen,aliens)
	# 开始游戏主循环
	while True: 
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats, play_button, ship, 
		aliens, bullets,sb)
		if stats.game_active:
			#更新飞船的位置
			ship.update()
			gf.create_alien(ai_settings,screen,aliens,stats)
			#更新所有未消失的子弹的位置
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
			bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, 
			bullets)
		#更新后的位置来绘制新屏幕
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
		bullets, play_button)

run_game()
