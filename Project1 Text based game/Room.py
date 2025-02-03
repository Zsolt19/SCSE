class Room:
    def __init__(self):
        """Initialize a room with name, description, linked rooms, character, and item."""
        self.name = None
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
    
    def set_name(self, room_name):
        """Set the name of the room."""
        self.name = room_name
    
    def set_description(self, room_description):
        """Set the description of the room."""
        self.description = room_description
    
    def get_name(self):
        """Return the name of the room."""
        return self.name
    
    def get_description(self):
        """Return the description of the room."""
        return self.description
    
    def describe(self):
        """Print a description of the room, including any characters or items present."""
        print(f"{self.name}\n--------------------\n{self.description}")
        if self.character:
            print(f"You see {self.character.get_name()} here.")
        if self.item:
            print(f"You notice a {self.item.get_name()} in the room.")
    
    def link_room(self, room, direction):
        """Link another room in a specified direction."""
        self.linked_rooms[direction] = room
    
    def move(self, direction):
        """Move to a linked room in the specified direction, if possible."""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self
    
    def set_character(self, character):
        """Place a character in the room."""
        self.character = character
    
    def get_character(self):
        """Return the character present in the room, if any."""
        return self.character
    
    def set_item(self, item):
        """Place an item in the room."""
        self.item = item
    
    def get_item(self):
        """Return the item present in the room, if any."""
        return self.item
