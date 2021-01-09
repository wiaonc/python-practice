import time
from datetime import datetime
import csv
timez = datetime.strptime('2014-7-1', '%Y-%m-%d')
timeb = time.strftime('%Y-%m-%d %H:%M:%S %W%Y%I',time.localtime(time.time()))
timex=time.localtime(time.time())
with open('sitka_weather_2014.csv') as f:
	reader = csv.reader(f)
	header_row = next(reader)
	highs,times,lows = [],[],[]
	for index, column_header in enumerate(header_row): 
		print(index, column_header)
	for row in reader:
		timezz = datetime.strptime(row[0], '%Y-%m-%d')
		z=row[0]
		times.append(timezz)
		z = str(timezz)

print(timez)