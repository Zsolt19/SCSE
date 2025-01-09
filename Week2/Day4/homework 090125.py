def option_1(): #the program snippet for option 1
    number=input("Enter a number")
    if number>0:
        print("The number is positive")
    return


while True: #infinite loop for menu choice
    import os #imports the OS commands
    os.system('cls') #clears the screen
    print("Choose from the below menu:\n1. If example\n2. If else example\n3. Elif example\n4. For loop example\n5. while loop example\n6. Exit (Infinite loop/break example)") #prints out the menu
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    answer=input() #awaits for an answer fro the user
    answer=int(answer) #converts the user choice from string to integer
    if answer==1: #breaks the loop when appropriate answer received
        option_1()
    elif answer==2:

    elif answer==3:

    elif answer==4:

    elif answer==5:

    elif answer==6:
        break