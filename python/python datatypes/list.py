myList= ["list","tuple","dictionary"]

#list operations
print("printing the list")
print(myList)
#printing single element in the list
print(myList[0])
#negative indexing
print(myList[-2])

#size of the list
size=len(myList)
print("size of the list")
print(size)

#appending elements to the list
myList.append("set")
print("appended list")
print(myList)

#inserting an element in a certain position in the list
myList.insert(2,"duplicate")
print("list after insertion",myList)

#inserting multiple elements using extend()
l=["sequence",3,4.2]
myList.extend(l)
print("list after extending")
print(myList)

#removing an element from the list
myList.remove(4.2)
print(myList)

#using pop()
myList.pop()
print(myList)

