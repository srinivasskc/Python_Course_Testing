class Cars:
    wheels = 4
    # This is class Attribute that is shared by all instances of the Cars class.

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    # This is a simple class definition for a Car.
    # make, model, year are instance attributes that are unique to each instance of the Cars class.

    def drive(self, miles):
        print(f"The {self.make} {self.model} drove for {miles} miles.")
        # miles attribute is available only within the drive method.
        # make and model attributes are instance level.
    
    @classmethod
    def set_wheels(cls, num_wheels):
        cls.wheels = num_wheels
        print(f"All cars now have {cls.wheels} wheels.")
        # This is a class method that modifies the class attribute wheels for all instances of the Cars class.

    @staticmethod
    def miles_to_kilometers(miles):
        kilometers = miles * 1.60934
        print(f"{miles} miles is equal to {kilometers} kilometers.")
        return kilometers
        # This is a static method that converts miles to kilometers.
        # It does not depend on the instance or class attributes.