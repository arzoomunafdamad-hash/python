from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name: {self.name}")
        print(f"Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):   
        pass



class Cat(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    
    def speak(self):
        print(f"{self.name} ({self.breed}) says: Meow! Meow!")


class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

    
    def speak(self):
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")


class Lion(Animal):
    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride

    
    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) says: ROARR!")


cat = Cat("Miko", "Home", "Ragdoll")
parrot = Parrot("Mona", "Rainforest", "Squawk")
lion = Lion("Kaira", "Savannah", "Pride of the Lion")

print("--- Animal Sound Show ---\n")
for animal in [cat, parrot, lion]:
    animal.display()
    animal.speak()
    print()



