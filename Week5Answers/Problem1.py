filename = 'aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'

wxdata = {'year':[], 'temperature':[]}

with open(filename, "r") as f:
	alist = f.read().splitlines()
for line in alist:
	wxdata['year'].append(int(line.split()[0]))
	wxdata['temperature'].append(float(line.split()[1]))

wxdata_sorted = list(zip(wxdata['temperature'], wxdata['year']))
wxdata_sorted.sort(reverse = True)
wxdata_sorted = [(k, v) for v, k in wxdata_sorted]

ranking = len("ranking\t")
year = 8
c = len("temperature anomaly (degrees C)\t")
f = len("temperature anomaly (degrees f)")
print(year)
print("Ranking	Year	Temperature Anomaly (degrees C)	Temperature Anomaly (degrees F)")

for i in range(10):
	x = float(( wxdata_sorted[i][1] * 9 / 5) + 32)
	print("{0:<{ranking}}{1:<{year}}{2:<{c}}{3:<{f}}".format(i, wxdata_sorted[i][0], wxdata_sorted[i][1], 
x, ranking = ranking, year = year, c = c, f = f))

