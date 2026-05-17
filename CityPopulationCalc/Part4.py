#Part 4

#This program reads in the content of CityPop.csv and stores
#the data in a container (a dictionary), and then asks the user to enter
#two years. The population difference for each city between these two entered years is then calculated
#the ooutput of each city, its id, and the population difference between the two given years is than outputted into a new csv file

#check if the CityPop file exists

import os
os.path.exists('CityPop.csv')

#Demos from lab are  pasted here for reference and dictionary container
#was created in demo1

def demo1(): # Read Method I: For-loop
    #create citypop dictionary (the container)
    citypop = {}
    listt = []
    #open and read file
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
        
    #print(citypop)
        # store and play with the record here
            #print(citypop)           
    f.close()
    #print("demo1 finished")
    return citypop,header,record

def demo5(): # Write Method I: "write"
    f=open(writeFileName,"w")
    # prepare a string seperated with comma for each line
    string_fields = ",".join(fields)
    string_produce = ",".join(listt)
    #string_record2 = ",".join(record2)
    # write each line
    f.write(string_fields)
    f.write(string_produce)
    #f.write(string_record2)
    f.close()
    print("demo5 finished")\

    #f_write = open('cityNames.csv','w')
    
    #for city in citypop.keys():
     #   city_name = city
      #  write_list = [city,'\n']
       # str_write_list = ','.join(write_list)
       # f_write.write(str_write_list)
    #f_write.close()

if __name__=="__main__":
    import math
    print("--- Demo Begins ---")
    # read and write file name
    readFileName = "CityPop.csv"
    # demos for read (all the same)
    demo1()

#Calls demo1 and its returned variables
    citypop,header,record = demo1()
 

#Prompts user to enter two years
    enteryear1 = input("Please enter first year:")
    enteryear2 = input("Please enter second year:")

#Assign Write file name for new csv file and call it CityPopChg

    writeFileName = "CityPopChg.csv"
    #Open and write the new file
    f1 = open("CityPopChg.csv",'w')
    #Create fields for this file for the header, which will be the id, city, and population change for the two years, then write a new line
    fields=["id","city","population_change","\n"]
    #join the fields
    string_fields = ",".join(fields)
    #write the fields
    f1.write(string_fields)
    #if the entered years are both in the cityPop csv header
    if enteryear1 in header and enteryear2 in header:
        #assign year_index1 to the index of the first entered year
        year_index1 = header.index(enteryear1)
        #assign year_index2 to the index of the second entered year
        year_index2 = header.index(enteryear2)
        #assign id_index to the index of id 
        id_index = header.index("id")
        #assign city_index to the index of city
        city_index = header.index('city')
        #loop through the dictionary
        for i in citypop:
            #pop1 is equal to the index of the city and year for the first year entered
            pop1 = float(citypop[i][year_index1])
            #pop2 is equal to the index of the city and year for the second year entered
            pop2 = float(citypop[i][year_index2])
            #popdiff is the difference between pop1 and pop2
            popdiff = pop1 - pop2
            #create a list of the id, city, and population change with a new line after each city
            listt = [str(citypop[i][id_index]),str(citypop[i][city_index]),str(popdiff),"\n"]
            #join this list for the new written csv file
            string_produce = ",".join(listt)
            #write string_produce
            f1.write(string_produce)
            
            
            #print(listt)
         
        #closef1       
        f1.close()
        print("Finished")
    #Error statement for if the year is not found in the file
    else:
        print("One or more of these years is not found in the CityPop file")
  


