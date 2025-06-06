from class_car import Cars
from class_driver import Driver


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # This is a simple class definition for a Cat.
    # init method initializes the name and age attributes of the Cat class.

my_cat = Cat("Whiskers", 2)
# Instance of Cat class = my_cat


print("-----")
my_car = Cars("Toyota", "Camry", 2020)
# Instance of Car class = my_car

my_driver = Driver("Srinivas", 36, "DL123456789")
# Instance of Driver class = my_driver

print("\n")
print("Printing the attributes of my_driver, my_car, and my_cat:")
print(f'{my_driver.age} Years old {my_driver.name} with license number {my_driver.license_number} is driving a {my_car.year} made {my_car.make} {my_car.model} car.')
print(f'{my_cat.name} is {my_cat.age} years old.')
print(f'The {my_car.make} car has {my_car.wheels} wheels.')
# This code creates instances of the Cat, Car, and Driver classes and prints their attributes.

print("\n")
print("----Printing the attributes of friends_car and friends_driver, friends_car_wheels:----")

friends_car = Cars("Honda", "Civic", 2019)
print(f"My friend's car is a {friends_car.year} {friends_car.make} {friends_car.model}.")

friends_driver = Driver("John", 30, "DL987654321") 
print(f"My friend's driver is {friends_driver.name}, who is {friends_driver.age} years old and has license number {friends_driver.license_number}.")
print(f"My friend's car has {friends_car.wheels} wheels.")


print("\n")
print("----Changing the attributes of my_car and my_car.wheels:----")

my_car.year = 2021
Cars.wheels = 5  # Changing the class attribute for all instances
print(f"My car is now a {my_car.year} made {my_car.make} model {my_car.model}.")
print(f"My car now has {my_car.wheels} wheels.")

print("\n")
print("----Changing the attributes of friends_car and friends_car.wheels:----")
friends_car.year = 2022
Cars.wheels = 6  # Changing the class attribute for all instances
print(f"My friend's car is now a {friends_car.year} made {friends_car.make} model {friends_car.model}.")
print(f"My friend's car now has {friends_car.wheels} wheels.")

print("\n")

print("----Using the drive method of my_car:----")
my_car.drive(100)
print("\n")
print("----Using the drive method of friends_car:----")
friends_car.drive(150)
print("\n")

Cars.set_wheels(8)  # Setting the wheels to 8 for all cars
print("----Using the class method set_wheels to change the wheels of all cars:----")
print(f"Now all cars have {Cars.wheels} wheels.")
print("\n")
print(my_car.wheels)
print(f"Now my car has {my_car.wheels} wheels.")
print("\n")
print(friends_car.wheels)
print(f"Now my friend's car has {friends_car.wheels} wheels.")
print("\n")

print("----Using the static method miles_to_kilometers:----")
kilometers = Cars.miles_to_kilometers(100)
print(f"100 miles is equal to {kilometers} kilometers.")
print("\n")
my_car.miles_to_kilometers(100)
friends_car.miles_to_kilometers(150)
print("\n")
