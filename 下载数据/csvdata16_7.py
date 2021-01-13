"""创建一个解析csv文件的类，提供文件名和查询的国家参数
返回self.y,self.times值"""
import csv
class Data():
	"""创建一个解析csv文件的类，提供文件名和查询的国家参数
	返回self.y,self.times值"""
	def __init__(self,csvs,country_name):
		code,name=[],[]
		name.append(country_name)
		code.append('Country Code')
		self.y = []
		self.times = []
		with open(csvs,encoding='utf-8') as n:
			data = csv.reader(n)
			z=next(data)
			for row in data:
				if code == row[1:2]:
					for tm in row[4:]:
						self.times.append(tm)
				elif name == row[0:1]:
					for zx in row[4:]:
						if zx !=''and zx !=' ':
							self.y.append(float(zx))
		for x in range(0,len(self.times)-len(self.y)):
			self.times.pop(-1)
		z = 1
		self.x=[]
		for s in self.y:
			self.x.append(z)
			z += 1



