a=496
print(id(a)) #id()-->returns unique identifier for an object
b=1792
print(id(b))
print(id(b)==id(a))

m=[1,2,3]
def modify(k):
    k.append(4)
    print("k=",k)
    
modify(m)
print(m)

f=[1,2,3]
def replace(g):
    g=[5,6,7]
    print("g=",g)
replace(f)
print(f)

f=[1,2,3]
def replace_content(g):
    g[0]=5
    g[1]=6
    g[2]=7
    print("g=",g)
replace_content(f)
print(f)

def banner(msg,border='-'):
    line=border*len(msg)
    print(line)
    print(msg)
    print(line)
banner(" Hello how are you")
banner("Hello how are you", "*")
banner("Hello how are you", border="*")
banner(border=".", msg="Hello how are you")