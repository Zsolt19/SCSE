class Room:
    #constructor
    def __init__ (self):
        self.name=None
        self.description=None
        self.linked_rooms={}
    #getter description
    def get_description(self):
        return self.description
    #setter description
    def set_description(self, room_description):
        self.description=room_description   
    # return room description
    def describe(self):
        print(self.description)
    # getter room name
    def get_name(self):
        return self.name
    # setter room name
    def set_name(self, room_name):
        self.name=room_name
    #link rooms
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction]=room_to_link
        #print( self.name + " linked rooms: " + repr(self.linked_rooms))
    #getter linked rooms
    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room=self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
    #move to linked room
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self