#Assignment 1: Design Your Own Class! 🏗️
#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.
class Smartphone:
    def __init__(self,model,processor,cost):
        self.model=model
        self.processor=processor
        self.cost=float(cost)
    def power_on(self):
        print(f"{self.model},is being Turned On!")
    def info(self):
        print(f"The phone model is {self.model},it operates under {self.processor} and the cost of buying it is {self.cost} $")
class Laptop(Smartphone):
    def info(self):
        print(f"""Laptop model:{self.model} ,processor:{self.processor},cost:{self.cost}""")
phone1=Smartphone("Samsung","Snapdragon",20000)
laptop1=Laptop("HP","Intel Core",36000)
phone1.power_on()
phone1.info()
laptop1.power_on()
laptop1.info()
