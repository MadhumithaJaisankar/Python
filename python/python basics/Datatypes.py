def Stringtype():
    Str1="This is String datatype"
    print(Str1)

def Numerictype():
    print("These are some examples of int datatype")
    for i in range(-10,10):
        print(i)
    x=1.5
    print("These are some examples of float datatype")
    while x<10:
        print(x)
        x+=1

def Sequencetype():
    myList= ["list","tuple","dictionary"]
    myTuple=("list","tuple","dictionary")
    myDict={1:"list",2:"tuple",3:"dictionary"}
    mySet={"list","tuple","dictionary"}
    print(type(myList))
    print(type(myTuple))
    print(type(myDict))

def booleantype(n):
    result= True if n>0 else False
    print(result)

Stringtype()
Numerictype()
Sequencetype()
booleantype(7)
