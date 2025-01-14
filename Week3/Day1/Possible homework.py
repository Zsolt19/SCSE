'''import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)  # Set screen size

# Create a turtle object
t = turtle.Turtle()
t.speed(3)  # Speed for drawing
t.hideturtle()  # Hide turtle for faster drawing

# Set up a color palette (for each letter)
color_palette = [
    "#FF6347",  # Tomato (red-orange)
    "#FF4500",  # OrangeRed
    "#FFD700",  # Gold
    "#32CD32",  # LimeGreen
    "#1E90FF",  # DodgerBlue
    "#9932CC",  # DarkOrchid
    "#FF69B4",  # HotPink
]

# Function to write a word with colored block letters
def write_colored_word(word):
    t.penup()
    # Move the turtle to the starting position (centered)
    t.setposition(-100, 0)
    t.pendown()

    # Cycle through the letters in the word
    for i, letter in enumerate(word):
        t.color(color_palette[i % len(color_palette)])  # Cycle through colors
        t.write(letter, font=("Arial", 80, "bold"))  # Write each letter with block style
        t.penup()
        t.forward(90)  # Space between letters
        t.pendown()

# Write the word on the screen (e.g., "HELLO")
write_colored_word("HELLO")

# Keep the window open until clicked
screen.exitonclick()
'''

'''import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)  # Set screen size

# Create a turtle object
t = turtle.Turtle()
t.speed(3)  # Speed for drawing
t.hideturtle()  # Hide turtle for faster drawing

# Set up a color palette (for each letter)
color_palette = [
    "#FF6347",  # Tomato (red-orange)
    "#FF4500",  # OrangeRed
    "#FFD700",  # Gold
    "#32CD32",  # LimeGreen
    "#1E90FF",  # DodgerBlue
    "#9932CC",  # DarkOrchid
    "#FF69B4",  # HotPink
]

# Function to write a word with colored block letters
def write_colored_word(word):
    t.penup()
    # Move the turtle to the starting position (centered)
    t.setposition(-100, 0)
    t.pendown()

    # Cycle through the letters in the word
    for i, letter in enumerate(word):
        t.color(color_palette[i % len(color_palette)])  # Cycle through colors
        t.write(letter, font=("Arial", 80, "bold"))  # Write each letter with block style
        t.penup()
        t.forward(90)  # Space between letters
        t.pendown()

# Ask the user for input and display the word
user_word = screen.textinput("Input", "Please enter a word to display: ")
if user_word:
    write_colored_word(user_word.upper())  # Make sure the word is in uppercase for consistency

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
t.speed(3)  # Speed for drawing
t.hideturtle()  # Hide turtle for faster drawing

# Set up a color palette
color_palette = [
    "#FF6347",  # Tomato (red-orange)
    "#FF4500",  # OrangeRed
    "#FFD700",  # Gold
    "#32CD32",  # LimeGreen
    "#1E90FF",  # DodgerBlue
    "#9932CC",  # DarkOrchid
    "#FF69B4",  # HotPink
]

# Move the turtle to the starting position
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Function to draw the letter 'A'
def draw_A():
    t.pendown()
    t.forward(60)  # Top horizontal
    t.left(120)
    t.forward(60)  # Left diagonal
    t.right(120)
    t.forward(60)  # Right diagonal
    t.backward(30)
    t.right(120)
    t.forward(30)  # Middle horizontal
    t.penup()

# Function to draw the letter 'B'
def draw_B():
    t.pendown()
    t.left(90)
    t.forward(100)  # Vertical line
    t.right(90)
    t.circle(-20, 180)  # Top curve
    t.right(180)
    t.circle(-20, 180)  # Bottom curve
    t.penup()

# Function to draw the letter 'C'
def draw_C():
    t.pendown()
    t.circle(50, 180)  # Half circle
    t.penup()

# Function to draw the letter 'D'
def draw_D():
    t.pendown()
    t.left(90)
    t.forward(100)  # Vertical line
    t.right(90)
    t.circle(-20, 180)  # Rounded part of the D
    t.penup()

# Function to draw the letter 'E'
def draw_E():
    t.pendown()
    t.forward(60)  # Top horizontal line
    t.backward(60)
    t.left(90)
    t.forward(50)  # Middle vertical line
    t.backward(50)
    t.right(90)
    t.forward(60)  # Bottom horizontal line
    t.penup()

# Function to draw the letter 'F'
def draw_F():
    t.pendown()
    t.forward(60)  # Top horizontal line
    t.backward(60)
    t.left(90)
    t.forward(50)  # Middle vertical line
    t.backward(50)
    t.penup()

# Function to draw the letter 'G'
def draw_G():
    t.pendown()
    t.circle(50, 180)  # Half circle
    t.left(90)
    t.forward(30)  # Horizontal part of G
    t.penup()

# Function to draw the letter 'H'
def draw_H():
    t.pendown()
    t.forward(60)  # Left vertical line
    t.backward(30)
    t.left(90)
    t.forward(30)  # Middle horizontal line
    t.backward(30)
    t.right(90)
    t.forward(60)  # Right vertical line
    t.penup()

# Function to draw the letter 'I'
def draw_I():
    t.pendown()
    t.forward(60)  # Top horizontal line
    t.backward(30)
    t.left(90)
    t.forward(100)  # Vertical line
    t.right(90)
    t.forward(30)  # Bottom horizontal line
    t.penup()

# Function to draw the letter 'J'
def draw_J():
    t.pendown()
    t.forward(60)  # Top horizontal line
    t.backward(30)
    t.left(90)
    t.forward(100)  # Vertical line
    t.right(90)
    t.circle(30, 180)  # Bottom curve
    t.penup()

# Function to draw the letter 'K'
def draw_K():
    t.pendown()
    t.left(90)
    t.forward(100)  # Vertical line
    t.backward(50)
    t.left(45)
    t.forward(50)  # Top diagonal
    t.backward(50)
    t.right(90)
    t.forward(50)  # Bottom diagonal
    t.penup()

# Function to write a word with colored block letters
def write_colored_word(word):
    t.penup()
    # Move the turtle to the starting position (centered)
    t.setposition(-200, 0)  # Start from the left of the screen
    t.pendown()

    # Cycle through the letters in the word
    for i, letter in enumerate(word):
        t.color(color_palette[i % len(color_palette)])  # Cycle through colors
        # Call the appropriate function for each letter
        if letter == 'A':
            draw_A()
        elif letter == 'B':
            draw_B()
        elif letter == 'C':
            draw_C()
        elif letter == 'D':
            draw_D()
        elif letter == 'E':
            draw_E()
        elif letter == 'F':
            draw_F()
        elif letter == 'G':
            draw_G()
        elif letter == 'H':
            draw_H()
        elif letter == 'I':
            draw_I()
        elif letter == 'J':
            draw_J()
        elif letter == 'K':
            draw_K()

        # After drawing a letter, ensure there's enough space
        t.penup()
        t.forward(20)  # Space between letters
        t.pendown()

        # Ensure that the turtle is properly aligned (reset to the baseline and face up)
        t.penup()
        t.setheading(0)  # Reset direction (horizontal)
        t.goto(t.xcor(), t.ycor())  # Ensure the turtle stays at the same baseline (horizontal)
        t.pendown()

# Ask the user for input and display the word
user_word = screen.textinput("Input", "Please enter a word to display: ")
if user_word:
    write_colored_word(user_word.upper())  # Make sure the word is in uppercase for consistency

# Keep the window open until clicked
screen.exitonclick()
