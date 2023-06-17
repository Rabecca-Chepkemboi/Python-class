class Car:
    car_brand = "Toyota"

    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model

    def my_car(self):
        return f"The {self.color} {self.make} {self.model} car is beautiful."


car1 = Car("Red", "Camry", "2022")
car2 = Car("Blue", "Corolla", "2021")

print(car1.my_car()) 
print(car2.my_car()) 