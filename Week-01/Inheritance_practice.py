class Vehicle:
    def __init__(self,brand,year,color,mileage):
        self.brand = brand
        self.year = year
        self.color = color
        self.mileage = mileage

    def describe(self):
        print(f'car brand is {self.brand}')
        print(f'car manifutcher year is {self.year}')
        print(f'car color is {self.color}')
        print(f'car mileage is {self.mileage}')

class Bike(Vehicle):
    def __init__ (self,brand,year,color,mileage,doors):
        self.brand = brand  