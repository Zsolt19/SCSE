
'''
# Defining private class
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

# Get method
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

# Set method    
    def set_width(self, new_width):
        self.__width=new_width

    def set_height(self, new_height):
        self.__height=new_height



    def calculate_area(self):
        return self.__width * self.__height


new_rectangle = Rectangle(5,7)
new_rectangle=Rectangle(11,15)

print(new_rectangle.get_width())
print(new_rectangle.get_height())

new_rectangle.set_width(19)
new_rectangle.set_height(20)

print(new_rectangle.get_width())
print(new_rectangle.get_height())
print("Area: ", new_rectangle.calculate_area())
print(type(new_rectangle))
'''
class MyClass:
    def __init__(self):
        self.__default_value = 10  # Default value that can't be overwritten

    @property
    def default_value(self):
        """This is a read-only property."""
        return self.__default_value


# Usage example:
obj = MyClass()

# Accessing the default value (this works)
print(obj.default_value)  # Output: 10

# Attempting to overwrite the value will fail because it's read-only
try:
    obj.default_value = 20  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")
