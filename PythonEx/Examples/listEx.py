from macpath import split
s="show how to index into sequences".split()
print(s)

print(s[4])
print(s[-1])
#s=s[x:]+s[:x]
print(s[3:])
print(s[:3])
print(s[:])

u=s.copy()
print(u)

a=[[1,2],[3,4]]
b=a[:]
print(a is b)
print(a==b)

c=[21,32]
print(c*4)

w="the quick brown fox jumps over the lazy dog".split()
print(w)
i=w.index("fox")
print(i)
print(w[i])
del w[3]
print(w)
print(w.insert(3, "fox"))
print(w)
print(w.count("the"))
print(' '.join(w))
print(22 in [1,2,3,4,5,22])
print(22 not in [23,45,22,21])

m=[1,2,3]
n=[4,5,6]
k=m+n
print(k)
k.extend([7,8,9])
print(k)

g=[1,3,44,22,33,66,34,21]
print(g)
g.reverse()
print(g)
g.sort()#ascending order
print(g)
g.sort(reverse=True)#decending order
print(g)

h=" abcdef pavan is good  boy ".split()
print(h)
h.sort(key=len)
print(h)
print(' '.join(h))


x=[4,9,2,1]
y=sorted(x)#built-in function sorts any ietrable series and returns list
print(y)
print(x)

p=[9,3,1,0]
q=reversed(p)#built-in function reverses any iterable series...returns a reverse iterator
print(q)
print(list(q))
print(p)








