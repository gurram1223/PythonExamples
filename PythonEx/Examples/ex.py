print("hello")

def met(i,j,k):
    for index in range(i,j,k):        
        print("total: ",index,"hello",index)
  
met(1,10,4) 
print ("This is {0} {1} {2} {3}".format("one", "two", "three", "four")) 
print ("This is {} {} {} {}".format("one", "two", "three", "four"))  

# Keyword arguments are called
# by their keyword name
print("{gfg} is a {0} science portal for {1}"
.format("computer", "geeks", gfg ="GeeksforGeeks"))

# Use the index numbers of the
# values to change the order that
# they appear in the string
print("Every {3} should know the use of {2} {1} programming and {0}"
        .format("programmer", "Open", "Source", "Operating Systems"))