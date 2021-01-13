from pygal_maps_world.i18n import COUNTRIES
z=0
for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])
	z +=1
print(z)
