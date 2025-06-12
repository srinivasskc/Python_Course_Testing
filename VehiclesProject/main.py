from car import Car
from truck import Truck

my_car = Car("Tesla","Model x",2023,True)
print(my_car.start_engine())

my_old_car = Car("Tata", "Tiago", 2016, False)
print(my_old_car.start_engine())


my_truck = Truck(make="Ford", model="F-150", year=2020, cargo_capacity=1000)

print(my_truck.start_engine())

#print(my_truck.__cargo_capacity)  This is throwing an error. Truck object does not have cargo capacity.
print(my_truck._Truck__cargo_capacity)


print(my_truck.load_cargo(500))
