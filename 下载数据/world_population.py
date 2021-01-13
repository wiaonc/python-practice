import json
from country_codes16_5 import get_country_code
import pygal.maps.world
from pygal.style import  LightColorizedStyle as LCS, RotateStyle as RS
from pygal_maps_world.i18n import COUNTRIES
# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)
# 创建一个包含人口数量的字典
cc_populations = {}
# 根据人口数量将所有的国家分成三组
cc_pops1,cc_pops2,cc_pops3={},{},{}
co = []
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code=get_country_code(country_name)
		if code:
			co.append(code)
			if population < 10000000:
				cc_pops1[code] = population
			elif population < 1000000000:
				cc_pops2[code] = population
			else:
				cc_pops3[code] = population
			#cc_populations[code] = population
		else:
			#print(country_name + ": " + str(population))
			print('ERROR - ' + country_name)
print(len(cc_pops1),len(cc_pops2),len(cc_pops3))
print(co)
coco=[]
for y,x in COUNTRIES.items() :
	coco.append(y)
z=set(co)^set(coco)
print(z)



wm_style = RS('#996633', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)
wm.render_to_file('world_population.svg')