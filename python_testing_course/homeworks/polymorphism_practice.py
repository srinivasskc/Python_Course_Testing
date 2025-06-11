class Vehicle:
    def move(self, name = None):
        if name is None:
            return "Vehicle is moving"
        else:
            return f"Vehicle {name} is moving"

class Car(Vehicle):
    def move(self, name=None):
        if name is None:
            return "Car is moving"
        else:
            return f"Car {name} is moving on the highway"

class Boat(Vehicle):
    def move(self, name=None):
        if name is None:
            return "Boat is moving"
        else:
            return f"Boat {name} is moving towards the shore"


my_vehicle = Vehicle()
print(my_vehicle.move())
print(my_vehicle.move("Tesla"))

my_car = Car()
print(my_car.move())
print(my_car.move("Tiago"))

my_boat = Boat()
print(my_boat.move())
print(my_boat.move("Airboat"))


