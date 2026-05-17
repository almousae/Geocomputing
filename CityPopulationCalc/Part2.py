
#Part 2

#This program reads in the content of CityPop.csv and stores
#the data in a container (a dictionary), and then asks the user to enter
#a city and a year. #The population of this city for that year is then printed

#check if the CityPop file exists
import os
os.path.exists('CityPop.csv')


#Demos from lab are  pasted here for reference and dictionary container
#was created in demo1

def demo1(): # Read Method I: For-loop
    #create citypop dictionary (the container)
    citypop = {}
    #open and read file name
    f=open(readFileName,"r")
    header=f.readline().strip().split(",") # skip the first row (field)
    #print(header)
    #assign the index for city to its appropriate index in the hdeader
    city_index = header.index('city')
    for line in f:
        record=line.strip().split(",") # get the record (a list of string)
        #print(record[city_index])
        city = record[city_index]
        #key is city, record is the value in the container
        citypop[city] = record
        #citypop[] = 
        #citypop[popultion] = population
        
    print(citypop)
        # store and play with the record here
            #print(citypop)           
    f.close()
    print("demo1 finished")
    #return the dictionary, header, and record for later parts of the lab
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

#Prompt user to enter a city with specific instructions and then prompt them to enter a year
    entercity = input("Please enter a city name (Instead of using spaces between word, use underscores, Example: New Delhi should be written as New_Delhi):")
    enteryear= input("Please enter a year:(Example: year 2000 should be written as yr2000)")
    #Check if the entered city is in the dictionary and year are located in the header
    if entercity in citypop and enteryear in header:
        #assign the year-index to the index of the entered year by the user
        year_index = header.index(enteryear)
        #assign foundcity variable to the index of city and year_index in the dictionary. This will give the population for that city in that year
        foundcity = citypop[entercity][year_index]
        #print the population
        print(foundcity)
    #if the city or year is not found in the header, an error message will be printed instead
    else:
        print("City or year not found in CityPop file")
     

#Code used later in part 3
    #entercity1 = input("Please enter first city name:")
    #entercity2 = input("Please enter second city name:")
    #if entercity1 in citypop and entercity2 in citypop:
     #   lat_index = header.index('latitude')
      #  long_index = header.index('longitude')
       # lat1 = float(citypop[entercity1][lat_index])
        #lat2 = float(citypop[entercity2][lat_index])
        #long1 = float(citypop[entercity1][long_index])
        #long2 = float(citypop[entercity2][long_index])
        #distance = math.acos((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2)))
        #final = distance * 6300
        #print(final)
     
        
            
        
   
