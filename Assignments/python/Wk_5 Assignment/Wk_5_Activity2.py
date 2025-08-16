class Animal:
    """A basic animal class."""
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    """A dog class."""
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

    def move(self):
        print("Running on four legs")

class Cat(Animal):
    """A cat class."""
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        print("Meow!")

    def move(self):
        print("Sneaking quietly")

class Car:
    def move(self):
        print("Driving ")

class Plane:
    def move(self):
        print("Flying")

class Bicycle:
    def move(self):
        print("Riding")


# Let's use different animals!
animals = [Dog("Buddy", "Golden Retriever"), Cat("Whiskers", "Gray"), Animal("Generic Animal")]

for animal in animals:
    animal.make_sound()
    if hasattr(animal, 'move'):
        animal.move()
    else:
        print("This animal doesn't know how to move")

print("\n---Vehicles---")
vehicles = [Car(), Plane(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()