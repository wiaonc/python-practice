import json
with open ('historyscore.json','r') as score:
	datas = json.load(score)
sdts ={}
for x in datas:
	data = []
	print(x)
	#在做数据储存的时候老是没储存进去，后来通过实验才发现不能储存多个相同键
	x['4'] = {'times':'d','scores':'a'}
	dts = x
	print(dts)
	data.append(dts)
with open ('historyscore.json','w') as score:
	#json.dump(data,score)
	pass
