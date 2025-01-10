def option_1(): #the program snippet for option 1
    number=int(input("Enter a number"))
    if number>0:
        print("The number is positive\nPress enter to continue")
        input()
    return

def option_2(): #the program snippet for option 2
    number=int(input("Enter a number:"))
    if number%2==0:
        print("The number is even.\nPress enter to continue")
        input()
    else:
        print("The number is odd.\nPress enter to continue")
        input()
    return

def option_3(answer1): #the program snippet for option 3
    if answer1==1: #breaks the loop when appropriate answer received
        option_1()
    elif answer1==2:
        option_2()
    elif answer1==3:
        print("I'm the one sorting your menu choice out.\nPress enter to continue")
        input()
    elif answer1==4:
        option_4()
    elif answer1==5:
        option_5()
    return

def option_4(): #the program snippet for option 4
    import random

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Allow the player 3 guesses
    attempts = 3

    print("Guess the number between 1 and 10! You have 3 attempts.")

    # Loop through 3 attempts
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < secret_number:
            print("The secret number is larger.")
        elif guess > secret_number:
            print("The secret number is smaller.")
        else:
            print("Congratulations! You guessed the correct number.\nPress enter to continue")
            input()
            break
    else:
        print(f"Sorry, you've used all your attempts. The correct number was {secret_number}.\nPress enter to continue")
        input()

    return

def option_5(): #the program snippet for option 5
    import random

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Initialize variables
    attempts = 0
    max_attempts = 3

    print("Guess the number between 1 and 10! You have 3 attempts.")

    # Use a while loop to give the player 3 attempts
    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("The secret number is larger.")
        elif guess > secret_number:
            print("The secret number is smaller.")
        else:
            print("Congratulations! You guessed the correct number.\nPress enter to continue")
            input()
            break
    else:
        print(f"Sorry, you've used all your attempts. The correct number was {secret_number}.\nPress enter to continue")
        input()

    return


while True: #infinite loop for menu choice
    import os #imports the OS commands
    os.system('cls') #clears the screen
    
    print("Choose from the below menu:\n1. If example\n2. If else example\n3. Elif example\n4. For loop example\n5. while loop example\n6. Exit (Infinite loop/break example)") #prints out the menu
    
    answer=input() #awaits for an answer fro the user
    answer=int(answer) #converts the user choice from string to integer
    
    if answer==6:
        break
    else:
        option_3(answer)