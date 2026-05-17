city = ["Tokyo","New Delhi","Sao Paulo","Mumbai","Mexico City","New York","Shanghai","Kolkata","Buenos Aires", "Los Angeles", "Beijing","Rio de Janeiro"]
population = [23.3,3.53,7.62,5.81,8.77,16.19,6.04,6.93,0,0,8.1,8.38]


#create empty dictionary assigned to cityPop variable
cityPop = {}
#create a four loop that is in the range of the length of the city list (so it is based on the number of values in the city list)
for i in range(len(city)):
    #loop through each value in this list, assign the city name as the key and the population as the value in the dictionary
    cityPop[city[i]] = population[i]
#print the dictionairy
print(cityPop)
    
