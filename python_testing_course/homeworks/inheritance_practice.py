class Shape:
    def __init__(self, name: str):
        """Initialize the Shape class with a name."""
        self.name = name

class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__("Circle")  # Call the parent class's __init__ method
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)  # area of a circle formula: πr²
    

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        super().__init__("Rectangle")  # Call the parent class's __init__ method
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height # area of a rectangle formula: width * height

class Triangle(Shape):
    def __init__(self, base: int, height: int):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    def area(self):
        return (0.5 * self.base * self.height) # area of a triangle is 1/2 * base * height

# Example usage:
my_circle = Circle(5)
print(f"Created a {my_circle.name} with radius {my_circle.radius}")
print(f"area of circle is {my_circle.area()}")

my_rectangle = Rectangle(10, 20)
print(f"Created a {my_rectangle.name} with width {my_rectangle.width} and height {my_rectangle.height}")
print(f"area of rectangle is {my_rectangle.area()}")


my_triangle = Triangle(15, 25)
print(f"Created a {my_triangle.name} with base {my_triangle.base} and height {my_triangle.height}")
print(f"area of triangle is {my_triangle.area()}")

# This will create instances of Circle, Rectangle, and Triangle,
# each inheriting from the Shape class and initializing their specific attributes.
# The output will confirm the creation of each shape with its respective dimensions.
