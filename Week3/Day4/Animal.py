class Animal:
    def __init__ (self, species):
        self.species=species
    
    def sound(self):
        return (f"{self.species} makes a sound")

class Dog(Animal):
    def __init__ (self, breed):
        super().__init__("Dog")
        self.breed=breed

    def bark(self):
        return (f"{self.breed} barks")

boston_terrier = Dog("Boston Terrier")

#boston_terrier.bark()
#boston_terrier.sound()

print(boston_terrier.bark(), boston_terrier.sound())