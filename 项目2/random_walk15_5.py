from random import choice
from random import randint

class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]
        self.get_step()
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1])
            #x_distance = choice([0, 1, 2, 3, 4])
            x_distance = randint(0,8)
            x_step = x_direction# * x_distance

            y_direction = choice([1,-1])
            # y_distance = choice([0, 1, 2, 3, 4])
            y_distance = randint(0,8)
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def fill_walks(self):
        """计算随机漫步包含的所有点(重构后的函数，适用于xy两个点随机漫步的值都一样)"""
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
    def get_step(self):
        direction = choice([1,-1])
        distance = randint(0,4)
        step = direction * distance
        return step


