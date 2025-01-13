'''# Python program to draw  
# Spiral  Helix Pattern 
# using Turtle Programming 
  
import turtle 
loadWindow = turtle.Screen() 
turtle.speed(2) 
  
for i in range(100): 
    turtle.circle(5*i) 
    turtle.circle(-5*i) 
    turtle.left(i) 
  
turtle.exitonclick() 
'''
'''# Python program to draw  
# Rainbow Benzene 
# using Turtle Programming 
import turtle 
turtle.clear()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x//100 + 1) 
    t.forward(x) 
    t.left(59) 
    print(x)
'''

'''import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(2)  # Set the line width

# Define a list of colors for the drawing
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw an abstract design
for i in range(36):
    t.color(colors[i % 6])  # Cycle through the colors
    t.forward(i * 10)  # Move forward by increasing lengths
    t.left(45)  # Turn the turtle by 45 degrees
    t.circle(i * 5)  # Draw a circle with increasing radius

# Hide the turtle after drawing
t.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
'''
'''import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(2)  # Set the line width

# Hide the turtle to improve performance
t.hideturtle()

# Draw an abstract design with random colors, angles, and shapes
for _ in range(100):
    t.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple", "white", "pink", "cyan", "magenta"]))
    t.forward(random.randint(20, 100))  # Move forward by a random distance
    t.left(random.randint(30, 180))  # Turn by a random angle
    t.circle(random.randint(20, 50))  # Draw a circle with a random radius

# Keep the window open until clicked
screen.exitonclick()
'''
'''import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(1)  # Start with a thin line

# Hide the turtle for better performance
t.hideturtle()

# Draw a highly abstract design with random shapes, colors, and sizes
for _ in range(200):
    t.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple", "white", "pink", "cyan", "magenta", "lime", "violet"]))
    t.pensize(random.randint(1, 5))  # Random line thickness
    t.forward(random.randint(50, 200))  # Move forward by a random distance
    t.left(random.randint(30, 120))  # Turn by a random angle
    t.circle(random.randint(10, 100))  # Draw a random circle
    t.right(random.randint(0, 360))  # Random turn to create chaotic effects

# Keep the window open until clicked
screen.exitonclick()
'''
'''import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)  # Optional: Change the screen size to 800x800

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(1)  # Start with a thin line
t.hideturtle()

# Screen boundaries (assume the screen is 400x400 centered at (0, 0))
boundary_limit = 350  # This will keep the turtle inside a square of size 700x700

# Function to check if the turtle is within the screen boundary
def check_boundary():
    x, y = t.position()
    return abs(x) < boundary_limit and abs(y) < boundary_limit

# Draw a highly abstract design with random shapes, colors, and sizes
for _ in range(300):  # Increase the number of steps for more complexity
    t.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple", "white", "pink", "cyan", "magenta", "lime", "violet"]))
    t.pensize(random.randint(1, 5))  # Random line thickness
    t.forward(random.randint(50, 150))  # Move forward by a random distance
    t.left(random.randint(30, 120))  # Turn by a random angle
    t.circle(random.randint(10, 50))  # Draw a random circle
    t.right(random.randint(0, 360))  # Random turn to create chaotic effects

    # If the turtle is about to go out of bounds, reset its position
    if not check_boundary():
        t.penup()
        t.setposition(random.randint(-boundary_limit, boundary_limit), random.randint(-boundary_limit, boundary_limit))  # Random repositioning within bounds
        t.pendown()

# Keep the window open until clicked
screen.exitonclick()
'''

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)  # Set screen size

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.width(2)  # Line thickness
t.hideturtle()  # Hide the turtle for faster drawing

# Predefined color palette (a harmonious, calm palette of warm tones)
color_palette = [
    "#D2691E",  # Chocolate (warm brown)
    "#FF4500",  # OrangeRed
    "#FF6347",  # Tomato (light red)
    "#FF7F50",  # Coral
    "#FFD700",  # Gold
    "#FFF8DC",  # Cornsilk (light cream)
    "#F0E68C",  # Khaki (light yellow-green)
]

# Function to draw a single polygon with a specific number of sides
def draw_polygon(sides, size):
    angle = 360 / sides  # Angle between each side
    for _ in range(sides):
        t.forward(size)
        t.left(angle)

# Function to draw a series of concentric polygons centered at (0, 0)
def draw_centered_polygons(sides, size, count, step, colors):
    for i in range(count):
        t.color(colors[i % len(colors)])  # Cycle through the color palette
        draw_polygon(sides, size)
        t.penup()
        t.forward(step)  # Move forward slightly to create space between polygons
        t.pendown()
        size += step  # Increase the size for the next polygon

# Function to draw a symmetrical, radial design
def draw_radial_design(sides, size, count, step, rotations, colors):
    for _ in range(rotations):
        draw_centered_polygons(sides, size, count, step, colors)
        t.right(360 / rotations)  # Rotate by a fraction of the full circle for symmetry

# Move to starting position (center of screen)
t.penup()
t.setposition(0, 0)  # Starting at the center
t.pendown()

# Adjust the maximum size to ensure the design fits within the screen
max_size = 120  # Maximum size of the polygons (this ensures the pattern fits within the screen)
step = 8  # Increment for each polygon's size
initial_size = 30  # Start with a smaller size to avoid clipping

# Calculate the number of concentric polygons based on size and screen constraints
count = (max_size - initial_size) // step

# Draw the radial design
draw_radial_design(sides=6, size=initial_size, count=count, step=step, rotations=12, colors=color_palette)  # Hexagons, 12 rotations (complete circle)

# Keep the window open until clicked
screen.exitonclick()
