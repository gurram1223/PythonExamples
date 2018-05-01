p=set()#set constructor for empty set
print(p)
print(type(p))

a={2,3,4,5,6,23,45,21,33,444} #set delimited by {}
print(a)
print(type(a))

t=[1,4,2,7,9,9,2]
print(set(t))

for x in {1,3,4,21,34,567}:
    print(x) # sets are iterable but order is orbitrary

k={1,2}
print(k)
k.add(3)# add one element to the set
print(k)
k.update([4,5,6,7])#passing any iterable series
print(k)
#k.remove(14)  rewuires an item in set, otherwise raises KeyError
print(k)
k.discard(4)
print(k)

a=k.copy()
print(a)

m=set(a)
print(m)

blue_eyes={'a','b','c','d','e'}
blond_hair={'a','c','f','g'}
smell_hcn={'b','d'}
taste_ptc={'b','d','e','j'}
o_blood={'a'}
b_blood={'b'}

print(blue_eyes.union(blond_hair))
print(blue_eyes.intersection(blond_hair))
print(blond_hair.difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes))
print(smell_hcn.issubset(blue_eyes))
print(taste_ptc.issuperset(smell_hcn))
print(o_blood.isdisjoint(b_blood))









