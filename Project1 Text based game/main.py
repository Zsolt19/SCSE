from Room import Room
from Item import Item
from Character import Character, Enemy, Friend

# Set up rooms
kitchen = Room()
kitchen.set_name("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

ballroom = Room()
ballroom.set_name("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance. There is a locked door to the north.")

dining_hall = Room()
dining_hall.set_name("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

# New rooms
library = Room()
library.set_name("Library")
library.set_description("A quiet room filled with dusty books and ancient scrolls.")

armory = Room()
armory.set_name("Armory")
armory.set_description("A room filled with weapons and armor. A shield hangs on the wall.")

garden = Room()
garden.set_name("Garden")
garden.set_description("A serene outdoor area with overgrown plants and a small fountain.")

dungeon = Room()
dungeon.set_name("Dungeon")
dungeon.set_description("A dark, damp room with chains hanging from the walls.")

throne_room = Room()
throne_room.set_name("Throne Room")
throne_room.set_description("A grand room with a massive throne at the center. An ogre stands guard.")

# Link rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(library, "east")
library.link_room(dining_hall, "west")
library.link_room(armory, "north")
armory.link_room(library, "south")
armory.link_room(garden, "east")
garden.link_room(armory, "west")
garden.link_room(dungeon, "south")
dungeon.link_room(garden, "north")
dungeon.link_room(library, "west")  # New connection between Dungeon and Library
library.link_room(dungeon, "east")  # New connection between Library and Dungeon
dungeon.link_room(throne_room, "east")
throne_room.link_room(dungeon, "west")

# Create enemies
goblin1 = Enemy()
goblin1.set_name("Goblin")
goblin1.set_description("A nasty little creature with sharp teeth.")
goblin1.set_weakness("sword")
kitchen.set_character(goblin1)

goblin2 = Enemy()
goblin2.set_name("Goblin")
goblin2.set_description("A nasty little creature with sharp teeth.")
goblin2.set_weakness("sword")
library.set_character(goblin2)

goblin3 = Enemy()
goblin3.set_name("Goblin")
goblin3.set_description("A nasty little creature with sharp teeth.")
goblin3.set_weakness("sword")
garden.set_character(goblin3)

ogre = Enemy()
ogre.set_name("Ogre")
ogre.set_description("A massive, terrifying creature with a club.")
ogre.set_weakness("shield")  # Shield is required to survive
throne_room.set_character(ogre)

# Create friend with key
key = Item()
key.set_name("Golden Key")
key.set_description("A shiny golden key that might open something important.")

friend = Friend()
friend.set_name("Gandalf")
friend.set_description("A wise old wizard with a long beard.")
friend.set_conversation("You shall not pass!... unless you defeated all those pesky Goblins.")
friend.set_item(key)
ballroom.set_character(friend)

# Create new friend in the Dungeon
informant = Friend()
informant.set_name("Aragorn")
informant.set_description("A rugged ranger with a keen eye for danger.")
informant.set_conversation("I can tell you how many Goblins remain. Talk to me for updates.")
dungeon.set_character(informant)

# Create items
sword = Item()
sword.set_name("Sword")
sword.set_description("A sharp steel sword, useful for fighting enemies.")
dining_hall.set_item(sword)

shield = Item()
shield.set_name("Shield")
shield.set_description("A sturdy shield that can protect you from harm.")
armory.set_item(shield)

# Track defeated goblins
defeated_goblins = 0

current_room = kitchen
inventory = []

print("Welcome to the game! Here are your possible commands:")
print("- north, south, east, west: Move between rooms")
print("- talk: Speak with a character in the room")
print("- fight: Engage in combat with an enemy")
#print("- ask: Request an item from a friend")
print("- take: Pick up an item in the room")
print("- use key: Use the golden key to unlock the exit door in the Ballroom")
print("- inventory: List all items in your inventory")
print("- exit: Quit the game")

while True:
    print("\n")
    current_room.describe()
    # Update the conversation based on the number of Goblins defeated
    if defeated_goblins == 3:
        friend.set_conversation("You shall now pass!...")
        informant.set_conversation("All Goblins have been defeated! You're ready to face the final challenge.")
    else:
        if defeated_goblins == 2:
            informant.set_conversation("You have defeated 2 Goblins. 1 remains.")
        elif defeated_goblins == 1:
            informant.set_conversation("You have defeated 1 Goblin. 2 remain.")
        else:
            informant.set_conversation("You have not defeated any Goblins. 3 remain.")

    # Display possible directions to move
    print("You can move in the following directions:")
    for direction, room in current_room.linked_rooms.items():
        print(f"- {direction.capitalize()} to {room.get_name()}")

    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        if command == "north" and current_room == ballroom:
            if any(item.get_name() == "Golden Key" for item in inventory):
                print("You unlocked the door with the Golden Key and escaped! You win the game!")
                break
            else:
                print("The door is locked. You need a Golden Key to unlock it.")
        elif current_room == throne_room:
            if any(item.get_name() == "Shield" for item in inventory):
                print("You use the shield to block the Ogre's attack and escape!")
                current_room.set_character(None)
            else:
                print("As you enter the Throne Room, the Ogre roars and charges at you!")
                print("You try to run, but the Ogre is too fast. It swings its massive club...")
                print("CRASH! The club smashes into you, and everything goes black.")
                print("You have been killed by the Ogre. Game Over.")
                break
        else:
            current_room = current_room.move(command)
    elif command == "fight":
        if isinstance(current_room.get_character(), Enemy):
            if current_room.get_character().get_name() == "Ogre":
                print("The Ogre is too powerful to fight! You need a shield to survive.")
            else:
                weapon = input("Choose your weapon: ")
                if any(item.get_name().lower() == weapon.lower() for item in inventory):
                    print(f"You swing your {weapon} at the Goblin!")
                    print("The Goblin screeches and lunges at you with its sharp teeth!")
                    print("You dodge just in time and strike again!")
                    if current_room.get_character().fight(weapon):
                        print("After a fierce struggle, you land a final blow!")
                        print("The Goblin collapses to the ground, defeated.")
                        defeated_goblins += 1
                        current_room.set_character(None)
                    else:
                        print("The Goblin dodges your attack and bites you!")
                        print("You fall to the ground, overwhelmed by the Goblin's ferocity.")
                        print("You have been defeated! Game Over.")
                        break
                else:
                    print("You don't have that weapon!")
        else:
            print("There is no enemy here to fight.")
    elif command == "talk":
        if isinstance(current_room.get_character(), Friend):
            if defeated_goblins < 3:
                print(f"{current_room.get_character().get_name()} says: {current_room.get_character().get_conversation()}")
            else:
                print(f"{current_room.get_character().get_name()} says: {current_room.get_character().get_conversation()}")
                item_received = current_room.get_character().give_item()
                if item_received:
                    inventory.append(item_received)
        else:
            print("There is no one to talk to here.")
    elif command == "take":
        if current_room.get_item():
            inventory.append(current_room.get_item())
            print(f"You picked up the {current_room.get_item().get_name()}.")
            current_room.set_item(None)
        else:
            print("There is nothing to take here.")
    elif command == "inventory":
        if inventory:
            print("Your inventory contains:")
            for item in inventory:
                print(f"- {item.get_name()}: {item.get_description()}")
        else:
            print("Your inventory is currently empty. Explore rooms to find items!")
    elif command == "exit":
        print("Thanks for playing!")
        break
    else:
        print("Invalid command. Type a valid command from the list above.")