import pygame
from pygame.sprite import Sprite
from random import randint
from random import choice
import game_functions as gf

class Alien(Sprite):
	"""表示单个外星人的类"""
	def __init__(self,ai_settings,screen):
		"""初始化外星人并设置其起始位置"""
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
        # 加载外星人图像，并设置其rect属性
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()
		# 每个外星人最初都在屏幕左上角附近
		self.rect.x =  randint(50,self.screen_rect.right-50)
		self.rect.bottom = self.rect.top
		
		# 存储外星人的准确位置
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		#储存外星人的X值
		self.move_x = []
	#def blitme(self):
	#	"""在指定位置绘制外星人"""
	#	self.screen.blit(self.image,self.rect)
	def move_aliens(self):
		while 1:
			direction = randint(1,600)
			x = choice([-0.2,0.2])
			if len(self.move_x) >88:
				break
			for xs in range(direction):
				self.move_x.append(x)
	def update(self):
		"""向左或向右移动外星人"""
		'''更新外星人位置'''
		self.move_aliens()
		movex=self.move_x.pop(0)#利用列表索引方式取第一个值，这里如果换成遍历列表取值将会造成错误的结果
		if self.rect.right >= self.screen_rect.right:
			movex *= -1
		elif self.rect.left <= 0:
			movex *= -1
		self.y += 0.4*self.ai_settings.alien_speed_factor
		self.x += movex*self.ai_settings.alien_speed_factor
		self.rect.y = self.y
		self.rect.x = self.x