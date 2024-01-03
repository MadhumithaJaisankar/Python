class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Creating two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Adding two Point objects using operator overloading
result = p1 + p2

print(f"Resultant Point: ({result.x}, {result.y})")
