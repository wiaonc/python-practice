import matplotlib.pyplot as plt
import pygal
from random_walk15_5 import RandomWalk
from die15_10 import Die
from random import choice
#实列化随机漫步类
rw = RandomWalk(36)
rw.fill_walk()
#实列化骰子类
die=Die()
die1= Die()
#使用柱状表绘制图形
hist = pygal.Bar()
hist.title='x and y'
hist.add('x',rw.x_values)
hist.add('y',rw.y_values)
hist.x_labels=[x+1 for x in range(int(rw.num_points))]
hist.render_to_file('die_visual.svg')

#使用 matplotlib 通过可视化来模拟掷骰子
x=[0]
y=[0]
for xz in range(35):
	zx=x[-1]+die.roll()
	x.append(zx)
for xz in range(35):
	zx=y[-1]+die1.roll()
	y.append(zx)
results=[die.roll()*die1.roll() for roll_num in range(1000)]
frequencies=[results.count(value) for value in range(1, die.num_sides*die1.num_sides+1)]
results1=[die.roll()*die1.roll() for roll_num in range(1000)]
frequencies1=[results1.count(value) for value in range(1, die.num_sides*die1.num_sides+1)]
plt.figure(dpi=128,figsize=(10, 6))
plt.plot(rw.y_values,c='red',linewidth=2)
plt.scatter(y,rw.y_values, c=y, cmap=plt.cm.Reds, edgecolor='none', s=20)
plt.show()

