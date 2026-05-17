#This file creates classes and instances to store the data from CityPop.csv

import math
import numpy as np
import matplotlib.pyplot as plt



class City:
    #creating init method that has parameters self,name,lat,long,pop,and header
    def __init__(self,name,lat,long,pop, header):
        #assign variables to parameters using self
        self.name=name
        self.lat = lat
        self.long = long
        self.pop = pop
        self.header = header
        
    #Method created to print the distance between two cities. Parameters are self and othercity
    def printDistance(self,othercity):
        #Assign lat1, lat2, long1, and long2 variables to their appropriate values from the Citypop file. Make sure they are floats
        lat1= float(self.lat)
        long1 = float(self.long)
        lat2 =float(othercity.lat)
        long2 =float(othercity.long)

        #calculate distance between two cities using the distance formula
        distance = math.acos((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2)))
        final = distance * 6300
        #print the final distance
        print(final)

    #Method created to print the population change over two years for one city. Parameters are self, year1, and year2.
    def printPopChange(self,year1,year2):
        #index1 is assigned to the located index of the population for the city in year1 using header from the main method
        index1= self.header.index(year1) -5
        #index2 is assigned to the located index of the population for the city in year2 using header from the main method
        index2= self.header.index(year2) -5
        #difference is assigned to the difference in population between year2 and year1 making sure they are floats
        difference = float(self.pop[index2]) - float(self.pop[index1])
        #print difference
        print(difference)

                                                
#main method
if __name__ == "__main__":
    #read file
    readFileName = "CityPop.csv"
    #open file
    f = open(readFileName,"r")

    #assign header to the header of the file
    header = f.readline().strip().split(",")
    #print(header)
    
    #create a list to store the city instances based on reading the entries in the file
    cities = []
    #loop through the lines in the file
    for line in f:
        #assign record to each record in file
        record = line.strip().split(",")
        #assign city_name to the specific record location of the city name
        city_name = record[4]
        #assign lat to the specific record location of the latitude
        lat = record[1]
        #assign long to the specific record location of the longitude
        long = record[2]
        #assign pop to the specific record location of the populations in indexes 5-13 since populations range from year 1970 to year 2010
        pop = record[5:14] 
        #Store data by creating city_instance vairable and using the City class and its parameters
        city_instance = City(name= city_name, lat = lat, long=long,pop=pop, header = header)
        #append city instances to cities list
        cities.append(city_instance)
        

    #close file
    f.close()
    
    #print out attributes of cities using for loop
    for i in cities:
        print(i.__dict__)

    #Testing printDistance method
    cities[0].printDistance(cities[1])
    #Testing printPopChange method
    cities[0].printPopChange('yr1970','yr2000')

    # Scatter Plot of populations of two different cities from 1970 to 2010
    #x axis is the years of 1970-2010
    x1=[1970,1975,1980,1985,1990,1995,2000,2005,2010]
    #loop through populations of the first city to define numbers for the y axis
    for i in range(len(cities[0].pop)):
        #pull population values and convert them to floats
        cities[0].pop[i] = float(cities[0].pop[i])
    y1 = cities[0].pop
    #print(y1)
    #Do the same thing for the second city below and assign to x2 and y2 to plot seperate points
    #x axis is the years of 1970-2010
    x2=[1970,1975,1980,1985,1990,1995,2000,2005,2010]
    for i in range(len(cities[1].pop)):
        cities[1].pop[i] = float(cities[1].pop[i])
    y2 = cities[1].pop
    #print(y2)
    #plot x1 and y1, color the points red, and make them circular to create a scatter plot. Label these points as "Tokyo"
    plt.plot(x1,y1,'ro',label='Tokyo')
    #plot x2 and y2, color the points blue, and make them circular to create a scatter plot. Label these points as "New Delhi"
    plt.plot(x2,y2,'bo',label='New Delhi')
    #Label the x axis as Year
    plt.xlabel('X-Axis: Year')
    #Label the y axis as Population
    plt.ylabel('Y-Axis: Population')
    #Create a legend in the upper left corner
    plt.legend(loc='upper left')
    #Show the plot
    plt.show()


    
        

        
