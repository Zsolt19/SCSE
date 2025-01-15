
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




new_rectangle = Rectangle(5,7)
new_rectangle=Rectangle(11,15)

print(new_rectangle.get_width())
print(new_rectangle.get_height())

new_rectangle.set_width(19)
new_rectangle.set_height(20)

print(new_rectangle.get_width())
print(new_rectangle.get_height())
print(type(new_rectangle))