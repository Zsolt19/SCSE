import random
import getpass

# Exercise 1: Birthday Message Function
def birthday_message(name, age):
    print(f"Happy Birthday {name}! I hear you are {age} today!")

# Exercise 2: Drink Order Function
def drink_order(size, type_of_drink):
    print(f"You've ordered a {size} {type_of_drink}.")

# Exercise 3: Cash Machine Function
def cash_machine(pin, entered_pin, amount, balance):
    if pin == entered_pin:
        if amount <= balance:
            balance -= amount
            print("Cash is being dispensed.")
            print(f"New balance: ${balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Incorrect PIN.")

# Exercise 4: List Operations
def list_operations():
    fav_sports = ["Soccer", "Basketball", "Tennis", "Baseball", "Volleyball"]
    fav_sports.append("Hockey")
    print(f"List after adding Hockey: {fav_sports}")
    print(f"First 4 elements: {fav_sports[:4]}")
    print(f"5th element: {fav_sports[4]}")
    fav_sports[5] = "Ice-Hockey"
    print(f"List after replacing Hockey with Ice-Hockey: {fav_sports}")
    fav_sports.pop(1)
    print(f"List after removing the 2nd element: {fav_sports}")
    fav_sports.reverse()
    print(f"List after reversing: {fav_sports}")
    fav_sports.sort()
    print(f"List after sorting: {fav_sports}")
    fav_sports.remove("Ice-Hockey")
    print(f"List after popping Ice-Hockey: {fav_sports}")
    fav_sports.clear()
    print(f"List after clearing all elements: {fav_sports}")

# Exercise 5: Roll The Dice
def roll_the_dice():
    dice_roll = random.randint(1, 6)
    print(f"Dice rolled: {dice_roll}")
    if dice_roll == 6:
        print("Congrats! Move 2 spaces!")
    else:
        print("Try again!")

# Exercise 6: Tuple Operations (Grocery Inventory)
def grocery_inventory():
    inventory = [
        ("Apple", 1.0, 50),
        ("Banana", 0.5, 100),
        ("Orange", 1.2, 30),
        ("Milk", 1.5, 20)
    ]
    total_value = sum([item[1] * item[2] for item in inventory])
    print(f"Total inventory value: ${total_value:.2f}")
    restock_items = [item[0] for item in inventory if item[2] < 50]
    print(f"Items that need restocking: {restock_items}")

# Exercise 7: Set Operations (Conference Attendees)
def conference_attendees():
    regular_attendees = {"Alice", "Bob", "Charlie"}
    vip_attendees = {"David", "Eve", "Alice"}
    speakers = {"Charlie", "David", "Frank"}
    
    print(f"Common attendees between regular and VIP: {regular_attendees & vip_attendees}")
    print(f"Unique regular attendees: {regular_attendees - vip_attendees}")
    print(f"All unique attendees: {regular_attendees | vip_attendees | speakers}")

# Exercise 8: Dictionary Operations (Store Inventory)
def store_inventory():
    inventory = {
        "Laptop": 10,
        "Smartphone": 20,
        "Headphones": 50,
        "Charger": 100
    }
    
    # Add new product
    inventory["Tablet"] = 30
    print(f"Updated inventory: {inventory}")
    
    # Check low-stock items
    low_stock_items = {key: value for key, value in inventory.items() if value < 30}
    print(f"Low stock items: {low_stock_items}")
    
    # Total quantity of products
    total_quantity = sum(inventory.values())
    print(f"Total quantity of products in stock: {total_quantity}")

# Main Menu System
def main_menu():
    while True:
        print("\nSelect an option:")
        print("1. Birthday Message")
        print("2. Drink Order")
        print("3. Cash Machine")
        print("4. List Operations")
        print("5. Roll The Dice")
        print("6. Grocery Inventory")
        print("7. Conference Attendees")
        print("8. Store Inventory")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            birthday_message(name, age)
        elif choice == '2':
            size = input("Enter size of the drink: ")
            type_of_drink = input("Enter type of drink: ")
            drink_order(size, type_of_drink)
        elif choice == '3':
            pin = "1234"  # Predefined pin
            entered_pin = getpass.getpass("Enter your PIN: ")
            amount = float(input("Enter amount to withdraw: "))
            balance = 1000  # Predefined balance
            cash_machine(pin, entered_pin, amount, balance)
        elif choice == '4':
            list_operations()
        elif choice == '5':
            roll_the_dice()
        elif choice == '6':
            grocery_inventory()
        elif choice == '7':
            conference_attendees()
        elif choice == '8':
            store_inventory()
        elif choice == '9':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
