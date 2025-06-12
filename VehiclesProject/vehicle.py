class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.make} {self.model}/{self.year}'s engine is starting"


