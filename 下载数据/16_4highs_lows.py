import csv
from matplotlib import pyplot as plt
from datetime import datetime
"""%A 星期的名称，如Monday 
%B 月份名，如January 
%m 用数字表示的月份（01~12） %d 用数字表示月份中的一天（01~31） %Y 四位的年份，如2015 
%y 两位的年份，如15 
%H 24小时制的小时数（00~23） %I 12小时制的小时数（01~12） %p am或pm 
%M 分钟数（00~59） %S 秒数（00~61）"""
# 从文件中获取日期、最高气温和最低气温
date=input('please input month(y-m):')
#times,highs,lows = [],[],[]
#times1,highs1,lows1=[],[],[]
def comparison_date(file,file1):
	with open(file) as f:
		print(file)
		reader = csv.reader(f)
		header_row = next(reader)
		print(header_row)
		times,highs,lows = [],[],[]
		for index, column_header in enumerate(header_row): 
			print(index, column_header)
		for row in reader:
			try:
				dates =  datetime.strptime(date,'%Y-%m')
				timess = str(dates)
				timen =datetime.strptime(row[0], "%Y-%m-%d")
				timey = str(timen)
				if timey[0:7] == timess[0:7]:
					timez =row[0]
					high = float(row[10])
					low = float(row[12])
					lows.append(low)
					highs.append(high)
					times.append(timez)
				else:
					print('no result')
			except ValueError:
				print('Value Error')
	with open(file1) as f:
		print(file1)
		reader = csv.reader(f)
		header_row = next(reader)
		print(header_row)
		times1,highs1,lows1 = [],[],[]
		for index, column_header in enumerate(header_row): 
			print(index, column_header)
		for row in reader:
			try:
				dates1 =  datetime.strptime(date,'%Y-%m')
				timess = str(dates1)
				timen =datetime.strptime(row[0], "%Y-%m-%d")
				timey = str(timen)
				if timey[0:7] == timess[0:7]:
					timez =row[0]
					high = float(row[10])
					low = float(row[12])
					lows1.append(low)
					highs1.append(high)
					times1.append(timez)
				else:
					print('no result')
			except ValueError:
				print('Value Error')
	# 根据数据绘制图形
	print(times)
	fig = plt.figure(dpi=128, figsize=(10, 6))
	plt.plot(times,highs, c='red', alpha=0.5)#alpha指定颜色的透明度
	plt.plot( lows, c='blue', alpha=0.5)
	plt.fill_between(times,highs,lows, facecolor='blue', alpha=0.1)
	plt.plot(times1,highs1, c='red', alpha=0.5)#alpha指定颜色的透明度
	plt.plot( lows1, c='blue', alpha=0.5)
	plt.fill_between(times1,highs1,lows1, facecolor='blue', alpha=0.1)
	fig.autofmt_xdate()#让标签斜着显示
	# 设置图形的格式
	plt.show()


comparison_date('sitka_weather_2014.csv','death_valley_2014.csv')
