import pickle

class Emp:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
        print("hrllfkewj")
    def display(self):
        print(self.eno,"\t",self.ename,"\t")

with open("emp.dat","wb") as f:
    e=Emp(1,"abc")
    pickle.dump(e,f) #saving object data to the file
    print("pickling completed")

with open("emp.dat","rb") as f:
    obj=pickle.load(f) #reading the object from the file is unpickling
    print("Emp info")
    obj.display()

#e.__init__(2, "nav")