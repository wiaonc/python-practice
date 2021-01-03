import matplotlib.pyplot as plt
from random_walk15_5 import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(1000)
    rw.fill_walks()
    # 设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
	#绘制随机点
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolor='none', s=10)
	#绘制线条
    plt.plot(rw.x_values,rw.y_values,linewidth=1)
    # 突出起点和终点
    plt.scatter(rw.x_values[0],rw.y_values[0], c='green', edgecolors='none', s=32)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=32)
    # 隐藏坐标轴
    plt.gca().get_xaxis().set_visible(False) 
    plt.gca().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break