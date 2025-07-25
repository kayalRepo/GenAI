import math

# Function to calculate area of a circle
def area_circle(radius):
    return math.pi * radius * radius

# Function to calculate area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Example usage
print("Area of Circle with radius 5:", area_circle(5))
print("Area of Rectangle with length 10 and width 4:", area_rectangle(10, 4))
print("Area of Triangle with base 6 and height 3:", area_triangle(6, 3))
