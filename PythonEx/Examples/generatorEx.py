import calendar

cal = calendar.month(2018, 4)
print("Here is the calendar:")
print(cal)
# A Python program to generate squares from 1
# to 100 using yield and therefore generator
 
# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1;
 
    # An Infinite loop to generate squares 
    while True:
        yield i*i 
        print("hello",i)               
        i += 1  # Next execution resumes 
                # from this point     
 
# Driver code to test above generator 
# function
for num in nextSquare():
    if num > 10:
        break   
    print(num)
