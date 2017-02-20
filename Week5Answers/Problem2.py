from fractions import Fraction #for use printing out the fraction
#set filename and variables
filename = 'CMI.csv'
total_readings = 0
highest_temp = 0
temp_time = 0
mean_temp = 0
snowcount = 0

#open the file and make a list of each line
with open(filename, "r") as f:
	alist = f.read().splitlines()
#iterate through each line
for line in alist[1:]:
	cur_line = line.split(',') #split by comma
	total_readings+=1	#add to total number of readings
				#which is just total number of lines

	if (str(cur_line[2]) != 'M'):	#sometimes there is M, we dont count those
		mean_temp += float(cur_line[2])	#add to total temp to be divided later
		if (float(cur_line[2]) > highest_temp):	#check for highest temp
			highest_temp = float(cur_line[2])
			temp_time = cur_line[1]

	obs = cur_line[-1].split()	#split observation by 'space'
	snowcount += obs.count('SN')	#count every SN, -SN, +SN
	snowcount += obs.count('-SN')
	snowcount += obs.count('+SN')

date = temp_time.split()	#split date for easy printing
#print everything to screen
print("1. {0} reports of snow in 2016.".format(snowcount))
print("2. {0} readings reported snow.".format(Fraction(snowcount, total_readings)))
print("3. The highest temperature in 2016 was {0} degrees F \
on {1} at {2}.".format(highest_temp, date[0], date[1]))
print("4. The mean temperature in 2016 was {0} degrees \
F.".format(mean_temp/total_readings))
		
