#define the file to open
filename = 'aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'

#make a dictionary with k,v = year,temperature
wxdata = {'year':[], 'temperature':[]}

#open the file as read only and make a list of all the lines separated
with open(filename, "r") as f:
	alist = f.read().splitlines()
#itterate through all lines and add to the dictionary
for line in alist:
	wxdata['year'].append(int(line.split()[0]))
	wxdata['temperature'].append(float(line.split()[1]))

#make a list of tuples from dictionary ordered (temperature,year)
wxdata_sorted = list(zip(wxdata['temperature'], wxdata['year']))
wxdata_sorted.sort(reverse = True) #sort highest value first
wxdata_sorted = [(k, v) for v, k in wxdata_sorted]	#switch the tuple

#this data is to format the output later it gets the length of the strings
ranking = len("ranking\t")
year = 8
c = len("temperature anomaly (degrees C)\t")
f = len("temperature anomaly (degrees f)")
print("Ranking	Year	Temperature Anomaly (degrees C)	Temperature Anomaly (degrees F)")

#get the first 10 values and print them out nicely
for i in range(10):
	x = float(( wxdata_sorted[i][1] * 9 / 5) + 32)
	print("{0:<{ranking}}{1:<{year}}{2:<{c}}{3:<{f}}".format(i+1, 
wxdata_sorted[i][0], wxdata_sorted[i][1], 
x, ranking = ranking, year = year, c = c, f = f))

