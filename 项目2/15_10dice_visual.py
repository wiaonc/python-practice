from die15_10 import Die
from random import choice
import pygal
# 创建一个骰子
die = Die()
die1 = Die()
die2 = Die()
# 掷几次骰子，并将结果存储在一个列表中
results = []
new_frequencies = []
#分析结果
frequencies=[]
#for roll_num in range(1000):
#	result = die.roll()
results=[die.roll()*die1.roll() for roll_num in range(1000)]
#for va in range(1, die.num_sides+1):
#	frequency = results.count(va) 
#	frequencies.append(frequency)
frequencies=[results.count(value) for value in range(1, die.num_sides*die1.num_sides+1)]
print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
#[x for x in frequencies]
#[x+2 for x in range(int(die.num_sides+die1.num_sides-1))]
hist.x_labels = [x+1 for x in range(int(die.num_sides*die1.num_sides))]
hist.x_title = 'Result'#[x for x in frequencies]
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
