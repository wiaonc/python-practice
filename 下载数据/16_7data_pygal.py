import pygal
from csvdata16_7 import Data
d1= Data('0-14岁的人口（占总人口的百分比）.csv','中国')
d2=Data('15-64岁的人口（占总人口的百分比）.csv','中国')
d3=Data('65岁和65岁以上的人口（占总人口的百分比）.csv','中国')
pyl=pygal.Bar()
pyl.x_labels=d1.times
pyl.title='不同阶段年龄占总人口比'

pyl.x_title="年份"
pyl.y_title="占比%"

pyl.add('age0-14',d1.y)
pyl.add('age15-64',d2.y)
pyl.add('age65+',d3.y)
# 保存
pyl.render_to_file('16_7data_pygal.svg')
