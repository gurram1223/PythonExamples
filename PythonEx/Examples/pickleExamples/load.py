import emp,pickle
f=open("emp1.dat","rb")
print("emp details: ")
while True:
    try:
       obj=pickle.load(f)
       obj.display() 
       print()
    except EOFError:
        print("all employees completed")
        break
f.close()
        

#obj2=pickle.load(f)