#keys in dict ->immutable
# values->mutable
name_and_ages=[('alice',2),('bob',3),('charlis',4)]
d=dict(name_and_ages)
print(d)

p=dict(a='alfa',b='beta',e='echo')
print(p)
g=dict(d='delta')
p.update(g)
print(p)

g=dict(p)
print(g)

