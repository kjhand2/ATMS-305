from fractions import Fraction
filename = 'CMI.csv'
total_readings = 0
snow = 0
highest_temp = 0
temp_time = 0
mean_temp = 0

with open(filename, "r") as f:
	alist = f.read().splitlines()
for line in alist[1:]:
	cur_line = line.split(',')
	total_readings+=1

	if (str(cur_line[2]) != 'M'):
		mean_temp += float(cur_line[2])
		if (float(cur_line[2]) > highest_temp):
			highest_temp = float(cur_line[2])
			temp_time = cur_line[1]

	obs = cur_line[-1].split()

	for x in obs:
		if (x == 'SN') | (x == '-SN') | (x == '+SN'):
			snow+=1
date = temp_time.split()
print("1. {0} reports of snow in 2016.".format(snow))
print("2. {0} readings reported snow.".format(Fraction(snow, total_readings)))
print("3. The highest temperature in 2016 was {0} degrees F \
on {1} at {2}.".format(highest_temp, date[0], date[1]))
print("4. The mean temperature in 2016 was {0} degrees \
F.".format(mean_temp/total_readings))
		
