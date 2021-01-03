import pygame.font
from pygame.sprite import Group
from ship import Ship
import json
import os
import time

class Scoreboard():
	"""显示得分信息的类"""
	def __init__(self, ai_settings, screen, stats,play_button):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		self.play_button = play_button
		# 显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 32)
		self.high_font = pygame.font.SysFont(None, 22)
		#创建一些变量
		self.dts ={}
		self.data_ranking = []
		# 准备包含最高得分和当前得分的图像
		self.prep_ranking()#准备排行图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()#准备飞船生命值
		self.load_file()#读取文档
		self.prep_ranking_data()#准备分数数据

	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		rounded_score = round(self.stats.score, -1)
		score_str =  'score:'+str("{:,}".format(rounded_score))
		self.score_image = self.font.render(score_str, True,
		self.text_color, None)
		# 将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	def show_score(self):#刷新得分
		"""在屏幕上显示飞船和得分"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		# 绘制飞船
		self.ships.draw(self.screen)
	def prep_high_score(self):
		"""将最高得分转换为渲染的图像"""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = 'history high score:'+str("{:,}".format(high_score))
		self.high_score_image = self.font.render(high_score_str, True, 
		self.text_color, None)
		#将最高得分放在屏幕顶部中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
	def prep_level(self):
		"""将等级转换为渲染的图像"""
		self.level_image = self.font.render(str(self.stats.level), True, 
		self.text_color, None)
		# 将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
	def prep_ships(self):
		"""显示还余下多少艘飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def prep_ranking(self):
		self.rankingx = pygame.image.load('images/historyscore.png')#获取图片
		self.ranking = pygame.transform.scale(self.rankingx,(int(self.play_button.historybg_rect.right*0.5),
		int(self.play_button.historybg_rect.bottom*0.06)))#更改图片像素，
		self.ranking_rect = self.ranking.get_rect()
		self.ranking_rect.right = self.play_button.historybg_rect.right * 0.97
		self.ranking_bottom = self.play_button.historybg_rect.bottom*0.05

	def dump_file(self):#写入数据
#		if not os.path.exists('data'):#检查 该目录没有data文件
#			os.mkdir("data")#创建data文件
		'''这里换成异常检查文件是否存在似乎更好'''
		times = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
		history = [{'times':times,'scores':self.stats.high_score}]
		hsty = {'times':times,'scores':self.stats.high_score}
		self.data = []
		for d in self.datas:
			#下面这段代码块在for循环中修改字典耗费了我好多时间才写出来。
			#原因就是还不太了解字典的属性，以及对逻辑不熟悉
			#下面这句还不知道怎么使用，但是如果用起来肯定是更简洁的
			#dx={k:v for k,v in d.items() if int(k)==self.stats.high_score}
			#self.ds={x:y for x,y in d.items()}
			#循环遍历字典
			for key,value in d.items():
				self.d ={}
				if int(key) == int(self.stats.high_score):
					#如果遍历的键和本局分数相同则值再添加一个值（这里的值是列表状态，所以不会影响字典大小）
					value.append(hsty)
					#再通过修改键值的方式传递给self。dts（应该是只要不添加新键值就没问题）
					d[key] = value
					self.dts = d
					break
				elif int(key) != int(self.stats.high_score):
					#如果键不同就传递原来的键值给self。dts，并且新的属性赋值一个新字典
					self.dts = d
					self.d=history
			if not d.keys():
				#如果字典是空的就赋值（这项目的是为了防止刚创建文本的时候字典没有数据会导致错误）
				d[self.stats.high_score] = history
				self.dts = d
			elif self.d:
				#如果self。d有值就添加到self。dts字典里（字典d没有新纪录的键就会导致self。d有个新字典值）
				self.dts[self.stats.high_score] =self.d
			break
		self.data.append(self.dts)
		with open ('data\historyscore.json','w') as score:
			json.dump(self.data,score)
	def load_file(self):#读取数据
		try:
			self.datas=[]
			with open ('data\historyscore.json','r') as score:
				self.datas = json.load(score)
		except FileNotFoundError:
			if not os.path.exists('data'):#检查 该目录没有data文件
				os.mkdir("data")
			#写入json文件，由于第一次写入json数据没有文件提供储存，所以下面要重新执行读取验证文件
			self.dump_file()
			#重新读取文件，以便创建好基础json数据
			self.load_file()
		else:
			pass
	def history_score(self):
		self.number = 0
		for data_score in self.data_ranking:
			data_score = ('time:'+str(data_score['times'])+
			'  high:'+str(data_score['scores']))
			#下面这里不清楚为什么要绘制11个分数排行框，如果不这样做那么第十名的分数就会跑最上面去
			self.number += 1
			if self.number == 11:
				self.number=0
			self.ranking_rect.top = self.ranking_bottom
			self.ranking_rect.centery =self.ranking_rect.top + int(self.play_button.historybg_rect.bottom*0.06)*self.number+50
			#将最高得分放在图片中央
			self.high_score_ranking = self.high_font.render(data_score, True, self.text_color, None)
			self.score_ranking_rect = self.high_score_ranking.get_rect()#绘制字体
			self.score_ranking_rect.center = self.ranking_rect.center
			#绘制排行图片 和分数
			self.screen.blit(self.high_score_ranking, self.score_ranking_rect)
			self.screen.blit(self.ranking, self.ranking_rect)
	def prep_ranking_data(self):
		for data_dict in self.datas:
			data_list = sorted(data_dict.items(),key=lambda x:int(x[0]),reverse=True)
			for dl in data_list:
				for data_dt in dl[1:2]:
					for self.data_d in data_dt[:9]:
						if len(self.data_ranking) == 10:
							break
						else:
							self.data_ranking.append(self.data_d)
	def clearly_ranking(self):
		try:
			os.remove('data\historyscore.json')
		except FileNotFoundError:
				print('success')
		else:
			pass