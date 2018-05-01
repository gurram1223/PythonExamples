t=("norway",2.345,4)
print(t)
print(len(t),t[2])

#nested tuples
a=((1,2),(2,3),(3,4),(4,5))
print(a[2],"     ",a[2][1])

def minmax(items):
    return min(items),max(items)
print(minmax([23,54,67,89,22,34]))
lower,upper=minmax([23,54,101,89,212,34])
print(lower,upper)

print(tuple("pavan"))#tuple constructor
      