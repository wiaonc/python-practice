import pygame.font

class Button():
	def __init__(self, ai_settings , screen ,stats):
		"""初始化按钮的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		# 设置按钮的尺寸和其他属性
		self.width, self.height = 240, 60
		self.button_color = (66, 44, 33)
		self.text_color = (255, 200, 255)
		self.font = pygame.font.SysFont(None, 32)
		self.font1 = pygame.font.SysFont(None, 52)
		# 按钮的标签只需创建一次
		self.prep_historybg()
		self.prep_play()
		self.prep_history()
		self.prep_reset()
		self.prep_return()
	def prep_historybg(self):
		self.historybg_image = pygame.image.load('images/historybg.png')
		self.historybg_size = pygame.transform.scale(self.historybg_image,(int(self.screen_rect.right / 2.4), int(self.screen_rect.bottom / 1.2)))
		self.historybg_rect = self.historybg_size.get_rect()
		self.historybg_rect.center = self.screen_rect.center
	def prep_play(self):
		"""准备一个开始按钮"""
		self.play_image = pygame.image.load('images/start.png')
		self.play_size = pygame.transform.scale(self.play_image,(int(self.screen_rect.right / 5.5), int(self.screen_rect.bottom / 10)))
		self.play_rect = self.play_size.get_rect()
		self.play_rect.bottom = self.screen_rect.bottom / 2
		self.play_rect.right = self.screen_rect.right / 2 +120
		self.play_msg_image = self.font.render('start', True, self.button_color,None)
		self.play_msg_rect = self.play_msg_image.get_rect()
		self.play_msg_rect.center = self.play_rect.center
	def prep_history(self):#历史高分排名按钮
		""""""
		self.history_image = pygame.image.load('images/ranking.png')
		self.history_size = pygame.transform.scale(self.history_image,(int(self.screen_rect.right / 5.5), int(self.screen_rect.bottom / 10)))
		self.history_rect = self.history_size.get_rect()
		self.history_rect.bottom = self.play_rect.bottom + self.screen_rect.bottom / 10 + 1
		self.history_rect.right = self.play_rect.right
		self.history_msg_image = self.font.render('History high score', True, self.button_color,None)
		self.history_msg_rect = self.history_msg_image.get_rect()
		self.history_msg_rect.center = self.history_rect.center
	def draw_button(self):
		# 绘制一个用图片填充的按钮
		self.screen.blit(self.play_size, self.play_rect)
		self.screen.blit(self.history_size, self.history_rect)
		self.screen.blit(self.play_msg_image, self.play_msg_rect)
		self.screen.blit(self.history_msg_image, self.history_msg_rect)
	def prep_reset(self):
		#绘制一个按钮
		self.reset_image = pygame.image.load('images/reset.png')
		self.reset_size = pygame.transform.scale(self.reset_image,(int(self.screen_rect.right / 7), int(self.screen_rect.bottom / 14)))
		self.reset_rect = self.reset_size.get_rect()
		self.reset_rect.left = self.historybg_rect.left + 10
		self.reset_rect.bottom = self.historybg_rect.bottom - 10
		self.reset_msg_image = self.font1.render('reset', True, (240, 244, 230),None)
		self.reset_msg_rect = self.reset_msg_image.get_rect()
		self.reset_msg_rect.center = self.reset_rect.center
	def prep_return(self):
		self.return_image = pygame.image.load('images/return.png')
		self.return_size = pygame.transform.scale(self.return_image,(int(self.screen_rect.right / 7), int(self.screen_rect.bottom / 14)))
		self.return_rect = self.return_size.get_rect()
		self.return_rect.right = self.historybg_rect.right - 10
		self.return_rect.bottom = self.historybg_rect.bottom - 10
		self.return_msg_image = self.font1.render('return', True, (240, 244, 230),None)
		self.return_msg_rect = self.return_msg_image.get_rect()
		self.return_msg_rect.center = self.return_rect.center
	def draw_score_ranking(self):
		self.screen.blit( self.historybg_size, self.historybg_rect)
		self.screen.blit(self.reset_size,self.reset_rect)
		self.screen.blit(self.return_size,self.return_rect)
		self.screen.blit(self.reset_msg_image, self.reset_msg_rect)
		self.screen.blit(self.return_msg_image, self.return_msg_rect)

