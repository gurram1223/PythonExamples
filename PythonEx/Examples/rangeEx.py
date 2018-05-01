print(range(5))

print(list(range(5,10)))
print(list(range(10,15)))
print(list(range(5,20,2)))

s=[0,1,2,3,4,5]

print('-'*5*len(s))

for i in range(len(s)):
    print(s[i])
    
print('-'*5*len(s))

for v in s:
    print(v)
print('-'*5*len(s))

t=[21,333,45,543,56,78,98]
for p in enumerate(t):  #enumerate()-> for counters
    print(p)
print('-'*5*len(s))
for i,v in enumerate(t):
    print("i={},v={}".format(i,v))