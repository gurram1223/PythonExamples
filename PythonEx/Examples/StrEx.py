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
    





