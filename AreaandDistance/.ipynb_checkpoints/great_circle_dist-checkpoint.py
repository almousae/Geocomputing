# This program calculates distance between any two points on earth

#import math and numpy module
import math
import numpy


#assign latitude or longitude to respective variable, convert to floats, and convert to radians
lat1 = input("Enter the latitude of the first location:")
lat1 = float(lat1)
lat1 = math.radians(lat1)


long1 = input("Enter the longitude of the first location:")
long1 = float(long1)
long1 = math.radians(long1)

lat2 = input("Enter the latitude of the second location:")
lat2 = float(lat2)
lat2 = math.radians(lat2)

long2 = input("Enter the longitude of the second location:")
long2 = float(long2)
long2 = math.radians(long2)


#assign distance formula to distance variable     
distance = math.acos((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2)))
#convert distance to float
distance = float(distance)
#create variable called final that is equal to distance multipled by 6300
final = distance * 6300
#prints final answer
print(final)                                                         


