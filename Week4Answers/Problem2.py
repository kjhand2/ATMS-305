import sys
import math

vp = 6.1094 * math.exp((17.625 * float(sys.argv[1])) / (float(sys.argv[1]) 
+ 243.04))

print('The vapor pressure for ', sys.argv[1], 'degrees C: ', vp, 
'hPa.')
