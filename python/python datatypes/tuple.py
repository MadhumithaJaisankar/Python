myTuple=("list","tuple","dictionary")


#tuple operations
#accessing the elements of the tuple
print(myTuple)
print(myTuple[1])

#concatenation of tuples
myTuple2=(1,2,3,4,5)
con_tuple=myTuple+myTuple2
print("concatenated tuples")
print(con_tuple)

#slicing
print(con_tuple[::2])

#deleting a entire tuple
del myTuple2
try:
    print(myTuple2)
except NameError:
    print("item not found")
