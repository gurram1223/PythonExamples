import emp
import pickle

f=open("emp1.dat","wb")
n=int(input("enter no of employees: "))
for i in range(n):
    eno=int(input("enter empno: "))
    ename=input("enter empno: ")
    e=emp.Employee(eno,ename)
pickle.dump(e,f)
print(e)
f.close()