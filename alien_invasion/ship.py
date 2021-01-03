import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		"""初始化飞船并设置其初始位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# 将每艘新飞船放在屏幕底部中央
		self.rect.bottom = self.screen_rect.bottom
		self.rect.centerx = self.screen_rect.centerx
		# 在飞船的属性center中存储小数值
		self.centerx = float(self.rect.centerx)
		#函数float()将值转换为小数
		self.bottom = float(self.rect.bottom)
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	def update(self):
		'''要将游戏元素居中，可设置相应rect对象的属性center、centerx或centery。要让游戏元素
与屏幕边缘对齐，可使用属性top、bottom、left或right；要调整游戏元素的水平或垂直位置，
可使用属性x和y，它们分别是相应矩形左上角的x和y坐标。这些属性让你无需去做游戏开发人员
原本需要手工完成的计算，你经常会用到这些属性。'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.centerx -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.bottom -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < 700:
			self.bottom += self.ai_settings.ship_speed_factor
		# 根据self.center更新rect对象
		self.rect.centerx = self.centerx
		self.rect.bottom = self.bottom
		
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.centerx = self.screen_rect.centerx
		self.bottom = self.screen_rect.bottom
		
