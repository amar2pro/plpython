#ACTIVITY ONE
# Parent Class
class Friend:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def introduce(self):
        print(f"My friend {self.name} lives in {self.location} and is {self.age} years old.")

    def hobby(self):
        print(f"{self.name} enjoys hanging out with friends.")


# Child Class (inherits from Friend)
class BestFriend(Friend):
    def __init__(self, name, age, location, known_for_years):
        super().__init__(name, age, location)  # Call parent constructor
        self.known_for_years = known_for_years

    # Polymorphism: override hobby()
    def hobby(self):
        print(f"{self.name} is my best friend! We've known each other for {self.known_for_years} years and love gaming together.")


# Create objects
friend1 = Friend("Lynn", 20, "Saika")
friend2 = Friend("Ted", 21, "Kiambu")
best_friend = BestFriend("Hope", 22, "Juja", 10)

# Using methods
friend1.introduce()
friend2.hobby()

best_friend.introduce()
best_friend.hobby()   # Overridden method

#ACTIVITY 2 
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("⛵ Boat is sailing on the water.")


# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # Each class executes its own move() method
