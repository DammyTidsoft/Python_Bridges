from abc import ABC, abstractmethod

# Abstract class representing a shape
class Shape(ABC):
    def __init__(self, color):
        self._color = color

    # Abstract method to calculate the area
    @abstractmethod
    def calculate_area(self):
        pass

    # Getter method for color
    def get_color(self):
        return self._color

    # Setter method for color
    def set_color(self, color):
        self._color = color


# Concrete class representing a Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    # Implementation of calculate_area abstract method
    def calculate_area(self):
        return 3.14 * self._radius * self._radius


# Concrete class representing a Rectangle
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self._length = length
        self._width = width

    # Implementation of calculate_area abstract method
    def calculate_area(self):
        return self._length * self._width


# Create Circle and Rectangle objects
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

# Accessing attributes using encapsulation (getter and setter methods)
print("Circle color:", circle.get_color())
circle.set_color("Green")
print("Circle color after update:", circle.get_color())

# Calling the calculate_area method
print("Circle area:", circle.calculate_area())
print("Rectangle area:", rectangle.calculate_area())
