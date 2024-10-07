class Animal:
    def __init__(self, species):
        self.species = species
    
    def bark(self):
        print("Animal is barking")
        

class Dog(Animal):
    def __init__(self, species, name):
        self.species = species
        self.name = name
        super().__init__(species)
        
        
sam = Dog("Canis lupus", "Sam")
print(sam.species)
sam.bark()