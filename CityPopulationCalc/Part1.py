#This program reads in the content of CityPop.csv and stores
#the data in a container (a dictionary)

import os
#check if the CityPop file exists
os.path.exists('CityPop.csv')


#Demos from lab are  pasted here for reference and dictionary container
#was created in demo1

def demo1(): # Read Method I: For-loop
    #create citypop dictionary (the container)
    citypop = {}
    listt = []
    #open and read file name
    f=open(readFileName,"r")
    header=f.readline().strip().split(",") # skip the first row (field)
    #assign the index for city to its appropriate index in the hdeader
    city_index = header.index('city')
    for line in f:
        record=line.strip().split(",") # get the record (a list of string)
        city = record[city_index]
        #key is city, record is the value in the container
        citypop[city] = record
      
    #print the dictionary/container  
    print(citypop)
           
    f.close()
    print("demo1 finished, container has been printed")
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



#create a main function
if __name__=="__main__":
    print("--- Demo Begins ---")
    # read and write file name
    readFileName = "CityPop.csv"
    #Read demo1 in order to print the dictionary container of the content in
    #CityPop.csv
    demo1()


    #writing file citypop.csv
    writeFileName = "CityPop.csv"


    #Code below is used in later parts
    
    #fields=["id","latitude","longitude","city","label","yr1970","yr1975","yr1980","yr1985","yr1990","yr1995","yr2000","yr2005","yr2010","\n"]
#Transfer returned vairbales from demo1 
    #citypop,header,record = demo1()
    #entercity = input("Please enter a city name:")
    #enteryear= input("Please enter a year:")
    #if entercity in citypop and enteryear in header:
     #   year_index = header.index(enteryear)
      #  foundcity = citypop[entercity][year_index]
       # print(foundcity)
     
        
            
        
        
        
    

