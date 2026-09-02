class PizzaParlor: #Pascal case
    
    def __init__(self, pepperoni, mushrooms, extra_cheese):
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.extra_cheese = extra_cheese
        
    def pizza_making(self):
        while True:
            topping_amount = input("Add topping or are you done?")
            if topping_amount == "pepperoni" or topping_amount == "mushroom" or topping_amount == "extra cheese":
                print(f"{topping_amount} added")
            elif topping_amount == "Done":
                break
            else:
                print("not in the menu")
                
    def calculate_total(self):
        self.total = self.pepperoni + self.mushrooms + self.extra_cheese
        
        self.total_cost = self.total * 1.5
        
        print(f"Total cost of pizza is: ${self.total_cost}")
    
        
                