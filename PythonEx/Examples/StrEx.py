c='pavan'   #strings are immutable
print(c.capitalize()) #Pavan
print(c)    #pavan
d=b'some bytes'
print(d.split())    #[b'some', b'bytes']
#List
b=['apple','orange','banana']
print(b[1]) #orange
b[1]=7
print(b[1])#7
a=[] 
a.append(2)
a.append('naveen')
print(a)#[2]
#list constructor
print(list("charecter"))#['c', 'h', 'a', 'r', 'e', 'c', 't', 'e', 'r']
#dictionaries
e={'alice':'1','bob':2,'eve':'234-3445-567'}
print(e['eve'])#234-3445-567
e['mor']='pavan'
print(e)#{'alice': '1', 'bob': 2, 'eve': '234-3445-567', 'mor': 'pavan'}
#for loop
cities=["lonon","khammam","paris"]
for city in cities:
    print(city)#lonon khammam paris

colors={'crimson':0xdc143c,'corol':0xff7f50}
for color in colors:
    print(color,colors[color])#crimson 14423100 corol 16744272
    
print("news"+"paper")

colors=';'.join(["red","blue","green"])
print(colors)
print(colors.split(';'))

print("pavankumargurram".partition("kumar"))

departure,seperator,arrival="London:Edinburg".partition(':')
print(departure,arrival,seperator)

origin,_,destination="seattle-bostin".partition('-')
print(origin,destination,_)

print("the age of {0} is {1}.{0}'s birthday is on {2}".format('fred',23,"21 oct 96"))

print("current position {latitude} {longitude}".format(latitude="60N",longitude
                                                       ="5E"))
pos=(54.2,23.1,34.4)
print("The position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos))

import math
print("Math constants:pi={m.pi},e={m.e}".format(m=math))
print("Math constants:pi={m.pi:.3f},e={m.e:.3f}".format(m=math))




























