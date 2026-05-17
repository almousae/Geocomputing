# This program calculates the area of a trapezoid or triangle based on the input of the user, and checks if the user enters number values.


#This assigns calctype to the input entered by the user on whether they would like to calculate the area of a triangle or trapezoid,
#and then prints what they selected
calctype = input("Enter triangle or trapezoid for whichever shape area you wish to calculate:")
print("You would like to calculate the area of a" , calctype)


#if statement for triangle
if calctype == "triangle":
    #assign base variable to input of base by user
    base = input("Enter base of triangle:")
    #assign height variable to input of height by user
    height = input("Enter height of triangle:")
    #try statement to check if variables are numbers:
    try:
        #try to convert base to float
        base = float(base)
        #try to convert height to float
        height = float(height)
        #try to calculate area and assign to variable
        area = 0.5 *base * height
        #print 'the area of the triangle is' and the area
        print('The area of the triangle is:' , area)
        #if the calculation was unsuccessful, an except statement notifies the user that non-numeric numbers were entered.
    except:
        #except stateemnt for if it cannot convert to float
        print("You entered a non-numeric number that could not be converted")
   
  


    
#else if statement for trapezoid
elif calctype == "trapezoid":
    #assign first base variable to the input of the first base by user
    firstbase = input("Enter the length of the first base of the trapezoid:")
    #assign second base variable to the input of the second base by user
    secondbase = input("Enter the length of the second base of the trapezoid:")
    #assignt height variable to input of height by user
    height = input("Enter height of trapezoid:")
    #try statement to check if variables are numbers:
    try:
        #try to convert first base to float
        firstbase = float(firstbase)
        #try to convert second base to float
        secondbase = float(secondbase)
        #try to convert the height to float
        height = float(height)
        #try to calculate area and assign to variable
        area = (firstbase+secondbase) * 0.5 * height
        #print 'the area of the trapezoid is' and the area
        print('The area of the trapezoid is:' , area)
        #if the calculation was unsuccessful, an except statement notifies the user that non-numeric numbers were entered.
    except:
        #except stateemnt for if it cannot convert to float
        print("You entered a non-numeric number that could not be converted")



             


