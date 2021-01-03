class Settings():
	def __init__(self):
		"""初始化游戏的静态设置"""
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (200,210,220)
		# 飞船设置
		self.ship_limit = 3
		# 子弹设置
		self.bullet_width = 6
		self.bullet_height = 15
		self.bullet_color = 60,60,90
		self.bullets_allowed = 12
		# 外星人设置
		self.fleet_drop_speed = 10
		# fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction = 1
		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1
		# 外星人点数的提高速度
		self.score_scale = 1.3
		self.initialize_dynamic_settings()
	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.2
		self.bullet_speed_factor = 1.8
		self.alien_speed_factor = 0.8
		# 记分
		self.alien_points = 5
	def increase_speed(self):
		"""提高速度设置和外星人分数"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
