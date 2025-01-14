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

# Function to draw the letter 'A'
def draw_A():
    turtle.setheading(60)
    turtle.forward(60)
    turtle.right(120)
    turtle.forward(60)
    turtle.backward(30)
    turtle.right(120)
    turtle.forward(30)
    turtle.penup()
    turtle.backward(30)
    turtle.left(120)
    turtle.forward(30)

# Function to draw the letter 'B'
def draw_B():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.circle(-12.5, 180)
    turtle.right(180)
    turtle.circle(-12.5, 180)
    turtle.penup()
    turtle.right(180)
    turtle.forward(12.5)
    turtle.pendown()

# Function to draw the letter 'C'
def draw_C():
    turtle.setheading(0)
    turtle.penup()
    # turtle.right(180)
    turtle.forward(25)
    turtle.pendown()
    turtle.circle(25, -180)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(50)
    turtle.pendown()

# Function to draw the letter 'D'
def draw_D():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.circle(-25, 180)
    turtle.penup()
    turtle.right(180)
    turtle.forward(25)
    turtle.pendown()

# Function to draw the letter 'E'
def draw_E():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.backward(30)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(30)
    turtle.penup()
    #turtle.backward(50)
    turtle.pendown()

# Function to draw the letter 'F'
def draw_F():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(30)
    turtle.backward(30)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.penup()
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(30)
    turtle.penup()

# Function to draw the letter 'G'
def draw_G():
    turtle.setheading(0)
    turtle.penup()
    # turtle.right(180)
    turtle.forward(25)
    turtle.pendown()
    turtle.circle(25, -180)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(50)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(15)
    turtle.penup()
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(15)

# Function to draw the letter 'H'
def draw_H():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(25)
    # turtle.penup()
    turtle.backward(50)
    turtle.pendown()

# Function to draw the letter 'I'
def draw_I():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()

# Function to draw the letter 'J'
def draw_J():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.circle(-10, 180)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()

# Function to draw the letter 'K'
def draw_K():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(45)
    turtle.forward(35)
    turtle.backward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.penup()
    turtle.backward(35)
    turtle.right(45)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.pendown()

# Function to draw the letter 'L'
def draw_L():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(30)
    # turtle.penup()
    # turtle.backward(30)
    # turtle.pendown()

# Function to draw the letter 'M'
def draw_M():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(35)
    turtle.right(135)
    turtle.forward(50)
    turtle.penup()
    #turtle.backward(50)
    turtle.pendown()

# Function to draw the letter 'N'
def draw_N():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(58)
    turtle.left(150)
    turtle.forward(50)
    turtle.penup()
    turtle.backward(100)
    turtle.left(30)
    turtle.forward(58)
    turtle.setheading(0)
    turtle.forward(29)
    turtle.pendown()

# Function to draw the letter 'O'
def draw_O():
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.circle(25)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.pendown()

# Function to draw the letter 'P'
def draw_P():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.circle(-12.5, 180)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(12.5)
    turtle.pendown()

# Function to draw the letter 'Q'
def draw_Q():
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.circle(25)
    turtle.penup()
    turtle.setheading(45)
    turtle.forward(20)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()
    #turtle.setheading(180)
    #turtle.forward(60)
    turtle.pendown()

# Function to draw the letter 'R'
def draw_R():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.circle(-12.5, 180)
    #turtle.right(180)
    #turtle.forward(25)
    turtle.left(120)
    turtle.forward(29)
    turtle.penup()
    turtle.backward(29)
    turtle.right(30)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(15)
    turtle.pendown()

# Function to draw the letter 'S'
def draw_S():
    turtle.penup()
    turtle.forward(25)
    turtle.setheading(90)
    turtle.forward(37.5)
    turtle.pendown()
    turtle.circle(12.5, 270)
    #turtle.setheading(0)
    turtle.circle(-12.5, 270)
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.setheading(270)
    turtle.forward(12.5)
    turtle.pendown()

# Function to draw the letter 'T'
def draw_T():
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.backward(20)
    turtle.forward(40)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(50)
    turtle.pendown()

# Function to draw the letter 'U'
def draw_U():
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(37.5)
    # turtle.right(180)
    # turtle.forward(50)
    # turtle.setheading(0)
    turtle.circle(12.5, 180)
    turtle.forward(37.5)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(50)
    turtle.pendown()

# Function to draw the letter 'V'
def draw_V():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.right(150)
    turtle.forward(58)
    turtle.left(120)
    turtle.forward(58)
    turtle.right(150)
    turtle.penup()
    turtle.forward(50)
  #  turtle.backward(50)
    turtle.pendown()

# Function to draw the letter 'W'
def draw_W():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.right(150)
    turtle.forward(58)
    turtle.left(120)
    turtle.forward(29)
    turtle.right(120)
    turtle.forward(29)
    turtle.left(120)
    turtle.forward(58)
    turtle.right(150)
    turtle.penup()
    turtle.forward(50)
  #  turtle.backward(50)
    turtle.pendown()

# Function to draw the letter 'X'
def draw_X():
    turtle.pendown()
    turtle.setheading(60)
    turtle.forward(58)
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(29)
    turtle.pendown()
    turtle.setheading(300)
    turtle.forward(58)
    # turtle.penup()
    # turtle.backward(17.5)
    # turtle.right(45)
    # turtle.pendown()

# Function to draw the letter 'Y'
def draw_Y():
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(25)
    turtle.left(45)
    turtle.forward(35)
    turtle.backward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.penup()
    turtle.backward(35)
    turtle.setheading(270)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(25)
    turtle.pendown()

# Function to draw the letter 'Z'
def draw_Z():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(71)
    turtle.left(135)
    turtle.forward(50)
    turtle.penup()
    turtle.left(135)
    turtle.forward(71)
    turtle.left(135)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    #turtle.backward(50)
    turtle.pendown()

# Function to draw a word
def draw_word(word):
    for letter in word:
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

        # Move the turtle to the right for the next letter
        turtle.penup()
        turtle.setheading(0)
        turtle.forward(10)  # Adjust this value to control the spacing between letters
        turtle.pendown()

# Initialize the screen
turtle.speed(5)
turtle.penup()
turtle.goto(-200, 0)  # Position the turtle at the starting point
turtle.pendown()

# Get the word from the user
word = input("Enter a word: ").upper()

# Draw the word
draw_word(word)

# Hide the turtle and finish
#turtle.hideturtle()
turtle.done()
