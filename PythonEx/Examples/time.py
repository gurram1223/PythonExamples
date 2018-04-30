import time
print(time.ctime())
print("-------------------------------------")
#default argument values are evaluated when def is evaluated.They can be modified like anuy other object
def show_default(arg=time.ctime()):
    print(arg)
show_default()  
print("-------------------------------------")
def add_spam(menu=[]):
    menu.append("spam")
    return menu
breakfast=["bacon", "eggs"]
lunch=["baked beans"]
res=add_spam(breakfast) 
res1=add_spam(lunch) 
print(res,res1)
print(add_spam())
print(add_spam())
print(add_spam())

print("-------------------------------------")
def add_spam1(menu=None):
    if menu is None:
        menu=[]
    menu.append('spam')
    return menu

print(add_spam1())
print(add_spam1())
print(add_spam1())

    