# This program uses a function to convert an input latitude and longitude value in degrees, minutes, and seconds.

#import math and numpy module
import math
import numpy

#create function for converting from DMS to DD
def converttodd(degrees,minutes,seconds):
    #if degrees are negative, convert minutes an seconds to negative
    if degrees < 0:
        minutes = minutes * -1
        seconds = seconds * -1
        #perform dd calculation and assign to variable dd
        dd = degrees + (minutes/60) + (seconds/3600)
        #return dd variable
        return(dd)
    else:
        #but if dms is positive, keep all other values positive and perform calculation normally
        dd = degrees + (minutes/60) + (seconds/3600)
        #return dd variable
        return(dd)

#create function for converting DD to DMS       
def convertfromdd(decdegrees):
    #if dd input is negative, convert decdegrees to absolute value of decdegrees
    if decdegrees < 0:
        decdegrees = abs(decdegrees)
        #pull integer from decdegrees using math.floor and assign to degrees variable
        degrees = math.floor(decdegrees)
        #create minutes variable, and assign to decegrees subtracted by the integer, multiply by 60
        minutes = (decdegrees-degrees) * 60
        #pull ingeger from minutes calulation using math.floor and assign to minutesfinal variable
        minutesfinal = math.floor(minutes)
        #calculate seconds and assign to seconds variable
        seconds = (minutes-minutesfinal) * 60
        #pull integer of seconds using math.floor and assign to secondsfinal variable
        secondsfinal = math.floor(seconds)
        #return negative degrees, minutes, and seconds
        return(-degrees,minutesfinal,secondsfinal)
    else:
        #if dd input was not negative, perform calculation normally without switching to abs value for degrees. Return all positive values
        degrees = math.floor(decdegrees)
        minutes = (decdegrees-degrees) * 60
        minutesfinal = math.floor(minutes)
        seconds = (minutes-minutesfinal) * 60
        secondsfinal = math.floor(seconds)
        return(degrees,minutesfinal,secondsfinal)

#create main program

if __name__ == "__main__":
    #assign input of values that are either in DMS format or DD format to the enter variable
    enter = input("Please enter a latitude of longitude value in DMS or DD format:")
    #convert to str
    enter = str(enter)
    #if a comma is identified in the string, this needs ot be identified as DMS format
    if "," in enter:
        print("The input value is in DMS form")
        #create a list of the degrees, minutes, and seconds value based on splitting the string each time there is a comma identified,
        #and make sure these are each then converting to floats to make sure they work in the converttodd function.
        mylist = [float(enter.split(",")[0]),float(enter.split(",")[1]),float(enter.split(",")[2])]
        #print(mylist[0],mylist[1],mylist[2])
        #assign calc variable to the converttodd function using the input values from the user in the main program
        calc = converttodd(mylist[0],mylist[1],mylist[2])
        #round to four decmical places
        calc = round(calc,4)
        #print Its DD form is, and then the calc number assigned to the variable based on the input that was entered
        print("Its DD form is",calc)
    #if a comma was not identified in the string, use the convertfromdd function and use the enter variable assigned to the input entered by the user. 
    else:
        enter = float(enter)
        conv = convertfromdd(enter)
        print("Its DMS form is", conv)



        

    
    


    













