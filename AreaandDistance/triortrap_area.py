# This program calculates the area of a trapezoid or triangle based on the user's input.


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
    #convert base to float
    base = float(base)
    #convert height to float
    height = float(height)
    #calculate area and assign to variable
    area = 0.5 *base * height
    #print 'the area of the triangle is' and the area
    print('The area of the triangle is:' , area)
  


    
#else if statement for trapezoid
elif calctype == "trapezoid":
    #assign first base variable to the input of the first base by user
    firstbase = input("Enter the length of the first base of the trapezoid:")
    #assign second base variable to the input of the second base by user
    secondbase = input("Enter the length of the second base of the trapezoid:")
    #assignt height variable to input of height by user
    height = input("Enter height of trapezoid:")
    #convert first base to float
    firstbase = float(firstbase)
    #convert second base to float
    secondbase = float(secondbase)
    #convert the height to float
    height = float(height)
    #calculate area and assign to variable
    area = (firstbase+secondbase) * 0.5 * height
    #print 'the area of the trapezoid is' and the area
    print('The area of the trapezoid is:' , area)
  





