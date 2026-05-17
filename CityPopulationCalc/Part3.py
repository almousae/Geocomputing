#Part 3

#This program reads in the content of CityPop.csv and stores
#the data in a container (a dictionary), and then asks the user to enter
#two cities and then calculated the distance between them.

#check if the CityPop file exists


import os
os.path.exists('CityPop.csv')

#Demos from lab are  pasted here for reference and dictionary container
#was created in demo1

def demo1(): # Read Method I: For-loop
    #create citypop dictionary (the container)
    citypop = {}
    #open and read file
    f=open(readFileName,"r")
    header=f.readline().strip().split(",") # skip the first row (field)
    #print(header)
    #assign the index for city to its appropriate index in the hdeader
    city_index = header.index('city')
    for line in f:
        record=line.strip().split(",") # get the record (a list of string)
        #print(record[city_index])
        #key is city, record is the value in the container
        city = record[city_index]
        citypop[city] = record
        #citypop[] = 
        #citypop[popultion] = population
        
    print(citypop)
        # store and play with the record here
            #print(citypop)           
    f.close()
    print("demo1 finished")
    return citypop,header,record

def demo5(): # Write Method I: "write"
    f=open(writeFileName,"w")
    # prepare a string seperated with comma for each line    string_fields = ",".join(fields)    string_record1 = ",".join(record1)
    string_record2 = ",".join(record2)
    # write each line
    f.write(string_fields)
    f.write(string_record1)
    f.write(string_record2)
    f.close()
    print("demo5 finished")

if __name__=="__main__":
    import math
    print("--- Demo Begins ---")
    # read and write file name
    readFileName = "CityPop.csv"
    # demos for read (all the same)
    demo1()
    writeFileName = "CityPop.csv"
    fields=["id","latitude","longitude","city","label","yr1970","yr1975","yr1980","yr1985","yr1990","yr1995","yr2000","yr2005","yr2010","\n"]

#Calls demo1 and its returned variables
    citypop,header,record = demo1()

#Prompts user to enter a city with specific instructions and then prompt them to enter a year
    entercity1 = input("Please enter first city name(Instead of using spaces between word, use underscores, Example: New Delhi should be written as New_Delhi):")
    entercity2 = input("Please enter second city name:(Instead of using spaces between word, use underscores, Example: New Delhi should be written as New_Delhi")
    #Check if both cities are located in the dictionary
    if entercity1 in citypop and entercity2 in citypop:
        #assign lat_index to the index of latitude in the header
        lat_index = header.index('latitude')
        #assign long_index to the index of the longitude in the header
        long_index = header.index('longitude')
        #lat1 variable is assigned to the lat index of the first city
        lat1 = float(citypop[entercity1][lat_index])
        #lat2 index is the index of the latitude for the second city
        lat2 = float(citypop[entercity2][lat_index])
        #long1 is the index of the longitude for the first city
        long1 = float(citypop[entercity1][long_index])
        #long2 is the index of the longitude for the second city
        long2 = float(citypop[entercity2][long_index])
        #calculare the distance between the two cities using distance formula
        distance = math.acos((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2)))
        final = distance * 6300
        #print final distance between two entered cities
        print(final)
    #if the cities are not found in the dictionary, print an error message
    else:
        print("one of more of these cities is not found in the CityPop file")
     
        
            
        
    #Code below is used in later parts of the lab
        
    

#for i in range(len(city)):
    #loop through each value in this list, assign the city name as the key and the population as the value in the dictionary
 #   cityPop[city[i]] = population[i]
#print the dictionairy
#print(cityPop)
    

#"id","latitude","longitude","city","label","yr1970","yr1975","yr1980","yr1985","yr1990","yr1995","yr2000","yr2005","yr2010",
