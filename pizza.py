import csv
import datetime

# create superclass
# add description and cost 
class BasePizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

# get_description instance method
    def get_description(self):
        return self.description

# get_cost instance method
    def get_cost(self):
        return self.cost

#types of pizza
# ClassicPizza,MargheritaPizza,TurkPizza,PlainPizza classes are subclass of BasePizza

#set description,cost

class ClassicPizza(BasePizza):
    def __init__(self):
        super().__init__("Classic", 5.0)

class MargheritaPizza(BasePizza):
    def __init__(self):
        super().__init__("Margherita", 7.0)

class TurkPizza(BasePizza):
    def __init__(self):
        super().__init__("Turk", 10.0)

class PlainPizza(BasePizza):
    def __init__(self):
        super().__init__("Plain", 6.0)

# Decorator is inherited from BasePizza 
# Decorator class is superclass of olive,mushroom,goatcheese,onion,corn,meat classes
class Decorator(BasePizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_cost(self):
        return self.component.get_cost() 
        
    def get_description(self):
        return self.component.get_description() 
     

#subclass
class Olive(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 0.1
        self.description = "Olive"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost
#subclass    
class Mushroom(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 0.2
        self.description = "Mushroom"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost
#subclass    
class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 0.3
        self.description = "Goat Cheese"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

#subclass
class Onion(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 0.3
        self.description = "Onion"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost
    
#subclass    
class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 0.3
        self.description = "Corn"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost
    
#subclass    
class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 0.5
        self.description = "Meat"

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost

#open Menu.txt file
def main():
    with open("Menu.txt", "r") as menuFile:
        print(menuFile.read())

#get customer's pizza choice
    pizzaType = input("Please choose a pizza base -enter the number-: ")
    pizzaType = int(pizzaType)
   
    if pizzaType == 1:
        pizza = ClassicPizza()
    elif pizzaType == 2:
        pizza = MargheritaPizza()
    elif pizzaType == 3:
        pizza = TurkPizza()
    elif pizzaType == 4:
        pizza = PlainPizza()
    else:
        print("Invalid Choice.")
        return

#get customer's sauce choice
    sauceType = input("Please choose a sauce -enter the number-: ")
    sauceType = int(sauceType)

    if sauceType == 11:
        pizza = Olive(pizza)
    elif sauceType == 12:
        pizza = Mushroom(pizza)
    elif sauceType == 13:
        pizza = GoatCheese(pizza)
    elif sauceType == 14:
        pizza = Meat(pizza)
    elif sauceType == 15:
        pizza = Onion(pizza)
    elif sauceType == 16:
        pizza = Corn(pizza)
    else:
        print("Invalid choice.")
        return


    totalCost = pizza.get_cost()
   
#get customer's info
    costumerInfo = {}
    costumerInfo["name"] = input("Enter your name: ")
    costumerInfo["id"] = input("Enter your ID number: ")
    costumerInfo["creditCardNo"] = input("Enter your credit card number: ")
    costumerInfo["creditCardPassword"] = input("Enter your credit card password: ")
    costumerInfo["description"] = pizza.get_description()
   
#write customer's info to csv file
    with open("Orders.csv", "a", newline="") as ordersFile:
        writer = csv.writer(ordersFile)
        writer.writerow([costumerInfo["name"], costumerInfo["id"], costumerInfo["creditCardNo"],
                        costumerInfo["creditCardPassword"], costumerInfo["description"], datetime.datetime.now()])
        
    print("Thank you")
    print(f"Name: {costumerInfo['name']}")
    print(f"ID: {costumerInfo['id']}")
    print(f"Credit Card No: {costumerInfo['creditCardNo']}")
    print(f"Description: {costumerInfo['description']}")
    print(f"Total Cost: {totalCost}")


if __name__ == "__main__":
    main()
