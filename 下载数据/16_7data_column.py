import matplotlib.pyplot as plt
from csvdata16_7 import Data
import numpy as np
import pylab as mpl
d1= Data('0-14岁的人口（占总人口的百分比）.csv','中国')
d2=Data('15-64岁的人口（占总人口的百分比）.csv','中国')
d3=Data('65岁和65岁以上的人口（占总人口的百分比）.csv','中国')

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

fig = plt.figure(dpi=128, figsize=(10, 6))
# 设置图表标题，并给坐标轴加上标签
plt.title("不同阶段年龄占总人口比", fontsize=18)
plt.xlabel("年份", fontsize=14)
plt.ylabel("占比%", fontsize=14)
bar_width = 0.45

plt.bar(d1.x,d1.y,alpha = 0.8, width = bar_width)
plt.bar(d2.times ,d2.y,alpha = 0.8, width = bar_width)
plt.bar(d3.times,d3.y,alpha = 0.8, width = bar_width)
# 为每个条形图添加数值标签
#for x,y in enumerate(d1.y):
#	plt.text(x, y+1, '%s' %y)

# 设置Y轴的刻度范围
plt.ylim([1, 100])
#让标签斜着显示
fig.autofmt_xdate()
# 显示图例
plt.legend(['age0-14','age15-64','age65+'])
# 显示图形
plt.show()