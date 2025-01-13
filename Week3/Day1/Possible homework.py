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

# Functions to draw each letter (A-Z)

# Function to draw the letter 'A'
def draw_A():
    t.pendown()
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.backward(50)
    t.right(120)
    t.forward(50)
    t.penup()

# Function to draw the letter 'B'
def draw_B():
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-25, 180)
    t.right(180)
    t.circle(-25, 180)
    t.penup()

# Function to draw the letter 'C'
def draw_C():
    t.pendown()
    t.circle(50, 180)
    t.penup()

# Function to draw the letter 'D'
def draw_D():
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-25, 180)
    t.penup()

# Function to draw the letter 'E'
def draw_E():
    t.pendown()
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(100)
    t.penup()

# Function to draw the letter 'F'
def draw_F():
    t.pendown()
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.penup()

# Function to draw the letter 'G'
def draw_G():
    t.pendown()
    t.circle(50, 180)
    t.left(90)
    t.forward(50)
    t.penup()

# Function to draw the letter 'H'
def draw_H():
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.penup()

# Function to draw the letter 'I'
def draw_I():
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.backward(100)
    t.penup()

# Function to draw the letter 'J'
def draw_J():
    t.pendown()
    t.circle(50, 180)
    t.forward(50)
    t.penup()

# Function to draw the letter 'K'
def draw_K():
    t.pendown()
    t.left(90)
    t.forward(100)
    t.backward(50)
    t.right(135)
    t.forward(70)
    t.backward(70)
    t.left(90)
    t.forward(70)
    t.penup()

# Function to draw the letter 'L'
def draw_L():
    t.pendown()
    t.forward(100)
    t.backward(100)
    t.left(90)
    t.forward(50)
    t.penup()

# Function to draw the letter 'M'
def draw_M():
    t.pendown()
    t.forward(100)
    t.left(135)
    t.forward(70)
    t.right(90)
    t.forward(70)
    t.left(135)
    t.forward(100)
    t.penup()

# Function to draw the letter 'N'
def draw_N():
    t.pendown()
    t.forward(100)
    t.left(135)
    t.forward(70)
    t.right(135)
    t.forward(100)
    t.penup()

# Function to draw the letter 'O'
def draw_O():
    t.pendown()
    t.circle(50)
    t.penup()

# Function to draw the letter 'P'
def draw_P():
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-25, 180)
    t.penup()

# Function to draw the letter 'Q'
def draw_Q():
    t.pendown()
    t.circle(50)
    t.left(45)
    t.forward(50)
    t.penup()

# Function to draw the letter 'R'
def draw_R():
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-25, 180)
    t.right(180)
    t.circle(-25, 180)
    t.left(135)
    t.forward(70)
    t.penup()

# Function to draw the letter 'S'
def draw_S():
    t.pendown()
    t.circle(50, 180)
    t.left(180)
    t.circle(50, 180)
    t.penup()

# Function to draw the letter 'T'
def draw_T():
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)
    t.penup()

# Function to draw the letter 'U'
def draw_U():
    t.pendown()
    t.forward(100)
    t.left(90)
    t.circle(-50, 180)
    t.left(90)
    t.forward(100)
    t.penup()

# Function to draw the letter 'V'
def draw_V():
    t.pendown()
    t.left(70)
    t.forward(100)
    t.right(140)
    t.forward(100)
    t.penup()

# Function to draw the letter 'W'
def draw_W():
    t.pendown()
    t.left(70)
    t.forward(100)
    t.right(140)
    t.forward(100)
    t.left(140)
    t.forward(100)
    t.penup()

# Function to draw the letter 'X'
def draw_X():
    t.pendown()
    t.left(45)
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.penup()

# Function to draw the letter 'Y'
def draw_Y():
    t.pendown()
    t.left(60)
    t.forward(50)
    t.backward(50)
    t.right(120)
    t.forward(50)
    t.backward(50)
    t.left(60)
    t.forward(100)
    t.penup()

# Function to draw the letter 'Z'
def draw_Z():
    t.pendown()
    t.forward(100)
    t.backward(100)
    t.right(45)
    t.forward(100)
    t.backward(100)
    t.left(45)
    t.forward(100)
    t.penup()

# Function to write a word with colored block letters
def write_colored_word(word):
    t.penup()
    # Move the turtle to the starting position (centered)
    t.setposition(-100, 0)
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
        elif letter == 'L':
            draw_L()
        elif letter == 'M':
            draw_M()
        elif letter == 'N':
            draw_N()
        elif letter == 'O':
            draw_O()
        elif letter == 'P':
            draw_P()
        elif letter == 'Q':
            draw_Q()
        elif letter == 'R':
            draw_R()
        elif letter == 'S':
            draw_S()
        elif letter == 'T':
            draw_T()
        elif letter == 'U':
            draw_U()
        elif letter == 'V':
            draw_V()
        elif letter == 'W':
            draw_W()
        elif letter == 'X':
            draw_X()
        elif letter == 'Y':
            draw_Y()
        elif letter == 'Z':
            draw_Z()

        t.penup()
        t.forward(120)  # Space between letters
        t.pendown()

# Ask the user for input and display the word
user_word = screen.textinput("Input", "Please enter a word to display: ")
if user_word:
    write_colored_word(user_word.upper())  # Make sure the word is in uppercase for consistency

# Keep the window open until clicked
screen.exitonclick()
