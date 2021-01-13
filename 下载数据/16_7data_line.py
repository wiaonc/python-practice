import matplotlib.pyplot as plt
from csvdata16_7 import Data
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

plt.plot(d1.times,d1.y,c='blue')
plt.plot(d2.times,d2.y,c='green')
plt.plot(d3.times,d3.y,c='red')
#plt.scatter(x,result, c=x, cmap=plt.cm.Reds, edgecolor='none', s=10)
fig.autofmt_xdate()#让标签斜着显示
plt.legend(['age0-14','age15-64','age65+'])
plt.show()