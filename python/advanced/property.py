class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

# Using the Circle class with properties
circle = Circle(5)
print(circle.radius)

circle.radius = 7
print(circle.radius)
