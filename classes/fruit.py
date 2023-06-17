class Fruit:
    is_fruit = True
    
    def __init__(self, name, color, is_sweet):
        self.name = name
        self.color = color
        self.is_sweet = is_sweet

    def my_fruit(self):
        return f"{self.name} are {self.color} in color are very sweet."


fruit1 = Fruit("Apple", "Red", True)
fruit2 = Fruit("Banana", "Yellow", True)

print(fruit1.my_fruit()) 
print(fruit2.my_fruit()) 