class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

class Cat(Animal):
    def __init__(self, name, habitat,breed):
        Animal .__init__(self, name, habitat)
        self.breed = breed

c = Cat("Miko", "Home", "Ragdoll")
print(c.name)
print(c.habitat)
print(c.breed)