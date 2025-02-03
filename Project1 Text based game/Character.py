class Character:
    def __init__(self):
        self.name = None
        self.description = None
        self.conversation = None
    
    def set_name(self, char_name):
        self.name = char_name
    
    def set_description(self, char_description):
        self.description = char_description
    
    def set_conversation(self, char_conversation):
        self.conversation = char_conversation
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_conversation(self):
        return self.conversation
    
    def describe(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        if self.conversation:
            print(self.conversation)
    
    def talk(self):
        if self.conversation:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " doesn't have anything to say.")
    
    def fight(self):
        print(self.name + " doesn't want to fight with you")

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.weakness = None
    
    def set_weakness(self, enemy_weakness):
        self.weakness = enemy_weakness   
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
    
    def bribe(self):
        print("You try to bribe " + self.name + ", but it does not work!")
    
    def steal(self):
        print("You attempt to steal from " + self.name + " but fail and anger them!")
    
    def sleep(self):
        print(self.name + " is now asleep. You can safely pass!")
        return True

class Friend(Character):
    def __init__(self):
        super().__init__()
        self.item = None  # Friend can now hold an item
    
    def set_item(self, item):
        self.item = item  # Assign an item to the friend

    def get_item(self):
        return self.item
    
    def give_item(self):
        if self.item:
            print(f"{self.name} gives you the {self.item.get_name()}.")
            given_item = self.item
            self.item = None  # Remove item from friend
            return given_item
        else:
            print(f"{self.name} has nothing to give.")
            return None
    
    def hug(self):
        print("You give " + self.name + " a warm hug. They seem happy!")
    
    def give_gift(self, gift):
        print("You give " + self.name + " a " + gift + ". They appreciate it!")
