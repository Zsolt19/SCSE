class Character:
    def __init__(self):
        self.name=None
        self.description=None
        self.conversation=None
    
    def set_name(self, char_name):
        self.name=char_name
    
    def set_description(self, char_description):
        self.description=char_description
    
    def set_conversation(self, char_conversation):
        self.conversation=char_conversation
    
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
        print(self.conversation)
    
    def talk(self):
        print(self.name + " says: " + self.conversation)
    
    def fight(self):
        print(self.name + " doesn't want to fight with you")

class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.weakness=None
    
    def set_weakness(self, enemy_weakness):
        self.weakness=enemy_weakness   
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item==self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False