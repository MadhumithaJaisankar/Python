class shapes:
    def __init__(self, name):
        self.name = name
        print(name)

    def square(self,side):
        return side*side
    
    def triangle(self,breadth,height):
        return breadth*height*1/2
    
    def rectangle(self,length, breadth):
        return length*breadth

# Creating an object of the shapes class
area = shapes("square")
print(area.square(43))
area=shapes("triangle")
print(area.rectangle(23,21))
area=shapes("rectangle")
print(area.rectangle(33,11))
# Accessing attributes and calling a method

